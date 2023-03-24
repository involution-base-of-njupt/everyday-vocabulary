# -*- coding: utf-8 -*-
# 增加或修改用户（管理员用）
import sys
import os
from common import account

from PyQt5.QtWidgets import *
from PyQt5 import uic

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class add_change_user(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/add_change_user.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.yes_btn = self.ui.pushButton  # 确认
        self.user_qwidget = self.ui.lineEdit  # 用户名输入框
        self.password_qwidget = self.ui.lineEdit_2  # 密码输入框
        self.textBrowser = self.ui.textBrowser  # 文本交互区域

         # 绑定信号与槽函数

        self.yes_btn.clicked.connect(self.clickedyes)   #按了确认操作按钮后开始一个函数




    # 确认按钮
    def clickedyes(self):
        username = self.user_qwidget.text()
        exist_result = account.exist(username)
        if exist_result[0]: # 发生错误
            self.textBrowser.setText("检查用户时出错，请重试")
            return
        elif exist_result[1]:
            check_result = account.check(username)
            if check_result[0]: # 发生错误
                self.textBrowser.setText("检查用户时出错，请重试")
                return
            elif check_result[2] == 'admin':
                self.textBrowser.setText(f"{username}是管理员，你不能修改他的的密码，请重试")
            else: # 没出错，修改密码
                password = self.password_qwidget.text()
                if write_result: # 出错
                    self.textBrowser.setText("写入用户时出错，请重试")
                else:
                    self.textBrowser.setText(f"修改 {username} 的密码成功")
        else: # 用户名不存在
            password = self.password_qwidget.text()
            write_result = account.write(username, account.encrypt(password))
            if write_result: # 出错
                self.textBrowser.setText("写入用户时出错，请重试")
            else:
                self.textBrowser.setText(f"用户名不存在，添加用户 {username} 成功")


def show():
    app = QApplication(sys.argv)
    try:
        w = add_change_user()
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






