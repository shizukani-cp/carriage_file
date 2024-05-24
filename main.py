import sys, os

if len(sys.argv) == 2:
    try:
        os.chdir(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Directory not found.")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")

while True:
    print(os.getcwd())
    print("0\t..")
    for i in range(len(os.listdir())):
        print(str(i + 1) + "\t" + os.listdir()[i])
    c = input("> ")
    try:
        try:
            os.chdir((["../"] + os.listdir())[int(c)])
        except NotADirectoryError:
            sys.exit("It's canno't openable.")
    except ValueError:
        if c == "e":
            break
        else:
            sys.exit("Command not found.")
sys.exit(0)