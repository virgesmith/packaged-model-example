from pathlib import Path
from typing import Annotated
import neworder
from packaged_model_example.environment import ModelConfig
from packaged_model_example.model import MyModel

import typer


def run_model(
    input_path: Annotated[Path, typer.Option(..., "--in", "-i", help="Path for input files")],
    config_file: Annotated[Path, typer.Option(..., "--config", "-c", help="Configuration file")],
    output_path: Annotated[Path, typer.Option(..., "--out", "-o", help="Path for outputs")],
) -> None:
    # Validate the inputs
    if not input_path.is_dir():
        raise KeyError(f"Input path ({input_path}) is not a valid folder")
    if not config_file.exists():
        raise KeyError(f"Config file not found: ({config_file}) does not exist")
    if not output_path.is_dir():
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"Created output directory {output_path}")

    config = ModelConfig.load(config_file)
    model = MyModel(config, input_path, output_path)

    neworder.run(model)
    neworder.log("Run complete")


def main() -> None:
    try:
        typer.run(run_model)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
