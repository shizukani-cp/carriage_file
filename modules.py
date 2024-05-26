import sys, os, shutil

EMPTY_CLIPBOARD_CONTENTS = {"fname":None,"content":None}
clipboard_contents = EMPTY_CLIPBOARD_CONTENTS

def num_to_name(n: int):
    return os.listdir()[int(n) - 1]

def clipboard(args: list[str]):
    if args[1] == "v":
        if not clipboard_contents == EMPTY_CLIPBOARD_CONTENTS:
            sys.exit("\x1b[31mThere are no items on the clipboard.\x1b[0m")
        try:
            with open(clipboard_contents["fname"], "xb") as f:
                f.write(clipboard_contents["content"])
        except FileExistsError:
            sys.exit("\x1b[31mFile already exists.\x1b[0m")
    elif args[1] == "c":
        try:
         if not os.path.isfile(num_to_name(args[2])):
            sys.exit("\x1b[31mIs not file.\x1b[0m")
        except IndexError:
            sys.exit("\x1b[31mMissing arguments.\x1b[0m")
        with open(num_to_name(args[2]), "rb") as f:
            clipboard_contents["fname"] = num_to_name(args[2])
            clipboard_contents["content"] = f.read()
    elif args[1] == "x":
        try:
         if not os.path.isfile(num_to_name(args[2])):
            sys.exit("\x1b[31mIs not file.\x1b[0m")
        except IndexError:
            sys.exit("\x1b[31mMissing arguments.\x1b[0m")
        with open(num_to_name(args[2]), "rb") as f:
            clipboard_contents["fname"] = num_to_name(args[2])
            clipboard_contents["content"] = f.read()
        os.remove(num_to_name(args[2]))
    else:
        sys.exit("\x1b[31mSubcommand not found.\x1b[0m")

def delete(args: list[str]):
    if os.path.isfile(num_to_name(args[1])):
        os.remove(num_to_name(args[1]))
    elif os.path.isdir(num_to_name(args[1])):
        shutil.rmtree(num_to_name(args[1]))

cTof = {
    "clipboard":clipboard,
    "c":clipboard,
    "del":delete,
    "delete":delete,
    "d":delete
}

def main(args: list[str]):
    try:
        f = cTof[args[0]]
    except KeyError:
        sys.exit("\x1b[31mCommand not found.\x1b[0m")
    else:
        f(args)