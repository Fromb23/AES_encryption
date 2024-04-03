# AES Encryption Algorithm Documentation

## Introduction
The AES (Advanced Encryption Standard) Encryption Algorithm is a symmetric encryption algorithm widely used for securing sensitive data. This documentation outlines the implementation of an AES-based file encryption system. The program encrypts files within the current directory and all its subdirectories, providing a secure means of protecting data.

## Features
- Encrypts files using AES encryption algorithm.
- Works on Kali Linux and can be configured for other OS versions.
- Supports file encryption for the current directory and all subdirectories.
- Provides decryption functionality for encrypted files.

## Installation
1. Clone the repository from [GitHub](https://github.com/Fromb23/AES_encryption).
2. Ensure that Python 3.x is installed on your system.
3. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage
### Encrypting Files
To encrypt files within the current directory and its subdirectories, follow these steps:
1. Open a terminal window.
2. Navigate to the directory containing the program files.
3. Run the encryption script using the command:
4. Follow the prompts to enter the encryption key and choose encryption options.

### Decrypting Files
To decrypt encrypted files, follow these steps:
1. Open a terminal window.
2. Navigate to the directory containing the program files.
3. Run the decryption script using the command:
4. Follow the prompts to enter the decryption key and choose decryption options.

## Configuration
The program is designed to work on Kali Linux by default. However, it can be configured to work with other OS versions by modifying the system-specific parameters in the source code.

## Testing
The AES Encryption Algorithm program has been thoroughly tested on Kali Linux to ensure its functionality and security. However, it is recommended to conduct additional testing on other OS versions before deployment in production environments.

## Security Considerations
- Always use strong encryption keys to maximize security.
- Securely store encryption keys and do not share them with unauthorized users.
- Regularly update the program to address any security vulnerabilities or bugs.

## Disclaimer
This program is provided for educational and informational purposes only. Use it responsibly and ethically, and ensure compliance with applicable laws and regulations regarding data encryption and privacy.
