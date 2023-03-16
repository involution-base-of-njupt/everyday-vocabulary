#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 账户管理模块
# 命令行界面和图形化界面都需要用到
# 前4个函数为命令行交互模式下的函数，后4个函数都需要用到

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

# TODO: 加密账户类型（需要换加密方式为对称加密方式）

# （命令行交互模式）初始化，检查账户文件是否存在，不存在则写入默认管理员账户，返回值为是否成功
def init():
    if not os.path.isfile(account_file) or not os.path.getsize(account_file): # 账户文件对应的路径不是文件（是文件夹或者不存在）或文件为空
        if os.path.isdir(account_file): # 账户文件对应的路径是文件夹
            choice = input('The account file is a directory! Remove it (Y/N)? ')
            if choice == 'y' or choice == 'Y':
                try:
                    os.remove(account_file)
                except Exception as e:
                    print('Error when removing the directory: ', e)
                init()
            elif choice == 'n' or choice == 'N':
                exit()
        write('admin', encrypt('admin'), 'admin')
        return True
    else: # 账户文件对应的路径是文件
        f = None
        try:
            f = open(account_file, 'r', newline='', encoding=codec)
            accounts = json.load(f)
            if accounts == None:
                print('Error when reading the account file!')
                return False
            else:
                return False
        except Exception as e:
            print('Error when opening the account file: ', e)
            exit()
        finally:
            if f:
                f.close()
            

# （命令行交互模式）用户注册
def register():
    username = input('Please input your username: ')
    if exist(username)[1]:
        print('This username already exists!')
        register()
    else:
        password = maskpass.askpass('Please input your password: ')
        encrypt_pwd = encrypt(password)
        result = write(username, encrypt_pwd, 'user')
        if result == None: # 注册成功
            global account_username, account_type
            account_username = username
            account_type = 'user'
            print('Register successfully, logged in!')
        else: # 发生错误
            print('Error occured when writing account: ', result)
            register()

# （命令行交互模式）用户登录
def login():
    global account_type, account_username
    username = input('Please input your username: ')
    if not exist(username)[1]:
        print('The username does not exist!')
        login()
    else:
        password = maskpass.askpass('Please input your password: ')
        check_result = check(username, encrypt(password))
        while True:
            if check_result[0]: # 发生错误
                print('Error occured when checking account: ', check_result[0])
                password = maskpass.askpass('Please input password again: ')
                check_result = check(username, encrypt(password))
            elif check_result[1] == False: # 密码错误
                password = maskpass.askpass('The password is wrong, please input again: ')
                check_result = check(username, encrypt(password))
            else: # 没出错并且密码正确
                break
        account_username = username
        account_type = check_result[2]
        print('Login successfully!')

# （命令行交互模式）修改密码
def change_password():
    global account_username
    current_password = maskpass.askpass('Please input your current password: ')
    while not check(account_username, encrypt(current_password))[1]:
        current_password = maskpass.askpass('The password is wrong, please input again: ')
    new_password = maskpass.askpass('Please input your new password: ')
    write(account_username, encrypt(new_password), account_type)
    return False

# 密码 SHA512 加密
def encrypt(password):
    return sha512(password.encode(codec)).hexdigest()

# 检查密码是否正确以及用户权限，传入用户名和加密后的密码，返回值：0.错误信息，1. 密码是否正确，2.用户权限类型
def check(username, encrypted_password):
    f = None
    try:
        f = open(account_file, 'r', encoding = codec)
        accounts = json.load(f)
        if accounts[username]['password'] == encrypted_password: # 密码正确
            return None, True, accounts[username]['type']
        else: # 密码错误
            return None, False, None
    except Exception as e: # 发生错误
        print('Error when checking account: ', e)
        return e, None, None
    finally:
        if f:
            f.close()

# 检查用户名是否存在，传入用户名，返回错误信息和结果
def exist(username):
    f = None
    try:
        f = open(account_file, 'r', newline='', encoding=codec)
        accounts = json.load(f)
        if username in accounts:
            return None, True
        else:
            return None, False
    except Exception as e:
        print('Error when checking account, ', e)
        return e, None
    finally:
        if f:
            f.close()

# 写入账户信息，传入用户名、加密后的密码、用户权限类型，返回错误信息
def write(username, encrypted_password, usertype):
    fr = None
    fw = None
    try:
        if not os.path.isfile(account_file) or not os.path.getsize(account_file):
            accounts = {}
        else:
            fr = open(account_file, 'r', newline='', encoding=codec)
            accounts = json.load(fr)
        accounts.setdefault(username, {})['password'] = encrypted_password
        accounts.setdefault(username, {})['type'] = usertype
        fw = open(account_file, 'w', newline='', encoding=codec)
        json.dump(accounts, fw, ensure_ascii=False)
        return None
    except Exception as e:
        print('Error when writing account: ', e)
        return e
    finally:
        if fr:
            fr.close()
        if fw:
            fw.close()