import sys

def clipboard(command):
    pass

cTof = {
    "clip":clipboard,
    "c":clipboard
}


def main(command):
    try:
        f = cTof[command]
    except KeyError:
        sys.exit("\x1b[31mCommand not found.\x1b[0m")
    else:
        f(command)