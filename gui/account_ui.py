import sys
import os
from common import account

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


        # 绑定信号与槽函数

        self.login_btn.clicked.connect(self.clickedlogin)   #按了登陆按钮后开始一个叫函数
        self.register_btn.clicked.connect(self.clickedregister)   #按了注册按钮后开始一个叫函数



    # TODO:
    def clickedlogin(self):
        username = self.user_name_qwidget.text()
        password = self.password_qwidget.text()
        check_result = account.check(username, account.encrypt(password))
        while True:
            if check_result[0]: # 发生错误
                self.textBrowser.setText("检查用户时出错，请重试")
            elif check_result[1] == False: # 密码错误
                self.textBrowser.setText("用户名或密码错误，请重试")
            else: # 没出错并且密码正确
                break
        global account_username, account_type
        account_username = username
        account_type = check_result[2]
        if account_type == 'admin':
            self.textBrowser.setText(f"欢迎管理员 {account_username}！")
        elif account_type == 'user':
            self.textBrowser.setText(f"欢迎用户 {account_username}！")


    def clickedregister(self):
        pass


def show():
    app = QApplication(sys.argv)

    w = account()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()






