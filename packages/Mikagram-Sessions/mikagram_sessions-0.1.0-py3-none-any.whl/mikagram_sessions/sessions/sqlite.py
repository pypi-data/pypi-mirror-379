import ipaddress
import sqlite3
from pathlib import Path
from abc import abstractmethod
from typing import List, Optional, TypedDict

from mikagram_sessions.alias.pathlike import PathLike
from .session import BaseSession
from . import defaults


EXTENSION = '.session'


class SqliteSessionData(TypedDict):
    dc_id: int
    auth_key: bytes
    server_address: str
    port: int


class SqliteSession(BaseSession):
    _file_path: Path
    _con: sqlite3.Connection
    _cur: sqlite3.Cursor

    def __init__(self, file_path: PathLike, ):
        super().__init__(str(file_path))
        self.file_path = file_path  # type: ignore
        self._con = sqlite3.connect(self.file_path)
        self._con.row_factory = sqlite3.Row
        self._cur = self._con.cursor()

        self.fetch_data()

    def fetch_data(self):
        if not self.check_tables():
            self.create_new()

        data = self.fetch_session()

        if data is not None:
            self._server_address = ipaddress.ip_address(
                data["server_address"]
            ).compressed
            self._auth_key = data["auth_key"]
            self._dc_id = data["dc_id"]
            self._port = data["port"]

        else:
            self._server_address = ipaddress.ip_address(defaults.DEFAULT_SERVER_ADDRESS).compressed
            self._auth_key = defaults.DEFAULT_AUTH_KEY
            self._dc_id = defaults.DEFAULT_DC
            self._port = defaults.DEFAULT_SERVER_PORT

    def get_tables(self) -> List[str]:
        with self._con:
            self._cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            fetched_tables = self._cur.fetchall()

        return [el["name"] for el in fetched_tables]

    @abstractmethod
    def fetch_session(self) -> Optional[SqliteSessionData]:
        raise NotImplementedError("Should be implemented")

    @abstractmethod
    def save(self):
        raise NotImplementedError("Should be implemented")

    @abstractmethod
    def check_tables(self):
        raise NotImplementedError("Should be implemented")

    @abstractmethod
    def create_new(self):
        raise NotImplementedError("Should be implemented")

    @property
    def file_path(self) -> Path:
        return self._file_path

    @file_path.setter
    def file_path(self, value: PathLike):
        path_value = Path(value) if isinstance(value, str) else value
        if not path_value.name.endswith(EXTENSION):
            path_value = path_value.with_name(path_value.name + EXTENSION)
        self._file_path = path_value

    def on_update(self, key: str):
        self.save()
