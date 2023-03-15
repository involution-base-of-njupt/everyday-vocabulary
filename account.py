#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import csv
from hashlib import sha512

# 用户文件路径和编码
account_file = 'account.csv'
codec = 'utf-8'

# 用户名和用户类型
account_username = None
account_type = None

# 初始化，检查账户文件是否存在，不存在则创建并写入默认管理员账户
def init():
    if not os.path.isfile(account_file):
        try:
            f = open(account_file, 'w', newline='')
            writer = csv.writer(f)
            writer.writerow(['admin', encrypt('admin'), 'admin'])
            return True
        except PermissionError:
            print('You do not have access to the account file!')
            raise
        except:
            print('Error!')
            raise
        finally:
            f.close()
    else:
        if os.path.isdir(account_file):
            choice = input('The account file is a directory! Remove it? (Y/N)')
            if choice == ('y' or 'Y'):
                try:
                    os.remove(account_file)
                except:
                    print('Error!')
                    raise
                init()
            elif choice == ('n' or 'N'):
                exit()
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
        password = input('Please input your password: ')
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
        password = input('Please input your password: ')
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
    current_password = input('Please input your current password: ')
    while not check(account_username, current_password)[0]:
        current_password = input('The password is wrong, please input again: ')
    new_password = input('Please input your new password: ')
    try:
        f = open(account_file, 'r', newline='')
        reader = csv.reader(f)
        if reader == None:
            return False
        for row in reader:
            if row[0] == account_username:
                row[1] = encrypt(new_password)
                writer = csv.writer(f)
                writer.writerows(reader)
                print('Change password successfully!')
                return True
    except:
        print('Error when changing password!')
        return False
    finally:
        f.close()
    return False

# 检查密码是否正确以及用户权限
def check(username, password):
    try:
        f = open(account_file, 'r', encoding = codec)
        reader = csv.reader(f)
        for row in reader:
            if row[0] == username and row[1] == encrypt(password):
                return True, row[2]
        return False, None
    except:
        print('Error when checking account!')
        return False, None
    finally:
        f.close()

# 检查用户名是否存在
def exist(username):
    with open(account_file, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == username:
                return True
        return False

# 写入账户信息
def write_account(username, password, usertype):
    with open(account_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password, usertype])
        return True
