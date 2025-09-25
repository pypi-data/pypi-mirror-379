import json
import pathlib

from spotag.models import Config

# use app.<name> to access config
CONFIG_DIR = pathlib.Path.joinpath(pathlib.Path.home(), ".raffleberry", "smt")
CONFIG_FILE = pathlib.Path.joinpath(CONFIG_DIR, "config.json")
ROOT_DIR = pathlib.Path.cwd()

config = Config("", "")


def _read_config(path):
    global config
    try:
        with open(path, "r") as f:
            data = json.load(f)
            config = Config(**data)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        _write_config(path, Config("", ""))
        raise Exception("Failed to read config, please configure your api keys")


def _write_config(path, data: Config):
    with open(path, "w") as f:
        f.write(json.dumps(data.dict, indent=4))


def init():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists():
        _write_config(CONFIG_FILE, config)
    _read_config(CONFIG_FILE)
