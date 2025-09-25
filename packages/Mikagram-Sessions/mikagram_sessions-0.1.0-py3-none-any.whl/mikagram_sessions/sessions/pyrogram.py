import time
from typing import Optional

from mikagram_sessions.constants import DATACENTRES

from .sqlite import SqliteSession, SqliteSessionData
from . import defaults


class PyrogramSqlite(SqliteSession):

    def fetch_session(self) -> Optional[SqliteSessionData]:
        with self._con:
            self._cur.execute("SELECT dc_id, auth_key from sessions")
            response = self._cur.fetchone()

        if response is None:
            return None

        dc_ip = DATACENTRES[response['dc_id']]

        return {
            "auth_key": response["auth_key"],
            "dc_id": response["dc_id"],
            "port": defaults.DEFAULT_SERVER_PORT,
            "server_address": dc_ip
        }

    def save(self):
        with self._con:
            self._cur.execute(
                "INSERT OR REPLACE into sessions "
                "(dc_id, auth_key, date) VALUES (?, ?, ?)",
                (
                    self._dc_id,
                    self._auth_key if self._auth_key is not None else b'',
                    int(time.time())
                )
            )

    def create_new(self):
        stmts = (
            "CREATE TABLE peers (id INTEGER PRIMARY KEY, access_hash INTEGER, type INTEGER NOT NULL, username TEXT, phone_number TEXT, last_update_on INTEGER NOT NULL DEFAULT (CAST(STRFTIME('%s', 'now') AS INTEGER)))",
            "CREATE TABLE sessions (dc_id INTEGER PRIMARY KEY, test_mode INTEGER, auth_key BLOB, date INTEGER NOT NULL, user_id INTEGER, is_bot INTEGER)",
            "CREATE TABLE version (number INTEGER PRIMARY KEY)",
            "INSERT INTO version VALUES (2)"
        )

        with self._con:
            for stmt in stmts:
                self._con.execute(stmt)

    def check_tables(self) -> bool:
        tables = (
            "sessions",
            "peers",
            "version"
        )

        for table in tables:
            if table not in self.get_tables():
                return False

        return True
