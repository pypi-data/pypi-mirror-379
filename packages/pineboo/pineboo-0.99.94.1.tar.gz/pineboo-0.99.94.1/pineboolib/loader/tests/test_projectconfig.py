"""
Tests for loader.projectconfig.
"""
import os.path
import unittest
import tempfile
from unittest.mock import Mock, patch
from pineboolib.loader.projectconfig import ProjectConfig, VERSION_1_1, VERSION_1_2
from pineboolib.loader.projectconfig import PasswordMismatchError
from pineboolib.loader.tests import fixture_read

# from unittest.mock import patch, Mock


class TestProjectConfig(unittest.TestCase):
    """Test ProjectConfig class."""

    maxDiff = 50000

    def test_basic(self) -> None:
        """Test to create projectConfig class."""
        cfg = ProjectConfig(database="mydb", type="SQLite3 (SQLITE3)")
        self.assertTrue(cfg)
        self.assertEqual(cfg.SAVE_VERSION, VERSION_1_2)

    def test_read_write(self) -> None:
        """Test that we can read a file, save it back, read it again and stays the same."""
        project_test1 = fixture_read("project_test1.xml")
        with tempfile.TemporaryDirectory() as tmpdirname:
            cfg = ProjectConfig(
                database="mydb",
                type="SQLite3 (SQLITE3)",
                filename=os.path.join(tmpdirname, "test.xml"),
            )
            cfg.SAVE_VERSION = VERSION_1_1
            cfg.save_projectxml(False)
            file1_ = open(cfg.filename)
            data1_ = file1_.read()
            file1_.close()
            self.assertEqual(data1_, project_test1)
            cfg2 = ProjectConfig(load_xml=cfg.filename)
            cfg2.SAVE_VERSION = cfg2.version
            cfg2.save_projectxml(True)
            file2_ = open(cfg2.filename)
            data2_ = file2_.read()
            file2_.close()
            self.assertEqual(data2_, project_test1)

    @patch("time.time")
    @patch("os.urandom")
    def test_read_write2(self, mock_urandom: Mock, mock_time: Mock) -> None:
        """Test we can read and write and stays equal (slightly more complicated)."""
        # NOTE: urandom and time need to be mocked so hashes and ciphers always return the same value
        mock_urandom.side_effect = lambda n: b"1234567890123456789012345678901234567890"[:n]
        mock_time.side_effect = lambda: 10000
        project_test2 = fixture_read("project_test2.xml")
        project_test3 = fixture_read("project_test3.xml")
        with tempfile.TemporaryDirectory() as tmpdirname:
            # Verify Version 1.1
            cfg = ProjectConfig(
                database="postgres_testdb",
                description="Postgres Test DB",
                type="PostgreSQL (PSYCOPG2)",
                host="192.168.1.101",
                port=5432,
                username="postgres",
                password="postgrespassword",
                project_password="myhardtoguesspassword",
                filename=os.path.join(tmpdirname, "test.xml"),
            )
            cfg.SAVE_VERSION = VERSION_1_1
            cfg.save_projectxml(False)
            file0_ = open(cfg.filename)
            data0_ = file0_.read()
            file0_.close()
            self.assertEqual(data0_, project_test2)

            with self.assertRaises(PasswordMismatchError):
                ProjectConfig(load_xml=cfg.filename, project_password="wrongpassword")

            cfg2 = ProjectConfig(load_xml=cfg.filename, project_password="myhardtoguesspassword")
            cfg2.SAVE_VERSION = cfg2.version
            cfg2.save_projectxml(True)
            file1_ = open(cfg2.filename)
            data1_ = file1_.read()
            file1_.close()
            self.assertEqual(data1_, project_test2)

            # Verify Version 1.2
            cfg2.SAVE_VERSION = VERSION_1_2
            cfg2.save_projectxml(True)
            file2_ = open(cfg2.filename)
            data2_ = file2_.read()
            file2_.close()
            # print(open(cfg2.filename).read())
            self.assertEqual(data2_, project_test3)

            with self.assertRaises(PasswordMismatchError):
                ProjectConfig(load_xml=cfg2.filename, project_password="wrongpassword")

            cfg3 = ProjectConfig(load_xml=cfg2.filename, project_password="myhardtoguesspassword")
            cfg3.SAVE_VERSION = VERSION_1_2
            cfg3.save_projectxml(True)
            file3_ = open(cfg3.filename)
            data3_ = file3_.read()
            file3_.close()
            self.assertEqual(data3_, project_test3)
