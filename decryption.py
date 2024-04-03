#!/usr/bin/python3

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_decryption():
    with open("encrypted_filename.txt", "rb") as file:
        ciphertext = file.read()

    # Retrieve the key and IV from their respective files
    with open("key.txt", "rb") as key_file:
        key = key_file.read()

    with open("iv.txt", "rb") as iv_file:
        iv = iv_file.read()

    # Create an AES cipher object with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data
    decrypted_data = cipher.decrypt(ciphertext)

    # Upad the Decrypted data
    decrypted_data = unpad(decrypted_data, AES.block_size)

    # Write the decrypted data into a file
    with open("decrypted.txt", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("Bingo!!! All files restored...")

aes_decryption()
