# -*- coding: utf-8 -*-
# 背单词汉译英
import sys, os, time, random
from common import word, wrong_words
from PyQt5.QtWidgets import *
from PyQt5 import uic


class ce(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        # 获取字典
        get_dict_result = word_manage.get_all()
        if not get_dict_result[0]: # 没出错
            word_dict = get_dict_result[1]  # 所有单词的字典
            amount_all = len(word_dict)  # 单词总数
            word_list = list(word_dict)  # 所有单词的列表，仅英文
        else: # 出错
            word_dict = {}
            amount_all = 0
            word_list = []


    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/ce.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件


        self.answer_qwidget = self.ui.lineEdit  # 密码输入框
        self.push_btn = self.ui.pushButton  # 提交按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

        # 绑定信号与槽函数
        self.push_btn.clicked.connect(self.clickedpush)   #按了提交按钮后开始一个叫clickedpush的函数



    # TODO:
    def clickedpush(self):
        print('耶')


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

    w = ce()
    # 展示窗口
    w.ui.show()


    app.exec()

if __name__ == '__main__':
    show()