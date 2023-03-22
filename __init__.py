#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__package__ = 'everyday_vocabulary'

# 入口菜单

from ui import account_ui
from shared import account
import menu
import sys
import signal
from colorama import Fore


# 命令行交互模式主函数，传入参数show_welcome（默认为True），控制是否显示欢迎信息
def cli_main(show_welcome=True):
    if show_welcome:
        print('欢迎使用天天背单词！')
    if account.init():
        print('''
    这是你第一次使用天天背单词！
    默认管理员账号：admin
    默认管理员密码：admin
        ''')
    while True:
        print('''
    1. 登录
    2. 注册用户
    3. 启动图形界面
    4. 退出
    ''')
        choice = input('请输入：')
        if choice == '1':
            account.login()
            if account.account_username:
                if account.account_type == 'admin':
                    print(Fore.GREEN, '成功以管理员身份登录！', Fore.RESET)
                    menu.admin_menu()
                elif account.account_type == 'user':
                    print(Fore.GREEN, '成功以用户身份登录！', Fore.RESET)
                    menu.user_menu()
                else:
                    print(Fore.RED, '未知账户类型！', Fore.RESET)
                    return
        elif choice == '2':
            account.register()
            if account.account_username:
                if account.account_type == 'admin':
                    print(Fore.GREEN, '成功以管理员身份注册，已自动登录！', Fore.RESET)
                    menu.admin_menu()
                elif account.account_type == 'user':
                    print(Fore.GREEN, '成功以用户身份注册，已自动登录！', Fore.RESET)
                    menu.user_menu()
                else:
                    print(Fore.RED, '未知账户类型！', Fore.RESET)
                    return
        elif choice == '3':
            gui_main()
        elif choice == '4':
            exit()
        else:
            print(Fore.RED, '输入错误！', Fore.RESET)
            cli_main(False)


# 图形界面主函数
def gui_main():
    account_ui.show()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL) # 使Ctrl+C可用
    if len(sys.argv) == 1 or sys.argv[0] == 'cli' or sys.argv[1] == 'cli': # 默认启动命令行交互模式
        cli_main()
    elif sys.argv[0] == 'gui' or sys.argv[1] == 'gui': # 启动图形界面
        gui_main()
    else: # 未知参数
        print(Fore.RED, '未知参数：', sys.argv, Fore.RESET)
        cli_main()
