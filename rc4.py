#!/usr/bin/env python3

import argparse
import sys
import uuid
from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes


def encrypt(data):
    key = get_random_bytes(16)
    rc4 = ARC4.new(key)

    ct = rc4.encrypt(data)

    print("KEY: ", fmt_output(key))
    print("PAYLOAD SIZE: ", len(ct))
    return ct


def fmt_output(ct):
    p = '02x'
    fmt_data = '0x' + ',0x'.join(format(x, p) for x in ct)
    return fmt_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='aes.py')
    parser.add_argument(
        '-f', help='bin file to encrypt'
    )
    parser.add_argument(
        '--raw', dest='raw', help='Data will be saved as raw binary file.', action=argparse.BooleanOptionalAction, default='--no-raw'
    )
    args = parser.parse_args()
    if args.f == None:
        parser.print_help()
        sys.exit()

    with open(args.f, mode='rb') as file:
        buf = file.read()
        file.close()
        ciphertext = encrypt(buf)
        f_name = uuid.uuid4()

    if args.raw == True:
        with open(f"{f_name}.txt", mode='wb') as file:
            file.write(ciphertext)
            file.close()
            print(f"[+] Encrypted binary payload saved as {f_name}.txt!")
    else:
        file = open(f"{f_name}.txt", "w") 
        file.write(fmt_output(ciphertext))
        file.close()
        print(f"[+] Encrypted payload saved as {f_name}.txt!")
        