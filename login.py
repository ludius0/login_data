from cryptography.fernet import Fernet
from getpass import getpass
# Put this somewhere safe!

l_list = []
with open("login_data.txt", "r") as f:
    for item in f:
        l_list.append(item)

    l_list = [i.split('\n', 1)[0] for i in l_list]

true_username = l_list[0].encode()
true_password = l_list[1].encode()


key = Fernet.generate_key()
f = Fernet(key)
encrypted = f.encrypt(true_username)


print(encrypted)

decrypted = f.decrypt(encrypted)

print(decrypted)


username = input("Username: ").encode()

password = getpass("Password: ").encode()
