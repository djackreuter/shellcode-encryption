#!/usr/bin/env python3

import argparse
import sys
from Crypto.Random import get_random_bytes

def xor(data, key):
    rand_key = False
    if key == None:
        rand_key = True
        key = get_random_bytes(8)
    else:
        b_key = bytes(key, 'latin-1')
        key = b_key

    res = b''
    for i in range(len(data)):
        curr_key = key[i % len(key)]
        res += bytes(chr(data[i] ^ curr_key), 'latin-1')
        # Add null byte to the end
        # if i == len(data) - 1:
        #     res += b'\0'

    print_output(key, "KEY")
    return res

def print_output(ciphertext, ident):
    padding = '02x'
    data = '{ 0x' + ', 0x'.join(format(x, padding) for x in ciphertext) + ' };'
    print(f"{ident}: {data}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='xor.py')
    parser.add_argument(
        '-k', help='XOR key. Will create random 8 character key if ommited'
    )
    parser.add_argument(
       '-f', help='bin file containing payload' 
    )
    parser.add_argument(
        '-s', help='String to XOR'
    )
    parser.add_argument(
        '-w', help="File to write encrypted binary payload to"
    )
    args = parser.parse_args()

    if args.f == None and args.s == None:
        parser.print_help()
        sys.exit()

    if args.f != None:
        with open(args.f, mode='rb') as file:
            buf = file.read()
            file.close()
    else:
        buf = bytes(args.s, 'latin-1')

    ciphertext = xor(buf, args.k)
    if args.w != None:
        with open(args.w, mode='wb') as file:
            file.write(ciphertext)
            file.close
    else:
        print_output(ciphertext, "DATA")
