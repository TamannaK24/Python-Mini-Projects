from cryptography.fernet import Fernet 

# creates key 
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
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
        for line in f:
            data = line.rstrip()
            acc, pwd = data.split("|")
            decrypted_password = fer.decrypt(pwd.encode()).decode()
            print(f"Username: {account} | Password: {decrypted_password}")

def add(account, password):
    encrypted_password = fer.encrypt(password.encode()).decode()
    with open('passwords.txt', 'a') as f:
         f.write(f"{account}|{encrypted_password}\n")  

with open('passwords.txt', 'w') as f:
    pass

print("Hello, welcome to the password manager!")
# write_key()
while True:
    answer = input("Would you like to add (A), view (V), or quit(Q)? ").lower().strip()
    if answer == "a":
        account = input("Please enter an account name: ")
        password = input("Please enter a password: ")
        add(account, password)  
    elif answer == "v":
        view()
    elif answer == "q":
        quit()
    else:
        print("Please enter a valid input. ")