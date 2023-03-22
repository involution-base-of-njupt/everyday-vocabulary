#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 账户管理模块
# 命令行界面和图形化界面都需要用到
# 前4个函数为命令行交互模式下的函数，后4个函数都需要用到

import os
import json
import maskpass
from hashlib import sha512
from colorama import Fore

# 用户文件路径和编码
account_file = 'account.json'
codec = 'utf-8'

# 用户名和用户类型
account_username = None
account_type = None

# TODO: 加密账户类型（需要换加密方式为对称加密方式）

# （命令行交互模式）初始化，检查账户文件是否存在，不存在则写入默认管理员账户，返回值为是否写入默认管理员账户
def init():
    if not os.path.isfile(account_file) or not os.path.getsize(account_file): # 账户文件对应的路径不是文件（是文件夹或者不存在）或文件为空
        if os.path.isdir(account_file): # 账户文件对应的路径是文件夹
            print(Fore.RED, '账户文件路径错误！', Fore.RESET)
            exit()
        write('admin', encrypt('admin'), 'admin')
        return True
    else: # 账户文件对应的路径是文件
        f = None
        try:
            f = open(account_file, 'r', newline='', encoding=codec)
            accounts = json.load(f)
            if accounts.keys() == []: # 账户文件为空
                write('admin', encrypt('admin'), 'admin')
                return True
            else:
                return False
        except Exception as e:
            print(Fore.RED, '读取账户时发生错误：', e, Fore.RESET)
            exit()
        finally:
            if f:
                f.close()


# （命令行交互模式）用户注册
def register():
    username = input('请输入用户名：')
    if exist(username)[1]:
        print(Fore.RED, '此用户名已被注册！', Fore.RESET)
        register()
    else:
        password = maskpass.askpass('请输入密码：')
        encrypt_pwd = encrypt(password)
        result = write(username, encrypt_pwd, 'user')
        if result == None: # 注册成功
            global account_username, account_type
            account_username = username
            account_type = 'user'
        else: # 发生错误
            return

# （命令行交互模式）用户登录
def login():
    global account_type, account_username
    username = input('请输入用户名：')
    if not exist(username)[1]:
        print(Fore.RED, '此用户名不存在！', Fore.RESET)
        login()
    else:
        password = maskpass.askpass('请输入密码：')
        check_result = check(username, encrypt(password))
        while True:
            if check_result[0]: # 发生错误
                password = maskpass.askpass('请重新输入密码：')
                check_result = check(username, encrypt(password))
            elif check_result[1] == False: # 密码错误
                print(Fore.RED, '密码错误，请重新输入密码：', Fore.RESET, end='')
                password = maskpass.askpass('')
                check_result = check(username, encrypt(password))
            else: # 没出错并且密码正确
                break
        account_username = username
        account_type = check_result[2]

# （命令行交互模式）修改密码
def change_password():
    current_password = maskpass.askpass('请输入当前密码：')
    check_result = check(account_username, encrypt(current_password))
    while True:
        if check_result[0]: # 发生错误
            current_password = maskpass.askpass('请重新输入密码：')
            check_result = check(account_username, encrypt(current_password))
        elif check_result[1] == False: # 密码错误
            print(Fore.RED, '密码错误，请重新输入密码：', Fore.RESET, end='')
            current_password = maskpass.askpass('')
            check_result = check(account_username, encrypt(current_password))
        else: # 没出错并且密码正确
            break
    new_password = maskpass.askpass('请输入新密码：')
    write(account_username, encrypt(new_password), account_type)
    print(Fore.GREEN, '密码修改成功！', Fore.RESET)
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
        print(Fore.RED, '验证账户时出现问题：', e, Fore.RESET)
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
        print(Fore.RED, '检查账户时出现问题：', e, Fore.RESET)
        return e, None
    finally:
        if f:
            f.close()

# 写入账户信息，传入用户名、加密后的密码、用户权限类型，返回错误信息
def write(username, encrypted_password, usertype):
    f = None
    try:
        if not os.path.isfile(account_file) or not os.path.getsize(account_file):
            accounts = {}
        else:
            f = open(account_file, 'r', newline='', encoding=codec)
            accounts = json.load(f)
        accounts.setdefault(username, {})['password'] = encrypted_password
        accounts.setdefault(username, {})['type'] = usertype
        f = open(account_file, 'w', newline='', encoding=codec)
        json.dump(accounts, f, ensure_ascii=False)
        return None
    except Exception as e:
        print(Fore.RED, '写入账户时出现问题：', e, Fore.RESET)
        return e
    finally:
        if f:
            f.close()