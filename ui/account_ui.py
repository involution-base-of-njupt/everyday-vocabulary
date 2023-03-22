import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./account.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件
        self.user_name_qwidget = self.ui.lineEdit_2  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit  # 密码输入框
        self.login_btn = self.ui.pushButton_2  # 登陆按钮
        self.register_btn = self.ui.pushButton_3  # 注册按钮


        # 绑定信号与槽函数

        self.login_btn.clicked.connect(self.clickedlogin)   #按了登陆按钮后开始一个叫函数
        self.register_btn.clicked.connect(self.clickedregister)   #按了注册按钮后开始一个叫函数



    # TODO:
    def clickedlogin(self):
        pass

    def clickedregister(self):
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


def run():
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    run()






