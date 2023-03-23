# -*- coding: utf-8 -*-
# 用户主菜单
import sys
from gui import account_ui
import os
from gui import ec_ui
from gui import ce_ui
from gui import new_words_manage_ui
from gui import user2_ce_ui
from gui import user2_ec_ui
from gui import change_password_ui

from PyQt5.QtWidgets import *
from PyQt5 import uic



class user1(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/user1.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.searchword_btn = self.ui.pushButton  # 搜索单词.
        self.wordlist_btn = self.ui.pushButton_2  # 输出单词列表
        self.ec_btn = self.ui.pushButton_3  # 英译中测试.
        self.ce_btn = self.ui.pushButton_4  # 中译英测试.
        self.ecmanage_btn = self.ui.pushButton_5  # 英译中错词本管理
        self.cemanage_btn = self.ui.pushButton_6  # 中译英错词本管理
        self.changepassword_btn = self.ui.pushButton_7  # 修改密码
        self.exit_btn = self.ui.pushButton_8  # 返回上级菜单.


         # 绑定信号与槽函数

        self.searchword_btn.clicked.connect(self.clickedsearchword)   # 搜索单词
        self.wordlist_btn.clicked.connect(self.clickedwordlist)   # 输出单词列表
        self.ec_btn.clicked.connect(self.clickedec)  # 英译中测试
        self.ce_btn.clicked.connect(self.clickedce)  # 中译英测试
        self.ecmanage_btn.clicked.connect(self.clickedecmanage)  # 英译中错词本管理
        self.cemanage_btn.clicked.connect(self.clickedcemanage)  # 中译英错词本管理
        self.changepassword_btn.clicked.connect(self.clickedchangepassword) # 修改密码
        self.exit_btn.clicked.connect(self.clickedexit)  # 返回上级菜单

          # 定义以上8个函数


    # TODO: 按钮改成单词菜单
    def clickedsearchword(self):
        self.new_words_manage_window = new_words_manage_ui.new_words_manage()
        self.new_words_manage_window.ui.show()

    def clickedwordlist(self):
        self.new_words_manage_window = new_words_manage_ui.new_words_manage()
        self.new_words_manage_window.ui.show()

    def clickedec(self):
        self.ec_window = ec_ui.ec()
        self.ec_window.ui.show()

    def clickedce(self):
        self.ce_window = ce_ui.ce()
        self.ce_window.ui.show()

    def clickedecmanage(self):
        self.user2_ec_window = user2_ec_ui.user2_ec()
        self.user2_ec_window.ui.show()

    def clickedcemanage(self):
        self.user2_ce_window = user2_ce_ui.user2_ce()
        self.user2_ce_window.ui.show()

    def clickedchangepassword(self):
        self.change_password_ui_window = change_password_ui.change_password()
        self.change_password_window.ui.show()

    def clickedexit(self):
        self.account_window = account_ui.account_ui()
        self.account_window.ui.show()




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

    w = user1()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()






