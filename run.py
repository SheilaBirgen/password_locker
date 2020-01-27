#!/usr/bin/env python3.6
from user import User, Credential
from random import random
import string
import getpass

def create_user(name, user_password):
    """
    Parameters
    """
    new_user = User(name, user_password)
    return new_user

def generate_password(user):
    """
    function to generate random password for user
    """
    return user.generate_random_password()

def save_user(user):
    """
    Function to save user
    """
    user.save_user()


def delete_user(user):
    """
    Function to delete user
    """
    user.delete_user()


def create_credential(account, account_username, account_password):
    """
  function create new credential
    """
    new_credential = create_credential(account, account_username, account_password)
    return new_credential


def save_credential(credential):
    """
    Function to save user
    """
    credential.save_credential()


def delete_credential(credential):
    """
    Function to delete credential
    """
    credential.delete_credential()

def find_credential(account_username):
    """
    Function to find credential
    """
    return Credential.find_credential_by_account_username(account_username)


def check_existing_credentials(account_username):
    """
    Function to check existing credential
    """
    return Credential.find_credential_by_account_username(account_username)


def display_credential():
    """
    Function to display credential
    """
    return Credential.display_credential()

def main():
    # keyboard = Controller()
    # time.sleep(2)
    print("Hello, WELCOME to THE PASSWORD LOCKER. What is your name, please :) ?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do today?")
    print('\n')

    while True:
        print(
            '''
                            USE THE SHORT CODES
                    1. cc - to create a new credential
                    2. dc - to display credential
                    3. fc - to find credential
                    4. dc - to delete credential
                    5. gp - to generate a random password
                    6. ex- to exit 
            ''')

        short_code = input("Use short-codes to navigate > ").lower()

        if short_code == 'cc':
            print(" Create account")
            print("-" * 10)

            print("Account ....")
            account = input("> ")

            print("username ....")
            account_username = input("> ")

            print("Enter Password")
            account_password = input("> ")

            save_credential(create_credential( account, account_username, account_password ))

            print("\n")
            print(f"New Credential{account} {account_username} {account_password} has been created")
            print("\n")

        elif short_code == "gp":
            print(
                "Please enter the account you want to generate password for > ")
            social_media = input("Enter account type > ")

            def random_password(length=8, uppercase=True, lowercase=True, numbers=True):
                """
                Random password generation
                """
                character_set = ''
                if uppercase: character_set += string.ascii_uppercase
                if numbers: character_set += string.digits
                if lowercase: character_set += string.ascii_lowercase

                character_set = string.ascii_letters + string.digits
                return "".join(random.choice(character_set) for i in range(length))

            print(
               f"Your random password for {social_media} is: ", random_password(8))

        elif short_code == "dc":

            if display_credential():
                print("Here is a list of all your Credential and passwords")
                print("\n")
                for credential in display_credential():
                    print(f"{credential.account} {credential.account_username}{account_password}")
                    print("\n")
            else:
                print("\n")
                print(
                    "You don't have any saved credentials yet. Try saving one")
                print("\n")

        elif short_code == 'fc':

            print("Enter the account username you want to search for")

            search_account_username = input()
            if check_existing_credentials(search_account_username):
                search_credential = find_credential(search_account_username)
                print(f"{search_credential.account} {search_credential.account_username}")
                print('-' * 20)

                print(f"Account password.......{search_credential.account_password}")

            else:
                print("That credential does not exist")

        elif short_code == "dl":
            print("Enter the account username of the credential you would like to delete.")
            my_delete = input("> ")
            my_del = find_credential(my_delete)
            Credential.credential_list.remove(my_del)
            print(
                f"Credential with  account username {my_delete} has been removed succefully")
        elif short_code == "ex":
            print("Logged out")
            break

        elif short_code == "ex":
            print(f"Thanks for visiting us. Have a great day {user_name}")
            break

if __name__ == '__main__':
    main()
