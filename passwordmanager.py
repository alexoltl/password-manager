from colorama import Fore
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 


key = load_key()
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
