# -*- coding: utf-8 -*-
# 修改自身密码
import sys, os
from common import account

from PyQt5.QtWidgets import *
from PyQt5 import uic





class change_password(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/user_change_password.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.yes_btn = self.ui.pushButton  # 确认

        self.oldpasssword_qwidget = self.ui.lineEdit  # 原密码输入框
        self.newpassword_qwidget = self.ui.lineEdit_2  # 新密码输入框
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

         # 绑定信号与槽函数

        self.yes_btn.clicked.connect(self.clickedyes)







    def clickedyes(self):
        oldpasssword = self.oldpasssword_qwidget.text()
        check_result = account.check(account.username, account.encrypt(oldpasssword))
        if check_result[0]: # 出错
            self.textBrowser.setText(f'检查当前密码是否正确时发生错误：{check_result[0]}')
        elif not check_result[1]: #密码错误
            self.textBrowser.setText('当前密码错误，修改失败')
        else: # 没出错并且密码正确
            newpassword = self.newpassword_qwidget.text()
            account.write(account.username, account.encrypt(newpassword))
            self.textBrowser.setText('修改成功')


def show():
    app = QApplication(sys.argv)
    try:
        w = user_change_password()
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





