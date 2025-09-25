# -*- coding: utf-8 -*-
"""
Create and register sqlAlchemy models in QSA tree.

Para llamar a uno de estos se puede hacer desde cualquier script de la siguiente manera

from pineboolib.qsa import *

cli = Clientes() <- Este es un modelo disponible, nombre del mtd existente y comenzando en Mayuscula.

También es posible recargar estos modelos creados a raiz de los mtds. Se puede crear por ejemplo
(tempdata)/cache/nombre_de_bd/models/Clientes_model.py. Esta librería sobrecargará en el arbol qsa la previa por defecto.

Un ejemplo sería:

    from pineboolib.qsa import *
    from sqlalchemy.orm import reconstructor

    class Clientes(Clientes):
        @reconstructor

        def init(self):
            print("Inicializado", self.nombre)


        def saluda(self):
            print("Hola", self.nombre)


Ejemplo de uso:
    from pineboolib.qsa import *

    session = aqApp.session()

    for instance in session.query(Clientes).order_by(Clientes.codcliente):
        instance.saluda()

"""
from pineboolib.application.utils import path
from pineboolib.application import load_script, qsadictmodules
from pineboolib.application.database.orm import basemodel
from pineboolib import logging, application
from pineboolib.application.parsers.parser_mtd import pnmtdparser
import sqlalchemy  # type: ignore [import]


from typing import Any, List, Dict, cast, TYPE_CHECKING

if TYPE_CHECKING:
    from pineboolib.application.metadata import pntablemetadata  # pragma: no cover

LOGGER = logging.get_logger(__name__)
PROCESSED: List[str] = []
PENDING_RELATIONS = []


def register_metadata_as_model(metadata: "pntablemetadata.PNTableMetaData") -> bool:
    """Register a mtd as model."""

    name_ = metadata.name()

    if "%s_model" % name_ in PROCESSED:
        LOGGER.warning("Overwriting %s model" % name_)

    path_ = pnmtdparser.mtd_parse(metadata)
    return save_model(path_, name_)


def save_model(path_, name: str) -> bool:
    """Save model."""

    model_class = load_script.load_model(name, path_)

    if model_class is not None:
        # event.listen(model_class, "load", model_class._constructor_init)
        qsadictmodules.QSADictModules.set_qsa_tree(
            "%s_orm" % name, cast(basemodel.BaseModel, model_class)
        )
        sqlalchemy.event.listen(
            model_class,
            "load",
            model_class._constructor_init,  # type: ignore [attr-defined] # noqa: F821
        )

        for field in model_class.legacy_metadata[  # type: ignore [attr-defined] # noqa: F821
            "fields"
        ]:
            obj = getattr(model_class, field["name"], None)
            if obj is not None:
                sqlalchemy.event.listen(
                    obj,
                    "set",
                    model_class._changes_slot,  # type: ignore [attr-defined] # noqa: F821
                )

        if name not in PROCESSED:
            PROCESSED.append(name)

        func_ = getattr(model_class, "pending_relationships", None)
        if func_:
            PENDING_RELATIONS.append(func_)

        for pending_relation in PENDING_RELATIONS:
            if pending_relation():
                PENDING_RELATIONS.remove(pending_relation)

                LOGGER.info(
                    "Relaciones pendientes de %s , generadas al cargar %s"
                    % (pending_relation.__module__, name)
                )
                del pending_relation

        return True

    return False


def load_models() -> None:
    """Load all sqlAlchemy models."""
    # print("LOADING MODELS!!!")
    db_admin = application.PROJECT.db_admin_mode

    if application.PROJECT.conn_manager is None:
        raise Exception("Project is not connected yet")

    models_: Dict[str, Any] = {}
    views_: Dict[str, Any] = {}
    for action_name, action in application.PROJECT.actions.items():
        class_orm = action._class_orm

        if class_orm:
            if class_orm in PROCESSED:
                continue

            path_class_orm = path._path(class_orm, False)
            if not path_class_orm:
                LOGGER.warning(
                    "Se ha especificado un model (%s) en el action %s, pero el fichero no existe",
                    class_orm,
                    action_name,
                )
                continue

            models_[class_orm] = path_class_orm
            # print("***", class_orm)
            PROCESSED.append(class_orm)

    for key, file_ in application.PROJECT.files.items():
        if file_.filename.endswith("_model.py"):
            name = key[:-3]
            if name.endswith(".mtd_model"):
                name = "%s_model" % name[:-10]

            if name in PROCESSED:
                continue
            else:
                PROCESSED.append(name)
                models_[name] = file_.path()

    for key, data in models_.items():
        name = key[0:-6]
        save_model(data, name)
        metadata = application.PROJECT.conn_manager.manager().metadata(name, True)
        if metadata is not None:
            if metadata.isQuery():
                views_[name] = data
            else:
                application.PROJECT.conn_manager.manager().metadata(name)
    # views las últimas...
    for key, data in views_.items():
        save_model(data, key)
        if db_admin:
            application.PROJECT.conn_manager.manager().createTable(key)

    del models_
    del views_
