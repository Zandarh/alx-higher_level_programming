#!/usr/bin/python3
alp = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - alp)), end="")
    alp = 32 if alp == 0 else 0
