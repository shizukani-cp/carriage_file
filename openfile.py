import re, subprocess, sys
import setting
from coloring import coloring

def open_file(fname: str):
    for program in setting.get_setting("open_program"):
        if re.fullmatch(program["file"], fname):
            subprocess.run(program["command"].replace("{filename}", fname), shell=True)
            return
    sys.exit(coloring("Unable to open file.", "error"))