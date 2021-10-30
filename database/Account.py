from .Database import Database


class Account(Database):
    def __init__(self, dbName: str) -> None:
        super().__init__(dbName)
        self._table = "accounts"

        self.connect()

    def connect(self) -> None:
        super().connect()
        self._createTable()

    def _createTable(self):
        with self._conn:
            self._cursor.execute(
                f"""
            CREATE TABLE IF NOT EXISTS {self._table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                email TEXT,
                username TEXT,
                password TEXT NOT NULL,
                url TEXT,
                app_name TEXT NOT NULL
            )
            """
            )

    def add(
        self,
        password: str,
        app_name: str,
        email: str = "",
        username: str = "",
        url: str = "",
    ):
        with self._conn:
            sql = f"""
            INSERT INTO {self._table} (email, username, password, url, app_name)
            VALUES (:email, :username, :password, :url, :app_name)
            """
            values = {
                "email": email,
                "username": username,
                "password": password,
                "url": url,
                "app_name": app_name,
            }
            self._cursor.execute(sql, values)

    def find(self, app_name):
        with self._conn:
            account = self._conn.execute(
                f"SELECT * FROM {self._table} WHERE app_name LIKE :app_name",
                {"app_name": f"%{app_name}%"},
            ).fetchone()
            return account

    def delete(self, app_name):
        with self._conn:
            self._conn.execute(
                f"DELETE FROM {self._table} WHERE app_name=:app_name",
                {"app_name": app_name},
            )

    def update(self, app_name: str, updateValue: dict):
        with self._conn:
            updateField = ""
            for key in updateValue.keys():
                updateField += f"{key}=:{key} "
            updateField = ", ".join(filter(bool, updateField.split(" ")))

            self._cursor.execute(
                f"UPDATE {self._table} SET {updateField} WHERE app_name=:app_name",
                {**updateValue, "app_name": app_name},
            )
