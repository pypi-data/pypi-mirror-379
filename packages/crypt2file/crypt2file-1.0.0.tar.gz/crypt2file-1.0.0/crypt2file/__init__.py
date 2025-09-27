import argparse
import os
from pathlib import Path
from cryptography.fernet import Fernet
import getpass

__title__ = 'crypt2file'
__license__ = 'MIT'
__author__ = 'Kyunghoon (aloecandy@gmail.com)'
__version__ = '1.0.0'

class Crypt:
    """
    Encrypts and decrypts data using a machine-specific key.

    The key is stored in the user's home directory (`~/.crypt2file/secret.key`).
    This means that files encrypted on one machine can only be decrypted on that same machine.
    To decrypt on another computer, you must manually copy the `secret.key` file.
    """
    def __init__(self, key_path=None):
        if key_path:
            self.key_path = Path(key_path)
        else:
            self.key_path = Path.home() / ".crypt2file" / "secret.key"

        self.key = self._load_or_generate_key()
        self.fernet = Fernet(self.key)

    def _load_or_generate_key(self):
        """Loads the key from the key path, or generates a new one if it doesn't exist."""
        try:
            key = self.key_path.read_bytes()
            # print(f"crypt2file: Loaded existing key from {self.key_path}")
        except FileNotFoundError:
            print(f"crypt2file: Key not found. Generating a new key...")
            self.key_path.parent.mkdir(parents=True, exist_ok=True)
            key = Fernet.generate_key()
            self.key_path.write_bytes(key)
            print(f"crypt2file: New key generated and saved to {self.key_path}")
            print("IMPORTANT: Back up this key file. If you lose it, you will not be able to decrypt your files.")
        return key

    def encrypt(self, data: bytes) -> bytes:
        """Encrypts bytes."""
        return self.fernet.encrypt(data)

    def decrypt(self, encrypted_data: bytes) -> bytes:
        """Decrypts bytes."""
        return self.fernet.decrypt(encrypted_data)

    def encrypt_to_file(self, message: str, file_path: str):
        """Encrypts a string and saves it to a file."""
        encrypted_data = self.encrypt(message.encode('utf-8'))
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        print(f"Message encrypted and saved to {file_path}")

    def decrypt_from_file(self, file_path: str) -> str:
        """Decrypts a file and returns the content as a string."""
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = self.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')

def main():
    """Command-line interface for crypt2file."""
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files using a machine-specific key.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encrypt command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a message and save to a file.")
    encrypt_parser.add_argument("file_path", help="The path to the output encrypted file.")
    encrypt_parser.add_argument("-m", "--message", help="The message string to encrypt. If not provided, input will be requested.")

    # Decrypt command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a file and print the message.")
    decrypt_parser.add_argument("file_path", help="The path to the encrypted file.")

    args = parser.parse_args()
    crypt = Crypt()

    if args.command == "encrypt":
        if args.message:
            message = args.message
        else:
            message = getpass.getpass("Enter message to encrypt: ")
        crypt.encrypt_to_file(message, args.file_path)
    elif args.command == "decrypt":
        try:
            message = crypt.decrypt_from_file(args.file_path)
            print("Decrypted message:")
            print(message)
        except Exception as e:
            print(f"Decryption failed: {e}")

if __name__ == "__main__":
    main()