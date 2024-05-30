import os, json, pathlib

with open(pathlib.Path(os.path.dirname(__file__)) / "settings.json", "r", encoding="utf-8") as f:
    settings = json.loads(f.read())

def get_setting(name: str):
    return settings[name]