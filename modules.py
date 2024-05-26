import sys, os

EMPTY_CLIPBOARD_CONTENTS = {"fname":None,"content":None}
clipboard_contents = EMPTY_CLIPBOARD_CONTENTS

def clipboard(args: list[str]):
    if not os.path.isfile(args[2]): sys.exit("\x1b[31mIs not file.\x1b[0m")
    if args[1] == "v":
        if clipboard_contents == EMPTY_CLIPBOARD_CONTENTS:
            sys.exit("\x1b[31mThere are no items on the clipboard.\x1b[0m")
        with open(clipboard_contents["fname"], "xb") as f:
            f.write(clipboard_contents["conetent"])
    elif args[1] == "c":
        with open(args[2], "rb"):
            clipboard_contents["fname"] = args[2]
            clipboard_contents["conetent"] = f.read()
    elif args[1] == "x":
        with open(args[2], "rb"):
            clipboard_contents["fname"] = args[2]
            clipboard_contents["conetent"] = f.read()
        os.remove(args[2])
    else:
        sys.exit("\x1b[31mSubcommand not found.\x1b[0m")

cTof = {
    "clipboard":clipboard,
    "c":clipboard
}

def main(args: list[str]):
    try:
        f = cTof[args[0]]
    except KeyError:
        sys.exit("\x1b[31mCommand not found.\x1b[0m")
    else:
        f(args)