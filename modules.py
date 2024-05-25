import sys

EMPTY_CLIPBOARD_CONTENTS = {"fname":None,"content":None}
clipboard_contents = EMPTY_CLIPBOARD_CONTENTS

def clipboard(command: str):
    args = command.split(" ")
    if args[1] == "v":
        if clipboard_contents == EMPTY_CLIPBOARD_CONTENTS:
            sys.exit("\x1b[31mThere are no items on the clipboard.\x1b[0m")
    elif args[1] == "c":
        pass
    elif args[1] == "x":
        pass
    else:
        sys.exit("\x1b[31mSubcommand not found.\x1b[0m")
    

cTof = {
    "clip":clipboard,
    "c":clipboard
}


def main(command: str):
    try:
        f = cTof[command]
    except KeyError:
        sys.exit("\x1b[31mCommand not found.\x1b[0m")
    else:
        f(command)