import sys, os

if len(sys.argv) == 2:
    try:
        os.chdir(sys.argv[1])
    except FileNotFoundError:
        sys.exit("\x1b[31mDirectory not found.\x1b[0m")
elif len(sys.argv) > 2:
    sys.exit("\x1b[31mToo many arguments.\x1b[0m")

while True:
    print("\x1b[32m" + os.getcwd() + "\x1b[0m")
    print("0\t..")
    for i in range(len(os.listdir())):
        print(str(i + 1) + "\t" + os.listdir()[i])
    c = input("> ")
    try:
        try:
            os.chdir((["../"] + os.listdir())[int(c)])
        except NotADirectoryError:
            sys.exit("\x1b[31mIt's can't openable.\x1b[0m")
    except ValueError:
        if c == "e":
            break
        else:
            sys.exit("\x1b[31mCommand not found.\x1b[0m")
sys.exit(0)