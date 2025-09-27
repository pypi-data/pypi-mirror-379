# crypt2file

**Version: 1.0.0**

A simple tool to encrypt and decrypt files. It uses a single, machine-specific key, meaning files encrypted on one computer can only be decrypted on that same computer.

## How It Works

`crypt2file` is designed for simple, machine-locked encryption. When you first use it, it generates a unique encryption key and stores it in your user home directory (`~/.crypt2file/secret.key`).

- **Machine-Specific Key**: Because the key is stored locally on your machine, any file you encrypt will only be decryptable on that machine. This is useful for storing sensitive information (like passwords or notes) in a file that is useless if copied to another computer.

- **Portability**: If you want to decrypt a file on a different computer, you must manually copy the `secret.key` file from the original machine to the same location (`~/.crypt2file/secret.key`) on the new machine.

**IMPORTANT**: The `secret.key` file is critical. If you lose this file (e.g., by reinstalling your OS), you will permanently lose the ability to decrypt any files you encrypted with it. **Please back up your `secret.key` file to a safe location.**

## Installation

```shell
pip install --upgrade .
```

## Usage

### As a Python Library

You can also use `crypt2file` in your Python code. A common use case is to load a password from a file, or create it if it doesn't exist.

```python
from crypt2file import Crypt
import getpass

crypt = Crypt()
file_path = "my_password.dat"

try:
    # Try to load the password from the file
    password = crypt.decrypt_from_file(file_path)
    print("Password loaded successfully.")
except Exception:
    # If it fails (e.g., file not found), prompt the user for a new one
    print(f"Could not load password from {file_path}. Creating a new one.")
    new_password = getpass.getpass("Enter a new password to save: ")
    crypt.encrypt_to_file(new_password, file_path)
    password = new_password
    print(f"New password saved to {file_path}.")

# Now you can use the 'password' variable in your application
print(f"The loaded/created password is: {password}")
```

### As a Command-Line Tool (CLI)

The easiest way to use `crypt2file` is from your terminal.

**Encrypt a message to a file:**

```shell
crypt2file encrypt my_secret_file.dat
```
> Enter message to encrypt: `********`
> Message encrypted and saved to my_secret_file.dat

Or provide the message directly:
```shell
crypt2file encrypt my_secret_file.dat -m "This is my secret message"
```
> Message encrypted and saved to my_secret_file.dat

**Decrypt a file:**

```shell
crypt2file decrypt my_secret_file.dat
```
> Decrypted message:
> This is my secret message

## License

This project is licensed under the MIT License.