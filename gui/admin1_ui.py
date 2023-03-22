import sys
import admin2_manage_words_ui
import admin2_manage_user_ui
import account_ui


from PyQt5.QtWidgets import *
from PyQt5 import uic


class admin1(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./admin1.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.manageword_btn = self.ui.pushButton  # 单词操作.
        self.inCSV_btn = self.ui.pushButton_2  # 导入CSV文件
        self.inJSON_btn = self.ui.pushButton_3  # 导入JSON文件
        self.changepassword_btn = self.ui.pushButton_4  # 修改密码
        self.manageuser_btn = self.ui.pushButton_5  # 用户管理.
        self.exit_btn = self.ui.pushButton_6  # 返回上级菜单.


         # 绑定信号与槽函数

        self.manageword_btn.clicked.connect(self.clickedmanageword)   #按了单词操作按钮后开始一个函数
        self.inCSV_btn.clicked.connect(self.clickedinCSV)   #按了导入CSV文件按钮后开始一个函数
        self.inJSON_btn.clicked.connect(self.clickedinJSON)  # 按了导入JSON文件按钮后开始一个函数
        self.changepassword_btn.clicked.connect(self.clickedchangepassword)  # 按了修改密码按钮后开始一个函数
        self.manageuser_btn.clicked.connect(self.clickedmanageuser)  # 按了用户管理按钮后开始一个函数
        self.exit_btn.clicked.connect(self.clickedexit)  # 按了返回上级菜单按钮后开始一个函数

          # 定义以上6个函数


    # TODO:
    def clickedmanageword(self):
        self.admin2_manage_words_window = admin2_manage_words_ui.admin2_manage_words()
        self.admin2_manage_words_window.ui.show()

    def clickedinCSV(self):
        pass

    def clickedinJSON(self):
        pass

    def clickedchangepassword(self):
        pass

    def clickedmanageuser(self):
        self.admin2_manage_user_window = admin2_manage_user_ui.admin2_manage_user()
        self.admin2_manage_user_window.ui.show()

    def clickedexit(self):
        self.account_window = account_ui.account()
        self.account_window.ui.show()




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

    w = admin1()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()






