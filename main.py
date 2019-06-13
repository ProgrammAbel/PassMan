#!/usr/bin/env python3
import hashlib
from getpass import getpass
from base64 import a85encode


def genpasswd(website, masterpass):
    website = website.encode()
    masterpass = masterpass.encode()
    salted = website + masterpass
    hash = hashlib.sha256(salted).digest()
    password = a85encode(hash).decode()

    print('This is your password: ', password)


def main():
    print('''Welcome to PassMan, a password manager written in Python!
Please type in the name of the website you want to sign up/log in to:''')
    website = input().encode()
    print('Now type in the Master Password:')
    masterpass = getpass('').encode()
    genpasswd(website, masterpass)


if __name__ == '__main__':
    main()
