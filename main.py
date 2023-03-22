#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 入口菜单

from ui.account_u import show_window
import account
import menu
import sys

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
            gui_main()
        elif choice == '4':
            exit()
        else:
            print('输入错误！')
            cli_main(False)


# 图形界面主函数
def gui_main():
    show_window()


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[0] == 'cli' or sys.argv[1] == 'cli': # 默认启动命令行交互模式
        cli_main()
    elif sys.argv[0] == 'gui' or sys.argv[1] == 'gui': # 启动图形界面
        gui_main()
    else: # 未知参数
        print('未知参数：', sys.argv)
        cli_main()