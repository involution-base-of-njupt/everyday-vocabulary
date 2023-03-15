#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import json
import maskpass
from hashlib import sha512

# 用户文件路径和编码
account_file = 'account.json'
codec = 'utf-8'

# 用户名和用户类型
account_username = None
account_type = None

# TODO: 加密账户类型

# 初始化，检查账户文件是否存在，不存在则创建并写入默认管理员账户
def init():
    if not os.path.isfile(account_file) or not os.path.getsize(account_file):
        write_account('admin', encrypt('admin'), 'admin')
        return True
    else:
        if os.path.isdir(account_file):
            choice = input('The account file is a directory! Remove it? (Y/N)')
            if choice == ('y' or 'Y'):
                try:
                    os.remove(account_file)
                except Exception as e:
                    print('Error when removing the directory: ' + e)
                init()
            elif choice == ('n' or 'N'):
                exit()
        else:
            try:
                f = open(account_file, 'r', newline='', encoding=codec)
                accounts = json.load(f)
                if accounts == None:
                    print('Error when reading the account file!')
                else:
                    return True
            except Exception as e:
                print('Error when opening the account file: ', e)
            finally:
                f.close()
        return False

# 密码 SHA512 加密
def encrypt(password):
    return sha512(password.encode(codec)).hexdigest()

# 用户注册
def register():
    username = input('Please input your username: ')
    if exist(username):
        print('This username already exists!')
        return
    else:
        password = maskpass.askpass('Please input your password: ')
        encrypt_pwd = encrypt(password)
        write_account(username, encrypt_pwd, 'user')
        global account_username, account_type
        account_username = username
        account_type = 'user'
        print('Register successfully, logged in!')

# 用户登录
def login():
    global account_type, account_username
    username = input('Please input your username: ')
    if not exist(username):
        print('The username does not exist!')
        return
    else:
        password = maskpass.askpass('Please input your password: ')
        check_result = check(username, password)
        if check_result[0]:
            account_username = username
            account_type = check_result[1]
            print('Login successfully!')
        else:
            print('The password is wrong or error!')

# 修改密码
def change_password():
    global account_username
    current_password = maskpass.askpass('Please input your current password: ')
    while not check(account_username, current_password)[1]:
        current_password = maskpass.askpass('The password is wrong, please input again: ')
    new_password = maskpass.askpass('Please input your new password: ')
    write_account(account_username, encrypt(new_password), account_type)
    return False

# 检查密码是否正确以及用户权限
def check(username, password):
    try:
        f = open(account_file, 'r', encoding = codec)
        accounts = json.load(f)
        if accounts[username]['password'] == encrypt(password):
            return True, accounts[username]['type']
        return False, None
    except Exception as e:
        print('Error when checking account: ', e)
        return False, None
    finally:
        f.close()

# 检查用户名是否存在
def exist(username):
    try:
        f = open(account_file, 'r', newline='', encoding=codec)
        accounts = json.load(f)
        if username in accounts:
            return True
        else:
            return False
    except Exception as e:
        print('Error when checking account, ', e)
        return False
    finally:
        f.close()

# 写入账户信息
def write_account(username, encrypted_password, usertype):
    try:
        f = open(account_file, 'r+', newline='', encoding=codec)
        if not os.path.getsize(account_file):
            accounts = {}
        else:
            accounts = json.load(f)
        accounts.setdefault(username, {})['password'] = encrypted_password
        accounts.setdefault(username, {})['type'] = usertype
        json.dump(accounts, f)
        return True
    except Exception as e:
        print('Error when writing account: ', e)
        raise
        return False
    finally:
        f.close()