import sys, os, subprocess
import modules
from coloring import coloring

if len(sys.argv) == 2:
    try:
        os.chdir(sys.argv[1])
    except FileNotFoundError:
        sys.exit(coloring("Directory not found.", "error"))
elif len(sys.argv) > 2:
    sys.exit(coloring("Too many arguments.", "error"))

while True:
    print(coloring(os.getcwd(), "chdir"))
    print("0\t", coloring("..", "dir"), sep="")
    for i in range(len(os.listdir())):
        print(str(i + 1) + "\t", end="")
        if os.path.isfile(os.listdir()[i]):
            print(coloring(os.listdir()[i], "file"))
        else:
            print(coloring(os.listdir()[i], "dir"))
    c = input("> ").split(" ")
    try:
        os.chdir((["../"] + os.listdir())[int(c[0])])
    except NotADirectoryError:
        subprocess.run("vim " + os.listdir()[int(c[0]) - 1], shell=True)
    except ValueError:
        if c[0] in ["e", "exit", "q", "quit"]:
            break
        else:
            modules.main(c)
sys.exit(0)