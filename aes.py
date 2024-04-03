#!/usr/bin/env python3

import argparse
import sys
import uuid
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def encrypt(data, key_size):
    key = get_random_bytes(key_size)
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(data, AES.block_size))
    if key_size == 16:
        print("AES-128")
    elif key_size == 24:
        print("AES-192")
    elif key_size == 32:
        print("AES-256")
    print("KEY: ", fmt_output(key))
    print("IV: ", fmt_output(cipher.iv))
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
    parser.add_argument(
        '-k', type=int, help='Key size. Can be 16, 24 or 32 bytes long (respectively for AES-128, AES-192 or AES-256).'
    )
    args = parser.parse_args()
    if args.f == None:
        parser.print_help()
        sys.exit()

    if args.k != 16 and args.k != 24 and args.k != 32:
        print("[!] Invalid or missing key size! Defaulting to 128")
        args.k = 16

    with open(args.f, mode='rb') as file:
        buf = file.read()
        file.close()
        ciphertext = encrypt(buf, args.k)
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
        