# -*- coding: utf-8 -*-
# 用户列表界面（管理员用）
import sys, os
# import account

from PyQt5.QtWidgets import *
from PyQt5 import uic





class userlist(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/userlist.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.textBrowser = self.ui.textBrowser


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

    def showwordlist(self):

        self.textBrowser.setText('ffffffffffffffffffffffff')#ffffffff处放用户列表
        self.textBrowser.repaint()




def show():
    app = QApplication(sys.argv)

    w = userlist()
    w.showwordlist()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()





