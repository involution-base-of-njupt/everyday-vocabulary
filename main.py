#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 命令行交互模式入口菜单

import account
import menu

# 传入参数show_welcome（默认为True），控制是否显示欢迎信息
def main(show_welcome=True):
    if show_welcome:
        print('Welcome to the English Dictionary!')
    if account.init():
        print('''
    This is the first time you use this dictionary!
    Default admin username: admin
    Default admin password: admin
        ''')
    print('Please login or register!')
    while True:
        print('''
    1. Login
    2. Register
    3. Exit
    ''')
        choice = input('Please input your choice: ')
        if choice == '1':
            account.login()
            if account.account_username:
                if account.account_type == 'admin':
                    print('Logged in as an admin.')
                    menu.admin_menu()
                elif account.account_type == 'user':
                    print('Logged in as a user.')
                    menu.user_menu()
                else:
                    print('Unkonwn account type!')
                    account.login()
        elif choice == '2':
            account.register()
            if account.account_username:
                if account.account_type == 'admin':
                    menu.admin_menu()
                elif account.account_type == 'user':
                    menu.user_menu()
                else:
                    print('Unkonwn account type!')
                    exit()
        elif choice == '3':
            exit()
        else:
            print('Invalid input!')
            main(False)


if __name__ == '__main__':
    main()