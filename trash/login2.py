from cryptography.fernet import Fernet
from getpass import getpass

key = Fernet.generate_key()
f = Fernet(key)


l_list = []
with open("login_data.txt", "r") as file:
    for item in file:
        l_list.append(item)

    l_list = [i.split('\n', 1)[0] for i in l_list]

true_username = l_list[-2].encode()
true_password = l_list[-1].encode()

encrypted_u = f.encrypt(true_username)
encrypted_p = f.encrypt(true_password)
space = "\n".encode()
        
with open("login_data.txt", "r+b") as file:
    file.write(encrypted_u)
    file.write(space)
    file.write(encrypted_p)



while True:
    user_username = input("Input username: ").encode()
    user_password = getpass("Input password: ").encode()


    decrypted_u = f.decrypt(encrypted_u)
    decrypted_p = f.decrypt(encrypted_p)
    
    if user_username == decrypted_u and decrypted_p == user_password:
        true_username = input("Success.\nChange username: ").encode()
        true_password = getpass("Change password: ").encode()

        encrypted_u = f.encrypt(true_username)
        encrypted_p = f.encrypt(true_password)

        open('login_data.txt', 'w').close()
            
        with open("login_data.txt", "r+b") as file:
            file.write(encrypted_u)
            file.write(space)
            file.write(encrypted_p)
        print("Yay")
        
    else:
        print("Error.\n Try again!")
