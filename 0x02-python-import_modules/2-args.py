#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_count = len(argv)
    index = 1
    if arg_count == 0:
        print("{:d} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{:d} argument:".format(arg_count))
        print("{:d}: {:s}".format(arg_count, sys.argv[index]))
    else:
        print("{:d} arguments:".format(arg_count))
        while index <= arg_count:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index += 1
