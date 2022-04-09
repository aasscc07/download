from Crypto.Cipher import AES 
import glob
import os
import math
import hashlib
import base64
import pickle


# try:
#     with open("test.jpg",'rb') as f:
#         print(f.read().decode('ascii'))
# except:
#     print("TEST\n\n")
#     with open("test.jpg",'rb') as f:
#         print(f.read())


# with open("test.txt",'wb') as f:
#     f.write("TEST".encode())

with open("test.txt",'wb') as f:
    f.write("TEST")