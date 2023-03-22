import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./E-C.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件



        self.A_btn = self.ui.pushButton_4  # A按钮
        self.B_btn = self.ui.pushButton_3  # B按钮
        self.C_btn = self.ui.pushButton_2  # C按钮
        self.D_btn = self.ui.pushButton  # D按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域
        self.user_qwidget = self.ui.lineEdit  # 密码输入框

        # 绑定信号与槽函数
        self.A_btn.clicked.connect(self.clickedA)   #按了A按钮后开始一个叫clickedA的函数
        self.B_btn.clicked.connect(self.clickedB)   #按了B按钮后开始一个叫clickedB的函数
        self.C_btn.clicked.connect(self.clickedC)   #按了C按钮后开始一个叫clickedC的函数
        self.D_btn.clicked.connect(self.clickedD)   #按了D按钮后开始一个叫clickedD的函数


    # TODO:
    def clickedA(self):
        print('A')

    def clickedB(self):
        print('B')

    def clickedC(self):
        print('C')

    def clickedD(self):
        print('D')


    def textBrowser(self):
        user = self.user_qwidget.text()

        # user_name = self.user_name_qwidget.text()
        # password = self.password_qwidget.text()
        # if user_name == "admin" and password == "123456":
        #     self.textBrowser.setText("欢迎%s" % user_name)
        #     self.textBrowser.repaint()
        # else:
        #     self.textBrowser.setText("用户名或密码错误....请重试")
        #     self.textBrowser.repaint()


def show():
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()


    app.exec()

if __name__ == '__main__':
    show()