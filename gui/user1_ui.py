# -*- coding: utf-8 -*-
# 用户主菜单
import sys
from gui import account_ui
import os
from gui import ec_ui
from gui import ce_ui
from gui import new_words_manage_ui
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

        self.en_wrong_checkbox = self.ui.checkBox  # 英译中错词本
        self.ch_wrong_checkbox = self.ui.checkBox_2  # 中译英错词本
        self.words_btn = self.ui.pushButton_2  # 我的词库
        self.ec_btn = self.ui.pushButton_3  # 英译中测试
        self.ce_btn = self.ui.pushButton_4  # 中译英测试
        self.ecmanage_btn = self.ui.pushButton_5  # 英译中错词本管理
        self.cemanage_btn = self.ui.pushButton_6  # 中译英错词本管理
        self.changepassword_btn = self.ui.pushButton_7  # 修改密码
        self.exit_btn = self.ui.pushButton_8  # 返回上级菜单.


         # 绑定信号与槽函数

        self.words_btn.clicked.connect(self.show_word_dict)   # 我的词库
        self.ec_btn.clicked.connect(self.clickedec)  # 英译中测试
        self.ce_btn.clicked.connect(self.clickedce)  # 中译英测试
        self.ecmanage_btn.clicked.connect(self.clickedecmanage)  # 英译中错词本管理
        self.cemanage_btn.clicked.connect(self.clickedcemanage)  # 中译英错词本管理
        self.changepassword_btn.clicked.connect(self.clickedchangepassword) # 修改密码
        self.exit_btn.clicked.connect(self.clickedexit)  # 返回上级菜单

          # 定义以上函数


    def show_word_dict(self):
        self.new_words_manage_window = new_words_manage_ui.new_words_manage('user_default')
        self.new_words_manage_window.ui.show()

    def clickedec(self):
        if self.en_wrong_checkbox.isChecked():
            self.ec_window = ec_ui.ec(wrong_words_mode=True)
        else:
            self.ec_window = ec_ui.ec(wrong_words_mode=False)
        self.ec_window.ui.show()

    def clickedce(self):
        if self.ch_wrong_checkbox.isChecked():
            self.ce_window = ce_ui.ce(wrong_words_mode=True)
        else:
            self.ce_window = ce_ui.ce(wrong_words_mode=False)
        self.ce_window.ui.show()

    def clickedecmanage(self):
        self.new_words_manage_window = new_words_manage_ui.new_words_manage('user_en_wrong_words')
        self.new_words_manage_window.ui.show()

    def clickedcemanage(self):
        self.new_words_manage_window = new_words_manage_ui.new_words_manage('user_zh_wrong_words')
        self.new_words_manage_window.ui.show()

    def clickedchangepassword(self):
        self.change_password_window = change_password_ui.change_password()
        self.change_password_window.ui.show()

    def clickedexit(self):
        self.account_window = account_ui.account_ui()
        self.account_window.ui.show()


def show():
    app = QApplication(sys.argv)
    try:
        w = user1()
        # 展示窗口
        w.ui.show()
        app.exec()
    except Exception as e:
        print(e)
    finally:
        # 在应用程序关闭之前停止Qt对象的运行
        app.quit()


if __name__ == '__main__':
    show()






