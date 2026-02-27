from pathlib import Path
from pydantic_settings import BaseSettings
import tomllib


class Timeline(BaseSettings):
    start_year: int
    end_year: int
    step: int = 1


class File(BaseSettings):
    file: str


class GRegWt(BaseSettings):
    enabled: bool = False


class ModelConfig(BaseSettings):
    """Defines a model configuration, as found in the config file"""

    name: str
    verbose: bool = False
    timeline: Timeline

    baseline: File

    gregwt: GRegWt

    @classmethod
    def load(cls, path: Path) -> "ModelConfig":
        with path.open("rb") as fd:
            return ModelConfig(**tomllib.load(fd))
