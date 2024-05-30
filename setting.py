import json, pathlib, subprocess

with open(pathlib.Path(subprocess.run("where cf", encoding='utf-8', stdout=subprocess.PIPE)
                       .stdout.split("\n")[0]).parent / "settings.json",
          "r", encoding="utf-8") as f:
    settings = json.loads(f.read())

def get_setting(name: str):
    return settings[name]