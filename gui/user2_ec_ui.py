# -*- coding: utf-8 -*-
# 用户错英译汉单词操作菜单
import sys, os
from gui import user1_ui


from PyQt5.QtWidgets import *
from PyQt5 import uic





class user2_ec(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/user2_ec.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.wrongwordlist_btn = self.ui.pushButton  # 查看所有错词
        self.searchwrongword_btn = self.ui.pushButton_2  # 搜索错词
        self.delectwrongword_btn = self.ui.pushButton_3  # 删除错词
        self.exit_btn = self.ui.pushButton_4  # 返回上级菜单.

        # 绑定信号与槽函数

        self.wrongwordlist_btn.clicked.connect(self.clickedwrongwordlist)
        self.searchwrongword_btn.clicked.connect(self.clickedsearchwrongword)
        self.delectwrongword_btn.clicked.connect(self.clickeddelectwrongword)
        self.exit_btn.clicked.connect(self.clickedexit)

        # TODO:

    def clickedwrongwordlist(self):
      pass

    def clickedsearchwrongword(self):
        # self.delect_word_window = delect_word_ui.delect_word()
        # self.delect_word_window.ui.show()
        pass

    def clickeddelectwrongword(self):
        # self.add_change_word_window = add_change_word_ui.add_change_word()
        # self.add_change_word_window.ui.show()
        pass

    def clickedexit(self):
        self.user1_window = user1_ui.user1()
        self.user1_window.ui.show()

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
    try:
        w = user2_ec()
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





