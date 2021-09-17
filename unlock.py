from cryptography.fernet import Fernet
from os import listdir
from os.path import isfile, join
import base64
import time

def decrypt(fn):
    with open("vault/"+fn, 'rb') as file:
        fi = file.read()

    decrypted = fernet.decrypt(fi)

    with open("vault/"+fn, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

print("Python Vault - Unlock Files")
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
    try:
        decrypt(i)
    except:
        print("password invalid")
        time.sleep(2)
        exit(0)
    print("decrypting file", itir, "of", len(onlyfiles))
    itir = itir + 1

print("")
print("done.")
time.sleep(2)
exit(0)
#TODO: turn into standalone executable