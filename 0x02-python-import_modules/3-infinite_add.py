#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    s = 0
    for i in range(1, args):
        arg = int(argv[i])
        s += arg
    print("{}".format(s))
