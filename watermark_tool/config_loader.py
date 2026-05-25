from pathlib import Path
import json


def load_config(config_path: str = "config.json") -> dict:
    # Convert the config path to a Path object.
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    # Read and parse the JSON configuration file.
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)