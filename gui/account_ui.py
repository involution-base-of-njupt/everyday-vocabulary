# -*- coding: utf-8 -*-
# 登录注册界面
import sys
import os
from common import account
from gui import admin1_ui
from gui import user1_ui

from PyQt5.QtWidgets import *
from PyQt5 import uic


class account(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/account.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件
        self.user_name_qwidget = self.ui.lineEdit_2  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit  # 密码输入框
        self.login_btn = self.ui.pushButton_2  # 登陆按钮
        self.register_btn = self.ui.pushButton_3  # 注册按钮
        self.textBrowser = self.ui.textBrowser # 显示框

        init_result = account.init()
        if init_result: # 是初始化
            self.textBrowser.setText('''
    这是你第一次使用天天背单词！
    默认管理员账号：admin
    默认管理员密码：admin
    ''')


        # 绑定信号与槽函数

        self.login_btn.clicked.connect(self.clickedlogin)   #按了登陆按钮后开始一个叫函数
        self.register_btn.clicked.connect(self.clickedregister)   #按了注册按钮后开始一个叫函数


    # 登录按钮
    def clickedlogin(self):
        username = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        check_result = account.check(username, account.encrypt(password))
        while True:
            if check_result[0]: # 发生错误
                self.textBrowser.setText(f"检查用户时出错：{check_result[0]}请重试")
                return
            elif check_result[1] == False: # 密码错误
                self.textBrowser.setText("用户名或密码错误，请重试")
                return
            else: # 没出错并且密码正确
                break
        account.username = username
        account.usertype = check_result[2]
        if account.usertype == 'admin':
            self.ui.textBrowser.setText(f"欢迎管理员 {username}！")
            self.admin1_window = admin1_ui.admin1()
            self.admin1_window.ui.show()
        elif account.usertype == 'user':
            self.ui.textBrowser.setText(f"欢迎用户 {username}！")
            self.user1_window = user1_ui.user1()
            self.user1_window.ui.show()
        else:
            self.textBrowser.setText(f"未知账户类型：{account.usertype}")
            return


    # 注册按钮
    def clickedregister(self):
        username = self.user_name_qwidget.text()
        exist_result = account.exist(username)
        if exist_result[0]:
            self.textBrowser.setText(f"检查用户时出错：{exist_result[0]}请重试")
            return
        elif exist_result[1]:
            self.textBrowser.setText("用户名已存在，请重试")
            return
        else:
            password = self.password_qwidget.text()
            write_result = account.write(username, account.encrypt(password), 'user')
            while True:
                if write_result[0]: # 发生错误
                    self.textBrowser.setText(f"写入用户时出错：{write_result[0]}，请重试")
                    return
                else: # 没出错
                    break
            account.username = username
            account.usertype = 'user'
            if account.usertype == 'admin':
                self.textBrowser.setText(f"注册成功，欢迎管理员 {username}！")
                self.admin1_window = admin1_ui.admin1()
                self.admin1_window.ui.show()
            elif account.usertype == 'user':
                self.textBrowser.setText(f"注册成功，欢迎用户 {username}！")
                self.user1_window = user1_ui.user1()
                self.user1_window.ui.show()
            else:
                self.textBrowser.setText(f"未知账户类型：{account.usertype}")


def show():
    app = QApplication(sys.argv)

    w = account()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()






