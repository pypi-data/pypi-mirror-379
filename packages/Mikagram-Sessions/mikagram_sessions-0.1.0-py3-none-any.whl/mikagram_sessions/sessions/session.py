from abc import ABC
from typing import Any, Optional, Union, overload


class BaseSession(ABC):
    session_name: str

    _dc_id = 0
    _server_address: Optional[str] = None
    _port: Optional[int] = None
    _auth_key: Optional[bytes] = None
    

    def __init__(self, session_name: str) -> None:
        self.session_name = session_name

    def on_update(self, key: str):
        ...

    def get_value(self, key: str, *, default: Optional[Any] = None) -> Optional[Any]:
        ...

    def set_value(self, key: str, value: Any):
        ...

    def set_dc(
        self,
        *,
        dc_id: Optional[int] = None,
        server_address: Optional[str] = None,
        port: Optional[int] = None
    ):
        self._dc_id = dc_id or 0
        self._server_address = server_address
        self._port = port
        self.on_update("dc")

    @property
    def dc_id(self):
        return self._dc_id

    @property
    def server_address(self):
        return self._server_address

    @property
    def port(self):
        return self._port

    @property
    def auth_key(self):
        return self._auth_key

    @auth_key.setter
    @overload
    def auth_key(self, value: str):
        """Set hex auth key
        """
        ...

    @auth_key.setter
    @overload
    def auth_key(self, value: bytes):
        """Set bytes auth key
        """
        ...

    @auth_key.setter
    def auth_key(self, value: Optional[Union[str, bytes]]):
        if isinstance(value, str):
            self._auth_key = bytes.fromhex(value)
        elif isinstance(value, bytes):
            self._auth_key = value
        else:
            raise TypeError(f"unexpected auth_key type {type(value)}")

        self.on_update("auth_key")

    @classmethod
    def from_session(cls, session: "BaseSession", new_name: str) -> "BaseSession":
        new_session = cls(new_name)

        new_session.set_dc(
            dc_id=session.dc_id,
            server_address=session.server_address,
            port=session.port
        )
        new_session.auth_key = session.auth_key

        #TODO: add addition sync
        return new_session

