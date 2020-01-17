from cryptography.fernet import Fernet
from getpass import getpass

key = Fernet.generate_key()
fk = Fernet(key)

def encrypt(true_username, true_password):
    encrypted_u = fk.encrypt(true_username)
    encrypted_p = fk.encrypt(true_password)
    return encrypted_u, encrypted_p
    

l_list = []
with open("login_data.txt", "r+") as f:
    for item in f:
        l_list.append(item)

    l_list = [i.split('\n', 1)[0] for i in l_list]

    true_username = l_list[0].encode()
    true_password = l_list[1].encode()

    encrypt(true_username, true_password)
    overwrite()

"""    
def overwriting():
    with open(filename, 'r+') as f:
        text = re.sub('foobar', 'bar', l_list)
        f.seek(0)
        f.write(text)
        f.truncate()
"""    


while True:
    user_username = input("Input username: ").encode()
    user_password = input("Input password: ").encode()


    decrypted_u = fk.decrypt(l_list[0])
    decrypted_p = fk.decrypt(l_list[1])
    
    if user_username == decrypted_u and decrypted_p == user_password:
        true_username = input("Change username: ").encode()
        true_password = input("Change password: ").encode()

        encrypt(true_username, true_password)
        print("Yay")
        
    else:
        print("Error.\n Try again!")



#decrypted = f.decrypt(encrypted_u)
