from cryptography import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    command = input(
        "Would you like to add a new password. Press q to quit?")
    if command == "q":
        break
    elif command == "add":
        add()
    else:
        print("Invalid command.")
        continue