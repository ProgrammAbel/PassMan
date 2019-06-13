#!/usr/bin/env python3
"""
Generate/retrieve and manage passwords.

Usage:
    ./main.py
"""
import hashlib
from getpass import getpass
from base64 import a85encode


def genpasswd(website, masterpass):
    """
    Generate/retrieve a password using the website name and Master Passphrase.

    Args:
        website: The name of the website you want to sign up/log in to.
        masterpassword: Your Master Passphrase.

    Outputs:
        The password, generated from the website name and Master Passphrase.
    """
    website = website.encode()
    masterpass = masterpass.encode()
    salted = website + masterpass
    hash = hashlib.sha256(salted).digest()
    password = a85encode(hash).decode()

    print('This is your password: ', password)


def main():
    """
    Input the website name and Master Passphrase to generate/retrieve a password.
    """
    print('''Welcome to PassMan, a password manager written in Python!
Please type in the name of the website you want to sign up/log in to:''')
    website = input().encode()
    print('Now type in the Master Password:')
    masterpass = getpass('').encode()
    genpasswd(website, masterpass)


if __name__ == '__main__':
    main()
