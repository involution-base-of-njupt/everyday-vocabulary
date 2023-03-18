#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 命令行交互模式入口菜单

import account
import menu

# 传入参数show_welcome（默认为True），控制是否显示欢迎信息
def main(show_welcome=True):
    if show_welcome:
        print('欢迎使用天天背单词！')
    if account.init():
        print('''
    这是你第一次使用天天背单词！
    默认管理员账号：admin
    默认管理员密码：admin
        ''')
    print('Please login or register!')
    while True:
        print('''
    1. 登录
    2. 注册用户
    3. 退出
    ''')
        choice = input('请输入：')
        if choice == '1':
            account.login()
            if account.account_username:
                if account.account_type == 'admin':
                    print('成功以管理员身份登录！')
                    menu.admin_menu()
                elif account.account_type == 'user':
                    print('成功以用户身份登录！')
                    menu.user_menu()
                else:
                    print('未知账户类型！')
                    return
        elif choice == '2':
            account.register()
            if account.account_username:
                if account.account_type == 'admin':
                    menu.admin_menu()
                elif account.account_type == 'user':
                    menu.user_menu()
                else:
                    print('未知账户类型！')
                    return
        elif choice == '3':
            exit()
        else:
            print('输入错误！')
            main(False)


if __name__ == '__main__':
    main()