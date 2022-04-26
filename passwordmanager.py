import base64
import os
import os.path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from colorama import Fore

mpass = input("What is the master password? (this will be use to encrypt and decrypt other passwords, do not lose it):").encode()

def make_salt():
    salt_exists = os.path.exists("salt.key")
    while salt_exists:
        break
    else:
        salt = os.urandom(16)
        with open("salt.key", "wb") as key_file:
            key_file.write(salt)
make_salt()



def load_salt():
    file = open("salt.key", "rb")
    salt = file.read()
    file.close()
    return salt 


salt = load_salt()
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)
key = base64.urlsafe_b64encode(kdf.derive(mpass))
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"{Fore.MAGENTA}User: {user}\nPassword: {fer.decrypt(passw.encode()).decode()}{Fore.RESET}")


def add():
    name = input(f"{Fore.GREEN}Enter a service or website name: {Fore.RESET}")
    pwd = input(f"{Fore.GREEN}Enter a password for that service or website: {Fore.RESET}")

    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")

while True:
    main = input(f"{Fore.BLUE}\nDo you want to view or add passwords?{Fore.GREEN}\n\n1. View\n\n2. Add\n\n3. Quit\n\n{Fore.RESET}>>> ")
    if main == "1":
        view()
    if main == "2":
        add()
    if main == "3":
        exit()