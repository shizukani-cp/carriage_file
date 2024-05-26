import sys, os

EMPTY_CLIPBOARD_CONTENTS = {"fname":None,"content":None}
clipboard_contents = EMPTY_CLIPBOARD_CONTENTS

def clipboard(args: list[str]):
    if args[1] == "v":
        if not clipboard_contents == EMPTY_CLIPBOARD_CONTENTS:
            sys.exit("\x1b[31mThere are no items on the clipboard.\x1b[0m")
        with open(clipboard_contents["fname"], "xb") as f:
            f.write(clipboard_contents["conetent"])
    elif args[1] == "c":
        try:
         if not os.path.isfile(os.listdir()[int(args[2]) - 1]):
            sys.exit("\x1b[31mIs not file.\x1b[0m")
        except IndexError:
            sys.exit("\x1b[31mMissing arguments.\x1b[0m")
        with open(os.listdir()[int(args[2]) - 1], "rb") as f:
            clipboard_contents["fname"] = os.listdir()[int(args[2]) - 1]
            clipboard_contents["content"] = f.read()
    elif args[1] == "x":
        try:
         if not os.path.isfile(os.listdir()[int(args[2]) - 1]):
            sys.exit("\x1b[31mIs not file.\x1b[0m")
        except IndexError:
            sys.exit("\x1b[31mMissing arguments.\x1b[0m")
        with open(os.listdir()[int(args[2]) - 1], "rb") as f:
            clipboard_contents["fname"] = os.listdir()[int(args[2]) - 1]
            clipboard_contents["content"] = f.read()
        os.remove(os.listdir()[int(args[2]) - 1])
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