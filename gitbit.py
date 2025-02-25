import os
import sys
import time
from replit import db
import urllib.parse
import replit.database

global username
global password
global choice
global choice2

username = ''
password = ''

def choiceloop(username):
    catalog(username)
    choice2 = input()

    if choice2 == '1':
        os.system('clear')
        print('Transfer Money')
        receiver = input('Receiver: ')
        amount = int(input('Amount: '))
        print(transfer_money(username, receiver, amount))
        time.sleep(1)
        os.system('clear')
        choiceloop(username)
    elif choice2 == '2':
        os.system('clear')
        print('Delete Account')
        delete_choice = input('Are you sure you want to delete your account? (yes/no): ')
        if delete_choice.lower() == 'yes':
            print(delete_account(username))
        else:
            print("Account deletion cancelled.")
            time.sleep(1)
            os.system('clear')
    else:
        os.system('clear')
        print('Logout')
        print('Are you sure you want to logout? (Y/N)')
        logout_choice = input()
        if logout_choice == 'Y':
            logout()
            os.system('clear')
        elif logout_choice == 'N':
            print('Logout cancelled.')
            choiceloop(username)

def transfer_money(sender, receiver, amount):
    if sender in db and receiver in db:
        if db[sender]['money'] >= amount:
            db[sender]['money'] -= amount
            db[receiver]['money'] += amount
            return f"Successfully transferred {amount} from {sender} to {receiver}."
        else:
            return "Insufficient balance."
    else:
        return "Database not properly initialized or sender/receiver not found in the database"

def guestcatalog():
    print('Welcome to Replbit, the unofficial currency of replit')
    print('''
    1. Create an account
    2. Login''')

def create_account(new_username, password, money):
    db[new_username] = {"password": password, "money": money}
    return "Account created successfully."

def login():
    global username
    os.system('clear')
    print('LOGIN \n')
    print('Username: ')
    username = input()
    print('Password:')
    password = input()
    if username in db and password == db[username]["password"]:
        print('Valid Account Found')
        time.sleep(1)
        os.system('clear')
        print('Setting up')
        time.sleep(1)
        print("Login successful. Welcome Back!")
        time.sleep(1)
        os.system('clear')
    else:
        print('Invalid Account')
        login()

def logout():
    global username
    username = ''
    print('Logged out successfully.')
    time.sleep(1)

def delete_account(username):
    if username in db:
        del db[username]
        return f"Account for {username} has been successfully deleted."
    else:
        return "Account not found in the database. Cannot delete."

def catalog(username):
  if isinstance(username, bytes):
      username = username.decode('utf-8')
  if username in db:
      money = db[username]['money']
      print('------------\nWelcome,', username, '\nYour Balance is', money, '\n| Catalog |\n1. Transfer\n2. Delete Account\n3. Logout\n------------')
  else:
      print("User not found in the database. Cannot display catalog.")
    
def usernameexists():
  print('Username: ')
  username = input()
  if username in db:
      print('Username already taken, please try a different username')
      return usernameexists()
  else:
      return username

def loop():
    global username
    guestcatalog()
    choice = input()
    if choice == '1':
        os.system('clear')
        print('Create an account \n')
        username = usernameexists()
        time.sleep(1)
        password = input('Password: ')
        time.sleep(1)
        os.system('clear')
        print('Please Remember your username and password. You will need them to login.')
        time.sleep(1)
        os.system('clear')
        create_account(username, password, 100)
        choiceloop(username)
    elif choice == '2':
        login()
        choiceloop(username)

    loop()

loop()
