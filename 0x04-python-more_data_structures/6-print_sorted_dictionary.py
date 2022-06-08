#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_key = sorted(a_dictionary.items())
    for x, y in sort_key:
        print(f"{x}: {y}")
