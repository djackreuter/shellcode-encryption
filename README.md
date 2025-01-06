# shellcode-encryption

Python scripts to encrypt shellcode and obfuscate strings.

## AES
```
python.exe .\aes.py
usage: aes.py [-h] [-f F] [--raw | --no-raw] [-k K]

options:
  -h, --help       show this help message and exit
  -f F             bin file to encrypt
  --raw, --no-raw  Data will be saved as raw binary file.
  -k K             Key size. Can be 16, 24 or 32 bytes long (respectively for AES-128, AES-192 or AES-256).
```

## RC4
```
python.exe .\rc4.py
usage: aes.py [-h] [-f F] [--raw | --no-raw]

options:
  -h, --help       show this help message and exit
  -f F             bin file to encrypt
  --raw, --no-raw  Data will be saved as raw binary file.
```

## XOR
```
python.exe .\xor.py
usage: xor.py [-h] [-k K] [-f F] [-s S] [-w W]

options:
  -h, --help  show this help message and exit
  -k K        XOR key. Will create random 8 character key if ommited
  -f F        bin file containing payload
  -s S        String to XOR
  -w W        File to write encrypted binary payload to
```

## Better XOR - Skips null bytes to prevent leaking key. Prints array of indices to use on the decryption side.
```
python.exe .\better_xor.py
usage: xor.py [-h] [-k K] [-f F] [-s S] [-w W]

options:
  -h, --help  show this help message and exit
  -k K        XOR key. Will create random 8 character key if ommited
  -f F        bin file containing payload
  -s S        String to XOR
  -w W        File to write encrypted binary payload to
```

## Generate Stack String
```
usage: gen_stack_string.py [-h] [-s S]

options:
  -h, --help  show this help message and exit
  -s S        Input string
  ```
