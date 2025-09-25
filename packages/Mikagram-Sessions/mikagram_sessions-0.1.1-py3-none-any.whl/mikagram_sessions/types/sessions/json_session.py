import json
from dataclasses import dataclass

from mikagram_sessions.alias import PathLike


DEFAULT_SETTINGS = {
    "device": None,
    "app_version": None,
    "system_lang_code": None
}


@dataclass
class JsonSessionModel():
    api_id: int
    app_hash: str
    dc_id: int
    server_address: str
    port: int

    auth_key: str
    settings: dict
    version: int

    def to_dict(self) -> dict:
        return {
            "api_id": self.api_id,
            "app_hash": self.app_hash,
            "dc_id": self.dc_id,
            "server_address": self.server_address,
            "port": self.port,
            "auth_key": self.auth_key,
            "settings": self.settings,
            "version":  self.version
        }

    @classmethod
    def from_dict(cls, value: dict):
        return JsonSessionModel(
            api_id=value["api_id"],
            app_hash=value["app_hash"],
            dc_id=value["dc_id"],
            server_address=value["server_address"],
            port=value["port"],
            auth_key=value["auth_key"],
            settings=value.get("settings", DEFAULT_SETTINGS.copy()),
            version=value["version"]
        )

    @classmethod
    def from_file(cls, path: PathLike):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)

    def to_file(self, path: PathLike):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f)
