#!/usr/bin/python3
if __name__ == "__main__"
    import sys

    count = len(sys.argv) - 1
    if count == 1:
        print("1 argument:")
    elif count == 0:
        print("0 argument.")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
