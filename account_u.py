# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account_u.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


#
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(1444, 898)
#         Form.setMaximumSize(QtCore.QSize(1444, 898))
#         Form.setStyleSheet("font: 14pt \"微软雅黑\";")
#         self.pushButton = QtWidgets.QPushButton(Form)
#         self.pushButton.setGeometry(QtCore.QRect(350, 350, 321, 51))
#         self.pushButton.setStyleSheet("\n"
# "font: 20pt \"微软雅黑\";\n"
# "background-color: rgb(0, 0, 0);\n"
# "color: rgb(255, 255, 255);")
#         self.pushButton.setObjectName("pushButton")
#         self.textBrowser = QtWidgets.QTextBrowser(Form)
#         self.textBrowser.setGeometry(QtCore.QRect(0, 0, 291, 451))
#         self.textBrowser.setStyleSheet("background-image: url(:/icon/account.png);")
#         self.textBrowser.setObjectName("textBrowser")
#         self.lineEdit = QtWidgets.QLineEdit(Form)
#         self.lineEdit.setGeometry(QtCore.QRect(420, 240, 261, 41))
#         self.lineEdit.setObjectName("lineEdit")
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(310, 160, 91, 41))
#         self.label.setStyleSheet("font: 18pt \"微软雅黑\";")
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(Form)
#         self.label_2.setGeometry(QtCore.QRect(320, 250, 61, 41))
#         self.label_2.setStyleSheet("font: 18pt \"微软雅黑\";")
#         self.label_2.setObjectName("label_2")
#         self.lineEdit_2 = QtWidgets.QLineEdit(Form)
#         self.lineEdit_2.setGeometry(QtCore.QRect(420, 160, 261, 41))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.pushButton_2 = QtWidgets.QPushButton(Form)
#         self.pushButton_2.setGeometry(QtCore.QRect(380, 40, 81, 51))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(Form)
#         self.pushButton_3.setGeometry(QtCore.QRect(540, 40, 81, 51))
#         self.pushButton_3.setObjectName("pushButton_3")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.pushButton.setText(_translate("Form", "确定"))
#         self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
#         self.label.setText(_translate("Form", "用户名"))
#         self.label_2.setText(_translate("Form", "密码"))
#         self.pushButton_2.setText(_translate("Form", "登陆"))
#         self.pushButton_3.setText(_translate("Form", "注册"))


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
        print('Error when writing account: ', e)
        return e
    finally:
        if f:
            f.close()

import account_picture_rc

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./account.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件
    #
    #     # 提取要操作的控件
    #     self.user_name_qwidget = self.ui.lineEdit  # 用户名输入框
    #     self.password_qwidget = self.ui.lineEdit_2  # 密码输入框
    #     self.login_btn = self.ui.pushButton  # 登录按钮
    #     self.forget_password_btn = self.ui.pushButton_2  # 忘记密码按钮
    #     self.textBrowser = self.ui.textBrowser  # 文本显示区域
    #
    #     # 绑定信号与槽函数
    #     self.login_btn.clicked.connect(self.login)
    #
          # def login(self):
    #     """登录按钮的槽函数"""
    #     user_name = self.user_name_qwidget.text()
    #     password = self.password_qwidget.text()
    #     if user_name == "admin" and password == "123456":
    #         self.textBrowser.setText("欢迎%s" % user_name)
    #         self.textBrowser.repaint()
    #     else:
    #         self.textBrowser.setText("用户名或密码错误....请重试")
    #         self.textBrowser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()
    w.ui.setWindowOpacity(0.9)
    #
    #
    # 哈哈哈哈哈哈哈哈哈哈透明啦哈哈哈哈哈哈
    #
    app.exec()