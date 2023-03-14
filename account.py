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
        with open(account_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['admin', encrypt('admin'), 'admin'])
            return True
    else:
        return False

# 密码 SHA512 加密
def encrypt(password):
    sha512().update(password.encode(codec))
    return sha512().hexdigest()

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
    username = input('Please input your username: ')
    if not exist(username):
        print('The username does not exist!')
        return
    else:
        password = input('Please input your password: ')
        encrypt_str = encrypt(password)
        if check(username, encrypt_str):
            account = username
            print('Login successfully!')
        else:
            print('The password is wrong!')

# 修改密码
def change_password(username, new_password):
    with open(account_file, 'r', newline='') as f:
        reader = csv.reader(f)
        if reader == None:
            return False
        for row in reader:
            if row[0] == username:
                row[1] = encrypt(new_password)
                writer = csv.writer(f)
                writer.writerows(reader)
                return True
    return False

# 检查密码是否正确
def check(username, password):
    with open(account_file, encoding = codec) as f:
        reader = csv.reader(f)
        if reader == None:
            return False
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
        return False

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
