from abc import ABC, abstractmethod
import sqlite3
import os


class Database(ABC):
    def __init__(self, dbName: str) -> None:
        self._dbName: str = dbName

    @abstractmethod
    def connect(self) -> None:
        dbpath: str = os.getcwd() + f"/{self._dbName}"
        if not os.path.exists(dbpath):
            with open(dbpath, "w"):
                pass
            with open(os.getcwd() + "/DON'T_DELETE_database.db.txt", "w") as f:
                f.write(
                    """Please don't delete file with name "database.db", this file is generate automatically when you first time store your username and password. This file is used to store all your data, so please don't delete file with name "database.db". BE CAREFULL!!
                """
                )

        self._conn: sqlite3.Connection = sqlite3.connect(dbpath)
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()

    def close(self):
        self._conn.close()

    @abstractmethod
    def _createTable(self):
        pass

    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def add(self):
        pass
