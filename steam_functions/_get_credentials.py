import os

def get_login():
    return os.environ['STEAMLOGIN']

def get_password():
    return os.environ['STEAMPASSWORD']

