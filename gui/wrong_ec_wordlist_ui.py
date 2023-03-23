# -*- coding: utf-8 -*-
# 单词列表界面
import sys, os
# import menu

from PyQt5.QtWidgets import *
from PyQt5 import uic





class wrong_ec_wordlist(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/wrong_wordlist.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.textBrowser = self.ui.textBrowser




    def showwordlist(self):

        self.textBrowser.setText("单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n""单词表\n" 'result')
        self.textBrowser.repaint()




def show():
    app = QApplication(sys.argv)

    w = wrong_ec_wordlist()

    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()





