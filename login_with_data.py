from cryptography.fernet import Fernet
from getpass import getpass

l_list = []
with open("login_data.txt", "r") as f:
    for item in f:
        l_list.append(item)

    l_list = [i.split('\n', 1)[0] for i in l_list]

    true_username = l_list[0].encode()
    true_password = l_list[1].encode()

    key = Fernet.generate_key()
    f = Fernet(key)


    encrypted_u = f.encrypt(true_username)
    encrypted_p = f.encrypt(true_password)
    
    l_list[0] = encrypted_u
    l_list[1] = encrypted_p




with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('lol', 'olo', text)
    f.seek(0)
    f.write(text)
    f.truncate()




print(encrypted_u)

decrypted = f.decrypt(encrypted_u)

print(decrypted)


username = input("Username: ").encode()

password = getpass("Password: ").encode()
