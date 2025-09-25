from typing import Optional

from .sqlite import SqliteSessionData, SqliteSession


class TelethonSqlite(SqliteSession):

    def fetch_session(self) -> Optional[SqliteSessionData]:
        with self._con:
            self._cur.execute("SELECT dc_id, server_address, port, auth_key FROM sessions")
            response = self._cur.fetchone()

        if response is None:
            return None
        return {
            "auth_key": response["auth_key"],
            "dc_id": response["dc_id"],
            "port": response["port"],
            "server_address": response["server_address"]
        }

    def save(self):
        with self._con:
            self._cur.execute(
                "INSERT OR REPLACE into sessions "
                "(dc_id, server_address, port, auth_key) "
                "VAlUES (?, ?, ?, ?)", (
                    self._dc_id,
                    self._server_address,
                    self._port,
                    self._auth_key if self._auth_key is not None else b''
                ))

    def create_new(self):
        stmts = (
            "CREATE TABLE IF NOT EXISTS sessions (dc_id integer primary key, server_address text, port integer, auth_key blob, takeout_id)",
            "CREATE TABLE IF NOT EXISTS entities (id integer primary key, hash integer not null, username text, phone integer, name text, date integer)",
            "CREATE TABLE IF NOT EXISTS sent_files (md5_digest blob, file_size integer, type integer, id integer, hash integer, primary key(md5_digest, file_size, type))",
            "CREATE TABLE IF NOT EXISTS update_state (id integer primary key, pts integer, qts integer, date integer, seq integer)",
            "CREATE TABLE IF NOT EXISTS version (version integer primary key)",
            "INSERT INTO version VALUES (7)"
        )
        with self._con:
            for stmt in stmts:
                self._con.execute(stmt)

    def check_tables(self) -> bool:
        tables = (
            "sessions",
            "entities",
            "sent_files",
            "update_state",
            "version"
        )

        for table in tables:
            if table not in self.get_tables():
                print(table)
                return False

        return True
