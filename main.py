import sys, os

if len(sys.argv) == 2:
    try:
        os.chdir(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Directory not found.")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")
