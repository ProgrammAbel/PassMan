import hashlib
from base64 import a85encode

print('''Welcome to PyPass, a password manager written in Python!
Please type in the name of the website you want to sign up/log in to:''')
website = input().encode()
print('Now type in the Master Password:')
masterpass = input().encode()

salted = website + masterpass
hash = hashlib.sha256(salted).digest()
password = a85encode(hash).decode()

print('This is your password: ', password)
