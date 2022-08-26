#!/usr/bin/python3

if __main__ == "__name__"
    import sys

    arg = len(sys.argv) - 1
    if arg == 1:
        print("1 argument:")
    elif arg == 1:
        print("0 argument.")
    else:
        print(""{} arguments:".format(arg)")
    for i in range(arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
