# DES_encryption
Script encrypts and decrypts using DES

```python

❯ python3 des_encryption.py --help
usage: DES Encryption [-h] [-e] [-d] -k KEY -s STR

This program encrypts and decrypts using DES.

options:
  -h, --help         show this help message and exit
  -e, --encrypt      Select this option to encrypt the provided string
  -d, --decrypt      Select this option to decrypt the provided string
  -k KEY, --key KEY  Specify the key for encryption or decryption
  -s STR, --str STR  Specify the string for encryption (plain text) or decryption (encrypted text)

Example usage:
python3 des_encryption.py -e -k "YourKey" -s "YourPlainText"
python3 des_encryption.py -d -k "YourKey" -s "YourEncryptedText"

```

## Encrypted

```python

❯ python3 des_encryption.py -e -k "YourKeyn" -s "YourPlainText"
Encryption selected
[+] Data encrypted: TQNOS3UIYqgy1AYtITacZA==

```

## Decrypted

```python

❯ python3 des_encryption.py -d -k "Captur3T" -s "k3FElEG9lnoWbOateGhj5pX6QsXRNJKh///8Jxi8KXW7iDpk2xRxhQ=="
Decryption selected
[+] Data decrypted: {This_Isn't_Where_I_Parked_My_Car}

```