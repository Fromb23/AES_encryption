#!/usr/bin/python3

import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def encrypt_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            encrypt_file(os.path.join(root, filename))

def aes_encrypt(filepath):
    # Generate a 256-bit AES key
    key = get_random_bytes(32)

    # Generate a 128-bit IV (Initialization Vector)
    iv = get_random_bytes(16)

    # Create an AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the plaintext data from the file
    with open("filename.txt", "rb") as file:
        plaintext = file.read()

    # Pad the plaintext using the PKCS7 scheme
    padded_plaintext = pad(plaintext, AES.block_size)

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Store the encrypted data in a new file
    with open("encrypted_filename.txt", "wb") as file:
        file.write(ciphertext)

    # Store the key and IV in separate files (secure key management)
    with open("key.txt", "wb") as key_file:
        key_file.write(key)

    with open("iv.txt", "wb") as iv_file:
        iv_file.write(iv)

encrypt_files_in_directory(directory)
