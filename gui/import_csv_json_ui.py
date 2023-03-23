# -*- coding: utf-8 -*-
import sys, os

from PyQt5.QtWidgets import *
from PyQt5 import uic


class import_csv_json(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/import_csv_json.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件


        self.locad_qwidget = self.ui.lineEdit  # 地址输入框
        self.answer_qwidget = self.ui.lineEdit  # 编码格式输入框
        self.yes_btn = self.ui.pushButton  # 是按钮
        self.no_btn = self.ui.pushButton_2  # 否按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

        # 绑定信号与槽函数
        self.yes_btn.clicked.connect(self.clickedyes)
        self.no_btn.clicked.connect(self.clickedno)

    # TODO:
    def clickedyes(self):
        print('耶')

    def clickedno(self):
        pass

   
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

    w = import_csv_json()
    # 展示窗口
    w.ui.show()


    app.exec()

if __name__ == '__main__':
    show()