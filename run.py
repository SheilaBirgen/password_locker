#!/usr/bin/env python3.6
from user import User, Credential
import random
import string
import getpass

def create_user(name, user_password):
    """
    Parameters
    ----------
    name
    user_password
    Returns
    -------
    """
    new_user = User(name, user_password)
    return new_user

def generate_password(user):
    """
    function to generate random password for user
    ----------
    user
    Returns
    -------
    """
    return user.generate_random_password()

def save_user(user):
    """
    Function to save user
    ----------
    user
    """
    user.save_user()


def delete_user(user):
    """
    Function to delete user
    ----------
    user
    """
    user.delete_user()


def create_credential(username,account, account_username, account_password):
    """
  function create new credential
    """
    new_credential = Credential(username,account, account_username, account_password)
    return new_credential


def save_credential(credential):
    """
    Function to save user
    ----------
    user
    """
    credential.save_credential()


def delete_credential(credential):
    """
    Function to delete credential
    ----------
    credential
    """
    credential.delete_credential()

def find_credential(account_username):
    """
    Function to find credential
    ----------
    name
    Returns
    -------
    """
    return Credential.find_by_account_username(account_username)


def check_existing_credentials(account_username):
    """
    Function to check existing credential
    ----------
    name
    Returns
    -------
    user
    """
    return Credential.find_by_account_username(account_username)


def display_credentials():
    """
    Function to display credential
    Returns
    -------
    """
    return Credential.display_all_credentials()
