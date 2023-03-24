#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 账户管理模块
# 命令行界面和图形化界面都需要用到

import os
import json
from hashlib import sha512

# 用户文件路径和编码
account_file = f"{os.path.abspath('.')}/data/account.json"
codec = 'utf-8'

# 用户名和用户类型
username = None
usertype = None

# TODO: 加密账户类型（需要换加密方式为对称加密方式）

# 密码 SHA512 加密
def encrypt(content):
    return sha512(content.encode(codec)).hexdigest()


# 初始化，检查账户文件是否存在，不存在则写入默认管理员账户，返回值为是否写入默认管理员账户
def init():
    if not os.path.isfile(account_file) or not os.path.getsize(account_file): # 账户文件对应的路径不是文件（是文件夹或者不存在）或文件为空
        if os.path.isdir(account_file): # 账户文件对应的路径是文件夹
            exit()
        else:
            # 创建data文件夹
            try:
                os.mkdir(os.path.dirname('data'))
            except FileExistsError:
                pass
            except Exception as e:
                exit(e)
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
            exit()
        finally:
            if f:
                f.close()


# 检查密码是否正确以及用户权限，传入用户名，可选传入加密后的密码，返回值：0.错误信息，1. 密码是否正确（如果没有传入则返回None），2.用户权限类型
def check(username, encrypted_password = ''):
    f = None
    try:
        f = open(account_file, 'r', encoding = codec)
        accounts = json.load(f)
        if encrypted_password: # 传入了加密后的密码，则检查
            if accounts[username]['password'] == encrypted_password: # 密码正确
                return None, True, accounts[username]['type']
            else: # 密码错误
                return None, False, None
        else: # 没传入加密后的密码，则不检查
            return None, None, accounts[username]['type']
    except Exception as e: # 发生错误
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
        return e, None
    finally:
        if f:
            f.close()


# 写入账户信息，传入用户名、加密后的密码、用户权限类型，返回错误信息
def write(username, encrypted_password, usertype = ''):
    if not username:
        return '用户名不能为空'
    f = None
    try:
        if not os.path.isfile(account_file) or not os.path.getsize(account_file):
            accounts = {}
        else:
            f = open(account_file, 'r', newline='', encoding=codec)
            accounts = json.load(f)
        accounts.setdefault(username, {})['password'] = encrypted_password
        if usertype:
            accounts.setdefault(username, {})['type'] = usertype
        f = open(account_file, 'w', newline='', encoding=codec)
        json.dump(accounts, f, ensure_ascii=False)
        return None
    except Exception as e:
        return e
    finally:
        if f:
            f.close()


# 删除账户，传入用户名，返回错误信息
def delete(username):
    f = None
    try:
        f = open(account_file, 'r', newline='', encoding=codec)
        accounts = json.load(f)
        if username in accounts:
            del accounts[username]
            f = open(account_file, 'w', newline='', encoding=codec)
            json.dump(accounts, f, ensure_ascii=False)
            return None
        else:
            return None
    except Exception as e:
        return e
    finally:
        if f:
            f.close()


# 读取所有账户信息，返回值：0.错误信息，1.账户信息字典（用户名为键，用户类型为值）
def read_all():
    f = None
    try:
        f = open(account_file, 'r', newline='', encoding=codec)
        accounts = json.load(f)
        result = {}
        for username in accounts:
            result[username] = accounts[username]['type']
        return None, result
    except Exception as e:
        return e, None
    finally:
        if f:
            f.close()