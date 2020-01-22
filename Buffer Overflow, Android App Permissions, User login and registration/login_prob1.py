import re
import json
import ast
import sys
import bcrypt

with open("dictionary_passwords.txt") as f:
    content = f.readlines()
password_dictionary = {}
for word in content:
    password_dictionary[word.strip()]=1

# Check if password is strong or not
def is_strong_password(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    pat = re.compile(reg)
    mat = re.search(pat, password)
    pwd = re.sub(r'[^A-Za-z]', '', password).lower()
    if mat and pwd not in password_dictionary:
        return True
    else:
        return False

# Generate hash of given password for secure storage
def generate_hash(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


def check_if_password_exists(password,hashed_password_list):
    for hashed_password in hashed_password_list:
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
            return True
    return False

# If username doesn't exists, execute this function
def username_not_exists(ip):
    if not ip: print("Account with given username doesn't exist. Please create an account")
    flag_user_input = input("Enter: \n1. To Create an Account \n2. To Exit\n")
    if int(flag_user_input) == 1:
        create_account()
    elif int(flag_user_input) == 2:
        sys.exit(1)

def login():
    # If file doesn't exists, create one
    try:
        f = open("dict1.txt","r+")
        f.close()
    except:
        f = open("dict1.txt","w+")
        f.close()

    with open("dict1.txt","r+") as f:
        json_string = f.read()
        if json_string:
            credentials = ast.literal_eval(json_string)
            username = input ("Enter Username: ")
            if username not in credentials:
                username_not_exists(0)
                return
            password = input ("Enter password: ")
            if check_if_password_exists(password,credentials[username]):
                print("\nLogin Successful !!\n")
                sys.exit(0)
            else:
                print("Account doesn't exist with given credentials. Please create an other account or Please try with different password.")
                u_input = input("Enter: \n1. To Login with different password \n2. To create an Account \n3. To Exit \n")
                if int(u_input) == 1:
                    login()
                elif int(u_input) == 2:
                    create_account()
                elif int(u_input) == 3:
                    f.close()
                    sys.exit(1)
        else:
            print("\nNo username exists\n")
            username_not_exists(1)
            return
    f.close()

def check_if_password_exists_whole_db(password,credentials):
    for credential in credentials:
        while check_if_password_exists(password, credentials[credential]):
            return True
    return False

def create_account():
    username = input ("Enter Username: ")
    password = input ("Enter password: ")
    while (username.lower() == password.lower()):
        print("Username is very similar to Password. Please re-enter your password")
        password = input("Enter password: ")

    while(not is_strong_password(password)):
        print("Please make sure the password is minimum 8 digits and maximum 20 digits long, includes atleast 1 upper case, 1 lower case, 1 number and 1 special character OR your password is very weak\n")
        password = input("Enter password: ")
        while (username.lower() == password.lower()):
            print("Username is very similar to Password. Please re-enter your password")
            password = input("Enter password: ")

    # If file doesn't exists, create one
    try:
        f = open("dict1.txt","r+")
        f.close()
    except:
        f = open("dict1.txt","w+")
        f.close()

    with open("dict1.txt","r+") as f:
        json_string = f.read()
        if json_string:
            credentials = ast.literal_eval(json_string)
        else:
            credentials = {}

    f.close()

    if username not in credentials:
        credentials[username] = []

    while check_if_password_exists_whole_db(password, credentials):
        print("Password already exists. Please enter different password.")
        password = input ("Enter password: ")
        while(not is_strong_password(password)):
            print("Please make sure the password is minimum 8 digits and maximum 20 digits long, includes atleast 1 upper case, 1 lower case, 1 number and 1 special character OR your password is very weak\n")
            password = input ("Enter password: ")
            while (username.lower() == password.lower()):
                print("Username is very similar to Password. Please re-enter your password")
                password = input ("Enter password: ")


    hashed_password = generate_hash(password)
    credentials[username].append(hashed_password)

    print("\n Account Creation Successful !! \n")

    # json = json.dumps(credentials)
    f = open("dict1.txt","w+")
    f.write(str(credentials))
    f.close()



while(True):
    user_input = input("Please Enter: \n1. To create an Account \n2. To Login \n3. To Exit \n")
    if int(user_input)==1:
        create_account()
    elif int(user_input)==2:
        login()
    else:
        sys.exit(1)
