#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    arg_count = len(arg)
    index = 1
    sum = 0
    while index <= arg_count:
        sum = sum + int(sys.argv[index])
        index += 1
    print("{:d}".format(sum))
