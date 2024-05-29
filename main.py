import sys, os, subprocess
import modules, coloring

if len(sys.argv) == 2:
    try:
        os.chdir(sys.argv[1])
    except FileNotFoundError:
        sys.exit("\x1b[31mDirectory not found.\x1b[0m")
elif len(sys.argv) > 2:
    sys.exit("\x1b[31mToo many arguments.\x1b[0m")

while True:
    print("\x1b[34m" + os.getcwd() + "\x1b[0m")
    print("0\t\x1b[32m..\x1b[0m")
    for i in range(len(os.listdir())):
        print(str(i + 1) + "\t", end="")
        if os.path.isfile(os.listdir()[i]):
            print("\x1b[33m" + os.listdir()[i] + "\x1b[0m")
        else:
            print("\x1b[32m" + os.listdir()[i] + "\x1b[0m")
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