#!/usr/bin/env python3

import argparse
import sys
from Crypto.Random import get_random_bytes

def gen_stack_string(data):
    data = data.strip()
    stack_string_contents = ['{ ']
    for i in range(len(data)):
        stack_string_contents.append(f"'{data[i]}', ")

    stack_string_contents.append("'\\0' };")
    print(''.join(stack_string_contents))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='gen_stack_string.py')
    parser.add_argument(
        '-s', help='Input string'
    )
    args = parser.parse_args()

    if args.s == None:
        parser.print_help()
        sys.exit()

    gen_stack_string(args.s)