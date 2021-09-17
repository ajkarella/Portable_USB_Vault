from cryptography.fernet import Fernet
from os import listdir
from os.path import isfile, join
import base64
import time

def encrypt(fn):
    with open("vault/"+fn, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("vault/"+fn, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

print("Python Vault - Lock Files")
print("")
key = input("Enter Password: ")
pad = 32 - len(key)
padding = "="*pad
key = key + padding

asciiStr = key.encode("ascii")
base64_bytes = base64.b64encode(asciiStr)
key = base64_bytes.decode("ascii")


fernet = Fernet(key)

onlyfiles = [f for f in listdir("vault") if isfile(join("vault", f))]

itir = 1
print("")
for i in onlyfiles:
    print("encrypting file", itir,"of",len(onlyfiles))
    encrypt(i)
    itir = itir + 1

print("")
print("done.")
time.sleep(2)
exit(0)