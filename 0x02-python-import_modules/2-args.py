#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        print("{} arguments.".format(args-1))
    if args > 1:
        for i in range(1, args):
            print("{} arguments:".format(args-1))
            print("{}: {}".format(i, sys.argv[i]))
