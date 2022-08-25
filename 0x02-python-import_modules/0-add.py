#!/usr/bin/python3

#"if __name__ == "__main__":" is added to make imported modules executable.
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
