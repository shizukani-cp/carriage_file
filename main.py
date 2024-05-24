import sys, os

if len(sys.argv) == 2:
    os.chdir(sys.argv[1])
elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")
