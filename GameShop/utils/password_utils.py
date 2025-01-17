import os
import hashlib

SALT_LEN = 32

def hash_password(password:str, hashed_pwd:bytes = None):
    if hashed_pwd:
        salt = hashed_pwd[:SALT_LEN]
        return salt + hashlib.pbkdf2_hmac('sha256', password. encode('utf-8'), salt, 100000) == hashed_pwd
    else:
        salt = os.urandom(SALT_LEN)
        return salt + hashlib.pbkdf2_hmac('sha256', password. encode('utf-8'), salt, 100000)

if __name__ == '__main__':
    pwd = '123456'
    hashed = hash_password(password=pwd)
    print(hashed)

    if hash_password('123456', hashed) == True:
        print('Ура!')
    else:
        print('Блин!...')