# -*- coding: utf-8 -*-
# 删除单词界面（管理员用）
import sys
import os


from PyQt5.QtWidgets import *
from PyQt5 import uic


class delect_word(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/delect_word.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.yes_btn = self.ui.pushButton  # 确认
        self.en_qwidget = self.ui.lineEdit  # 英文输入框
        self.textBrowser = self.ui.textBrowser  # 文本交互区域

         # 绑定信号与槽函数

        self.yes_btn.clicked.connect(self.clickedyes)   #按了确认操作按钮后开始一个函数





    # TODO:
    def clickedyes(self):
        # en = self.en_qwidget.text()


        # self.textBrowser.setText(内容)
        # self.textBrowser.repaint()
       pass






def show():
    app = QApplication(sys.argv)

    w = delect_word()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()






