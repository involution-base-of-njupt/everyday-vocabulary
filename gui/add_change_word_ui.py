# -*- coding: utf-8 -*-
# 增加或修改单词
import sys
import os
from common import word

from PyQt5.QtWidgets import *
from PyQt5 import uic

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class add_change_word(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/add_change_word.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.yes_btn = self.ui.pushButton  # 确认
        self.en_qwidget = self.ui.lineEdit  # 英文输入框
        self.cn_qwidget = self.ui.lineEdit_2  # 中文输入框
        self.textBrowser = self.ui.textBrowser  # 文本交互区域

         # 绑定信号与槽函数

        self.yes_btn.clicked.connect(self.clickedyes)   #按了确认操作按钮后开始一个函数





    # 确认按钮
    def clickedyes(self):
        en = self.en_qwidget.text()
        zh = self.cn_qwidget.text()
        exist_result = word.exist(en)
        if exist_result[0]: # 发生错误
            self.textBrowser.setText("检查单词时出错，请重试")
            return
        elif exist_result[1]:
            read_result = word.read(en)
            if read_result[0]: # 发生错误
                self.textBrowser.setText("读取单词时出错，请重试")
                return
            else: # 没出错，修改
                change_result = word.change(en, zh)
                if change_result: # 出错
                    self.textBrowser.setText("修改单词时出错，请重试")
                else:
                    self.textBrowser.setText(f"修改 {en} 的中文含义为 {zh} 成功")
        else: # 单词不存在
            add_result = word.add(en, zh)
            if add_result[0]: # 出错
                self.textBrowser.setText("添加单词时出错，请重试")
            else:
                self.textBrowser.setText(f"单词不存在，添加 {en}：{zh}成功")

        # self.textBrowser.setText("欢迎%s" % user_name)
        # self.textBrowser.repaint()




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

    w = add_change_word()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()






