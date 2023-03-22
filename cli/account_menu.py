#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from colorama import Fore
import maskpass
from common import account


# （命令行交互模式）用户注册
def register():
    username = input('请输入用户名：')
    if account.exist(username)[1]:
        print(Fore.RED, '此用户名已被注册！', Fore.RESET)
        register()
    else:
        password = maskpass.askpass('请输入密码：')
        encrypt_pwd = account.encrypt(password)
        result = account.write(username, encrypt_pwd, 'user')
        if result == None: # 注册成功
            account.username = username
            account.usertype = 'user'
        else: # 发生错误
            return


# （命令行交互模式）用户登录
def login():
    username = input('请输入用户名：')
    if not account.exist(username)[1]:
        print(Fore.RED, '此用户名不存在！', Fore.RESET)
        login()
    else:
        password = maskpass.askpass('请输入密码：')
        check_result = account.check(username, account.encrypt(password))
        while True:
            if check_result[0]: # 发生错误
                password = maskpass.askpass('发生错误请重新输入密码：')
                check_result = account.check(username, account.encrypt(password))
            elif check_result[1] == False: # 密码错误
                print(Fore.RED, '密码错误，请重新输入密码：', Fore.RESET, end='')
                password = maskpass.askpass('')
                check_result = account.check(username, account.encrypt(password))
            else: # 没出错并且密码正确
                break
        account.username = username
        account.usertype = check_result[2]


# （命令行交互模式）修改密码
def change_password():
    current_password = maskpass.askpass('请输入当前密码：')
    check_result = account.check(account.username, account.encrypt(current_password))
    while True:
        if check_result[0]: # 发生错误
            current_password = maskpass.askpass('请重新输入密码：')
            check_result = account.check(account.username, account.encrypt(current_password))
        elif check_result[1] == False: # 密码错误
            print(Fore.RED, '密码错误，请重新输入密码：', Fore.RESET, end='')
            current_password = maskpass.askpass('')
            check_result = account.check(account.username, account.encrypt(current_password))
        else: # 没出错并且密码正确
            break
    new_password = maskpass.askpass('请输入新密码：')
    account.write(account.username, account.encrypt(new_password), account.usertype)
    print(Fore.GREEN, '密码修改成功！', Fore.RESET)
    return False
