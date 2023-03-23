# -*- coding: utf-8 -*-
# 管理员用户管理菜单
import sys, os
from gui import admin1_ui
#from gui import userlist_ui
from gui import add_change_user_ui
from gui import delect_user_ui


from PyQt5.QtWidgets import *
from PyQt5 import uic




# ||||||||||||||||||||||||||||||||||||||||||||||||||

class admin2_manage_user(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/admin2_manage_user.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.adduser_btn = self.ui.pushButton  # 添加用户
        self.changepassword_btn = self.ui.pushButton_2  # 修改普通用户密码
        self.deleteuser_btn = self.ui.pushButton_3  # 删除用户
        self.userlist_btn = self.ui.pushButton_4  # 查看用户列表
        self.exit_btn = self.ui.pushButton_6  # 返回上级菜单.


         # 绑定信号与槽函数

        self.adduser_btn.clicked.connect(self.clickedadduser)
        self.changepassword_btn.clicked.connect(self.clickedchangepassword)
        self.deleteuser_btn.clicked.connect(self.clickeddeleteuser)
        self.userlist_btn.clicked.connect(self.clickeduserlist)
        self.exit_btn.clicked.connect(self.clickedexit)

          # 定义以上5个函数


    # TODO:
    def clickedadduser(self):
        self.add_change_user_window = add_change_user_ui.add_change_user()
        self.add_change_user_window.ui.show()

    def clickedchangepassword(self):
        self.add_change_user_window = add_change_user_ui.add_change_user()
        self.add_change_user_window.ui.show()

    def clickeddeleteuser(self):
        self.delect_user_window = delect_user_ui.delect_user()
        self.delect_user_window.ui.show()


    def clickeduserlist(self):
        self.userlist_window = userlist_ui.userlist()
        self.userlist_window.ui.show()

    def clickedexit(self):
        self.admin1_window = admin1_ui.admin1()
        self.admin1_window.ui.show()


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


def show():
    app = QApplication(sys.argv)

    w = admin2_manage_user()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()





