import json, pathlib, sys

with open(pathlib.Path(sys.argv[0]).parent / "settings.json",
          "r", encoding="utf-8") as f:
    settings = json.loads(f.read())

def get_setting(name: str):
    return settings[name]