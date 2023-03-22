import sys
import user1_ui

from PyQt5.QtWidgets import *
from PyQt5 import uic





class user2_manage_words(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./user2_manage_words.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.addword_btn = self.ui.pushButton  # 添加单词
        self.deleteword_btn = self.ui.pushButton_2  # 删除单词
        self.changeword_btn = self.ui.pushButton_3  # 修改单词
        self.searchword_btn = self.ui.pushButton_4  # 搜索单词
        self.showword_btn = self.ui.pushButton_5  # 输出单词列表
        self.exit_btn = self.ui.pushButton_6  # 返回上级菜单


         # 绑定信号与槽函数

        self.addword_btn.clicked.connect(self.clickedaddword)   #按了添加单词按钮后开始一个函数
        self.deleteword_btn.clicked.connect(self.clickeddeleteword)   #按了删除单词按钮后开始一个函数
        self.changeword_btn.clicked.connect(self.clickedchangeword)  # 按了修改单词按钮后开始一个函数
        self.searchword_btn.clicked.connect(self.clickedsearchword)  # 按了搜索单词按钮后开始一个函数
        self.showword_btn.clicked.connect(self.clickedshowword)  # 按了输出单词列表按钮后开始一个函数
        self.exit_btn.clicked.connect(self.clickedexit)  # 按了返回上级菜单按钮后开始一个函数

          # 定义以上6个函数


    # TODO:
    def clickedaddword(self):
        pass

    def clickeddeleteword(self):
        pass

    def clickedchangeword(self):
        pass

    def clickedsearchword(self):
        pass

    def clickedshowword(self):
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

    w = user2_manage_words()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()





