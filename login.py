from cryptography.fernet import Fernet
from getpass import getpass

key = Fernet.generate_key()
f = Fernet(key)

def crypt_username(username):
    encrypted_u = f.encrypt(username)
    return encrypted_u

def crypt_password(password):
    encrypted_p = f.encrypt(password)
    return encrypted_p

def decrypt_username(encrypted_u):
    decrypted_u = f.decrypt(encrypted_u)
    return decrypted_u

def decrypt_password(encrypted_p):
    decrypted_p = f.decrypt(encrypted_p)
    return decrypted_p


def change_u(encrypted_u):
    print("Choose new username.")
    username = input().encode()
    encrypted_u = f.encrypt(username)
    return encrypted_u
    

def change_p(encrypted_p):
    print("Choose new password.")
    password = input().encode()
    encrypted_p = f.encrypt(password)
    return encrypted_p


def menu():
    while True:
        
        user_choice = input("Do you want change username or password? (yes/no): ")
        if user_choice == "yes":
            loop = True
            while loop:
                user_choice = input("Choose number:\n1. Username \n2. Password\n")
                
                if user_choice == "1":
                    global encrypted_u
                    encrypted_u = change_u(encrypted_u)
                    print(f"Your new crypted username: {encrypted_u}")
                    loop = False
                    
                elif user_choice == "2":
                    global encrypted_p
                    encrypted_p = change_p(encrypted_p)
                    print(f"Your new crypted password: {encrypted_p}")
                    loop = False
                    
                else:
                    print("Error in input.")
        else:
            None
            
        user_choice = input("Do you want login again or kill program? (yes/no/kill): ")
        if user_choice == "yes":
            break
        elif user_choice == "kill":
            global main_loop
            main_loop =  False
            break
        else:
            None



username = "username".encode()
password = "password".encode()

encrypted_u = crypt_username(username)
encrypted_p = crypt_password(password)

main_loop = True

while main_loop:
    
    user_u = input("Username: ").encode()
    user_p = input("Password: ").encode()  #getpass


    decrypted_u = decrypt_username(encrypted_u)
    decrypted_p = decrypt_password(encrypted_p)

    print("Logging in...")

    if decrypted_u == user_u and decrypted_p == user_p:
        print("You are in!")
        menu()
    else:
        print("Something went wrong!")
    





    


