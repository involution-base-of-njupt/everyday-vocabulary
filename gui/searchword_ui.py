import sys
import admin1_ui

from PyQt5.QtWidgets import *
from PyQt5 import uic





class searchword(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./searchword.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.search_btn = self.ui.pushButton  # 搜索按钮



         # 绑定信号与槽函数

        self.search_btn.clicked.connect(self.clickedsearch)   #按了搜索按钮后开始一个函数

          # 定义以上5个函数


    # TODO:
    def clickedsearch(self):
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

    w = searchword()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()





