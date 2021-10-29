from .Database import Database
import bcrypt


class User(Database):
    def __init__(self, dbName: str) -> None:
        super().__init__(dbName)
        self._table = "users"

    def connect(self) -> None:
        super().connect()
        self._createTable()

    def _createTable(self):
        with self._conn:
            self._cursor.execute(
                f"""
            CREATE TABLE IF NOT EXISTS {self._table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL        
            )
            """
            )

    def add(self, username: str, password: str) -> None:
        hashPassword = bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt()).decode(
            "utf-8"
        )
        with self._conn:
            self._cursor.execute(
                f"INSERT INTO {self._table} (username, password) VALUES (:username, :password)",
                {"username": username, "password": hashPassword},
            )

    def isEmpty(self) -> bool:
        count = self._cursor.execute(f"SELECT * FROM {self._table} LIMIT 1").fetchone()
        return not count

    def find(self, username, password):
        user = self._cursor.execute(
            f"SELECT * FROM {self._table} WHERE username=:username",
            {"username": username},
        ).fetchone()

        if not user:
            return False

        return bcrypt.checkpw(bytes(password, "utf-8"), bytes(user[2], "utf-8"))
