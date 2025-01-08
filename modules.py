import sys, os, shutil, subprocess
import pyperclip
from coloring import coloring

EMPTY_CLIPBOARD_CONTENTS = {"fname":None, "content":None}
clipboard_contents = EMPTY_CLIPBOARD_CONTENTS

def num_to_name(n: int):
    return os.listdir()[int(n) - 1]

def clipboard(args: list[str]):
    if args[1] == "v":
        if not clipboard_contents == EMPTY_CLIPBOARD_CONTENTS:
            sys.exit(coloring("There are no items on the clipboard.", "error"))
        try:
            with open(clipboard_contents["fname"], "xb") as f:
                f.write(clipboard_contents["content"])
        except FileExistsError:
            sys.exit(coloring("File already exists.", "error"))

    elif args[1] == "c":
        try:
         if not os.path.isfile(num_to_name(args[2])):
            sys.exit(coloring("Is not file.", "error"))
        except IndexError:
            sys.exit(coloring("Missing arguments.", "error"))
        with open(num_to_name(args[2]), "rb") as f:
            clipboard_contents["fname"] = num_to_name(args[2])
            clipboard_contents["content"] = f.read()

    elif args[1] == "x":
        try:
         if not os.path.isfile(num_to_name(args[2])):
            sys.exit(coloring("Is not file.", "error"))
        except IndexError:
            sys.exit(coloring("Missing arguments.", "error"))
        with open(num_to_name(args[2]), "rb") as f:
            clipboard_contents["fname"] = num_to_name(args[2])
            clipboard_contents["content"] = f.read()
        os.remove(num_to_name(args[2]))

    else:
        sys.exit(coloring("Subcommand not found.", "error"))

def delete(args: list[str]):
    if os.path.isfile(num_to_name(args[1])):
        os.remove(num_to_name(args[1]))

    elif os.path.isdir(num_to_name(args[1])):
        shutil.rmtree(num_to_name(args[1]))

def rename(args: list[str]):
    os.rename(num_to_name(args[1]), args[2])

def newfile(args: list[str]):
    try:
        with open(args[1], "x"):
            pass
    except FileExistsError:
        sys.exit(coloring("File already exists.", "error"))

def copy_chdir_command(args: list[str]):
    pyperclip.copy(f"cd {os.getcwd()}")

def shell(args: list[str]):
    subprocess.run(" ".join(args[1:]), shell=True)

cTof = {
    "clipboard": clipboard,
    "c": clipboard,
    "del": delete,
    "delete": delete,
    "d": delete,
    "rename": rename,
    "new": newfile,
    "chdir": copy_chdir_command,
    "shell": shell
}

def main(args: list[str]):
    try:
        f = cTof[args[0]]
    except KeyError:
        sys.exit(coloring("Command not found.", "error"))
    else:
        f(args)
