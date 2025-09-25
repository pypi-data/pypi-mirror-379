"""Sys module."""

# -*- coding: utf-8 -*-
from pineboolib.qsa import qsa
import traceback
from pineboolib import logging


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pineboolib.interfaces import isqlcursor  # pragma: no cover

LOGGER = logging.get_logger(__name__)


class FormInternalObj(qsa.FormDBWidget):
    """FormInternalObj class."""

    def _class_init(self) -> None:
        """Inicialize."""
        # self.form = self
        self.current_user = None
        self.iface = self

    def init(self) -> None:
        """Init function."""
        settings = qsa.AQSettings()
        app_ = qsa.aqApp
        if not app_:
            return

        if qsa.SysType().isLoadedModule("flfactppal"):
            cod_ejercicio = None
            try:
                cod_ejercicio = qsa.from_project("flfactppal").iface.pub_ejercicioActual()
            except Exception as error:
                LOGGER.error(
                    "Module flfactppal was loaded but not able to execute <flfactppal.iface.pub_ejercicioActual()>"
                )
                LOGGER.error(
                    "... this usually means that flfactppal has failed translation to python"
                )
                LOGGER.exception(error)

            if cod_ejercicio:
                util = qsa.FLUtil()
                nombre_ejercicio = util.sqlSelect(
                    "ejercicios", "nombre", qsa.ustr("codejercicio='", cod_ejercicio, "'")
                )
                if qsa.AQUtil.sqlSelect("flsettings", "valor", "flkey='PosInfo'") == "True":
                    texto = ""
                    if nombre_ejercicio:
                        texto = qsa.ustr("[ ", nombre_ejercicio, " ]")
                    texto = qsa.ustr(
                        texto,
                        " [ ",
                        app_.db()
                        .mainConn()
                        .driverNameToDriverAlias(app_.db().mainConn().driverName()),
                        " ] * [ ",
                        qsa.SysType().nameBD(),
                        " ] * [ ",
                        qsa.SysType().nameUser(),
                        " ] ",
                    )
                    app_.setCaptionMainWidget(texto)

                else:
                    if nombre_ejercicio:
                        app_.setCaptionMainWidget(nombre_ejercicio)

                if not settings.readBoolEntry("application/oldApi", False):
                    valor = util.readSettingEntry("ebcomportamiento/ebCallFunction")
                    if valor:
                        funcion = qsa.Function(valor)
                        try:
                            funcion()
                        except Exception:
                            qsa.debug(traceback.format_exc())

    def afterCommit_flfiles(self, cur_files_: "isqlcursor.ISqlCursor") -> bool:
        """After commit flfiles."""

        if cur_files_.modeAccess() != cur_files_.Browse:
            value = cur_files_.valueBuffer("sha")

            _qry = qsa.FLSqlQuery()

            if _qry.exec_("SELECT sha FROM flfiles"):
                if _qry.size():
                    util = qsa.FLUtil()
                    value = ""
                    while _qry.next():
                        value = util.sha1("%s%s" % (value, _qry.value(0)))

            _cur_serial = qsa.FLSqlCursor("flserial", "dbaux")
            _cur_serial.select()
            _cur_serial.setModeAccess(
                _cur_serial.Edit if _cur_serial.first() else _cur_serial.Insert
            )
            _cur_serial.refreshBuffer()
            _cur_serial.setValueBuffer("sha", value)
            return _cur_serial.commitBuffer()

        return True

    def afterCommit_fltest(self, cursor: "isqlcursor.ISqlCursor") -> bool:
        """Aftercommit fltest."""
        util = qsa.FLUtil()

        if cursor.modeAccess() == cursor.Insert:
            cursor_pk = cursor.primaryKey()
            return cursor.valueBuffer(cursor_pk) == util.sqlSelect(
                "fltest", cursor_pk, "%s = %s " % (cursor_pk, cursor.valueBuffer(cursor_pk))
            )

        return True

    def get_description(*args) -> str:
        """Retrun description string."""

        return "Área de prueba T."

    def delegateCommit(cursor) -> bool:
        """Return default delegateCommit."""

        return qsa.from_project("formHTTP").iface.saveCursor(cursor)

    def controlDatosCacheo(self, cursor: "qsa.FLSqlCursor", updated: int) -> bool:
        """Return default controlDatosCacheo."""

        from pineboolib import application

        table_name: str = cursor.table()
        pk_name = cursor.primaryKey()
        pk_value = cursor.valueBuffer(pk_name)

        if "fldatatables_cache" not in application.PROJECT.actions.keys():
            qsa.debug("no hay ninguna acción con el nombre de fltadatable_cache")
            return True

        if table_name.endswith("_cachelite"):
            qsa.debug("la tabla es _cacheclite")
            return True

        meta = cursor.metadata()

        if not meta.useCachedFields():
            qsa.debug("%s no usa cachedfields %s" % (table_name, meta.cachedFields()))
            return True

        modoAcceso = {
            2: "Update",
            1: "Insert",
            3: "Delete",
        }

        if updated == 2:
            registros: str = meta.cachedFields()
            if registros != "*":
                camposCacheados = registros.split(",")
                cambios = False
                for campo in camposCacheados:
                    if cursor.valueBuffer(campo) != cursor.valueBufferCopy(campo):
                        cambios = True
                        break
                if not cambios:
                    qsa.debug("los campos actualizados no son cacheados")
                    return True

        if not qsa.AQUtil.execSql(
            "INSERT INTO fldatatables_cache(mode,tablename,pk_value,timestamp) VALUES ('%s', '%s', '%s',CURRENT_TIMESTAMP)"
            % (modoAcceso[updated], table_name, pk_value)
        ):
            qsa.debug("Ha fallado el insert")
            return False

        return True
