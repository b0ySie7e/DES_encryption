from base64 import b64decode, b64encode
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad, pad
import argparse

def encrypted_data(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
    encrypted_data = cipher.encrypt(padded_text)
    return b64encode(encrypted_data).decode('utf-8')

def decrypted_data(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decoded_data = b64decode(encrypted_text)
    decrypted_data = unpad(cipher.decrypt(decoded_data), DES.block_size)
    return decrypted_data.decode('utf-8')

def main():
    parser = argparse.ArgumentParser(
        prog='DES Encryption',
        description='This program encrypts and decrypts using DES.',
        epilog='Example usage:\npython3 des_encryption.py -e -k "YourKey" -s "YourPlainText"\n'
               'python3 des_encryption.py -d -k "YourKey" -s "YourEncryptedText"',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument('-e', '--encrypt', 
                        action='store_true',
                        help='Select this option to encrypt the provided string')
    
    parser.add_argument('-d', '--decrypt', 
                        action='store_true',
                        help='Select this option to decrypt the provided string')
    
    # Key
    parser.add_argument('-k', '--key',
                        required=True,
                        help='Specify the key for encryption or decryption')
    
    parser.add_argument('-s', '--str',
                        required=True,
                        help='Specify the string for encryption (plain text) or decryption (encrypted text)')
    
    args = parser.parse_args()

    if len(args.key) != 8:
        print('[+] Error: The key must be exactly 8 characters long.')
        return

    if args.encrypt:
        print("Encryption selected")
        encrypted_text = encrypted_data(args.str, args.key.encode('utf-8'))
        print(f'[+] Data encrypted: {encrypted_text}')
        
    elif args.decrypt:
        print("Decryption selected")
        decrypted_text = decrypted_data(args.str, args.key.encode('utf-8'))
        print(f'[+] Data decrypted: {decrypted_text}')  

    else:
        parser.print_help()
        print('[+] Error: You must specify either -e/--encrypt or -d/--decrypt')

if __name__ == "__main__":
    main()
