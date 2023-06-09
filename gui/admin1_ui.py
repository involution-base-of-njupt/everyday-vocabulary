# -*- coding: utf-8 -*-
# 管理员主菜单
import sys, os

from gui import account_ui
from gui import change_password_ui
#from gui import import_csv_json_ui
from gui import new_user_manage_ui
from gui import new_words_manage_ui

from PyQt5.QtWidgets import *
from PyQt5 import uic


class admin1(QWidget):


    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/admin1.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.manageword_btn = self.ui.pushButton  # 单词操作.
        self.inCSV_btn = self.ui.pushButton_2  # 导入CSV文件
        self.inJSON_btn = self.ui.pushButton_3  # 导入JSON文件
        self.changepassword_btn = self.ui.pushButton_4  # 修改密码
        self.manageuser_btn = self.ui.pushButton_5  # 用户管理.
        self.exit_btn = self.ui.pushButton_6  # 返回上级菜单.


         # 绑定信号与槽函数

        self.manageword_btn.clicked.connect(self.clickedmanageword)   #按了单词操作按钮后开始一个函数
        self.inCSV_btn.clicked.connect(self.clickedinCSV)   #按了导入CSV文件按钮后开始一个函数
        self.inJSON_btn.clicked.connect(self.clickedinJSON)  # 按了导入JSON文件按钮后开始一个函数
        self.changepassword_btn.clicked.connect(self.clickedchangepassword)  # 按了修改密码按钮后开始一个函数
        self.manageuser_btn.clicked.connect(self.clickedmanageuser)  # 按了用户管理按钮后开始一个函数
        self.exit_btn.clicked.connect(self.clickedexit)  # 按了返回上级菜单按钮后开始一个函数

          # 定义以上6个函数



    def clickedmanageword(self):
        self.new_words_manage_window = new_words_manage_ui.new_words_manage('admin')
        self.new_words_manage_window.ui.show()

    def clickedinCSV(self):
        self.import_csv_json_window = import_csv_json_ui.import_csv_json('csv')
        self.import_csv_json_window.ui.show()

    def clickedinJSON(self):
        self.import_csv_json_window = import_csv_json_ui.import_csv_json('json')
        self.import_csv_json_window.ui.show()

    def clickedchangepassword(self):
        self.change_password_ui_window = change_password_ui.change_password()
        self.change_password_window.ui.show()

    def clickedmanageuser(self):
        self.new_user_manage_window = new_user_manage_ui.new_user_manage()
        self.new_user_manage_window.ui.show()

    def clickedexit(self):
        self.account_window = account_ui.account_ui()
        self.account_window.ui.show()


def show():
    #if previous_window:
    #    previous_window.close()
    app = QApplication(sys.argv)
    try:
        w = admin1()
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






