from __future__ import annotations

import os
import pathlib
import types
from typing import Any

from pydantic import BaseModel, ConfigDict
from pydantic_settings import (
    BaseSettings,
    JsonConfigSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

__all__ = ("ConfigModel", "setup")


class ConfigModel(BaseModel):
    model_config = ConfigDict(frozen=True)


class _Settings(BaseSettings):
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        result = [init_settings]
        if cls.model_config.get("json_file"):
            result.append(JsonConfigSettingsSource(settings_cls))
        if cls.model_config.get("yaml_file"):
            result.append(YamlConfigSettingsSource(settings_cls))
        return tuple(result)


def setup[T: Any](settings_class: type[T], path: pathlib.Path | None = None) -> T:
    settings_path = (
        path
        or (pathlib.Path(os.environ["settings"]) if os.environ.get("settings") else None)
        or pathlib.Path("config.yaml")
    )

    if not settings_path.is_file():
        raise ValueError(f"Invalid settings path. File {settings_path} does not exist.")

    config: SettingsConfigDict = {"frozen": True}
    if settings_path.is_file():
        if settings_path.suffix == ".json":
            config["json_file"] = settings_path
        elif settings_path.suffix == ".yaml":
            config["yaml_file"] = settings_path
        else:
            raise ValueError(f"Unsupported settings format {settings_path.suffix}")

    settings = types.new_class(
        settings_class.__name__,
        (settings_class, _Settings),
        {},
        lambda ns: ns.update({"model_config": config}),
    )
    return settings()
