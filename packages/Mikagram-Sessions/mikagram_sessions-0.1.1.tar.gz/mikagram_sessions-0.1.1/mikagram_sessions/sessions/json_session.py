import ipaddress
from pathlib import Path
from typing import Any, Optional

from mikagram_sessions.alias import PathLike
from mikagram_sessions.types import JsonSessionModel

from .session import BaseSession
from . import defaults


EXTENSION = '.mika.json'
SESSION_VERSION = 1


class JsonSession(BaseSession):

    _file_path: Path
    _session_data: JsonSessionModel

    def __init__(
        self,
        file_path: PathLike,
    ):
        super().__init__(str(file_path))

        self.file_path = file_path  # type: ignore

        if self.file_path.exists():
            session_data = JsonSessionModel.from_file(self.file_path)
        else:
            session_data = JsonSessionModel.from_dict({
                "api_id": defaults.DEFAULT_API_ID,
                "app_hash": defaults.DEFAULT_APP_HASH,
                "dc_id": defaults.DEFAULT_DC,
                "auth_key": defaults.DEFAULT_AUTH_KEY,
                "server_address": defaults.DEFAULT_SERVER_ADDRESS,
                "port": defaults.DEFAULT_SERVER_PORT,
                "version": SESSION_VERSION
            })

        self._session_data = session_data

        # Set vars to super
        self._server_address = ipaddress.ip_address(self._session_data.server_address).compressed
        self._auth_key =bytes.fromhex(self._session_data.auth_key) if self._session_data.auth_key is not None else None
        self._dc_id = self._session_data.dc_id
        self._port = self._session_data.port

    def save(self):
        self._session_data.server_address = self._server_address or ""
        self._session_data.dc_id = self.dc_id
        self._session_data.port = self.port  # type: ignore

        key_bytes: bytes = self._auth_key if self._auth_key is not None else b""  # type: ignore
        self._session_data.auth_key = key_bytes.hex()

        self._session_data.to_file(self._file_path)

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

    def get_value(self, key: str, *, default: Any = None) -> Optional[Any]:
        if key == "api_id":
            return self._session_data.api_id
        elif key == "api_hash":
            return self._session_data.app_hash

        return self._session_data.settings.get(key, default)

    def set_value(self, key: str, value: Any):
        if key == "api_id":
            if not isinstance(value, int):
                raise TypeError(f"api_id should be int, not {type(value)}")
            self._session_data.api_id = value
        elif key == "api_hash":
            if not isinstance(value, str):
                raise TypeError(f"api_id should be str, not {type(value)}")
            self._session_data.app_hash = value
        else:
            self._session_data.settings[key] = value

        self.save()
