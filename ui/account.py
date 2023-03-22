"""
动态加载ui文件
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./account.ui")
    # 展示窗口
    ui.show()

    app.exec()


        # 提取要操作的控件
     #   self.user_name_qwidget = self.ui.lineEdit_2  # 用户名输入框
      #  self.password_qwidget = self.ui.lineEdit  # 密码输入框
    #     self.login_btn = self.ui.pushButton_2  # 登陆按钮
    #     self.register_btn = self.ui.pushButton_3  # 注册按钮
    #     self.yes_btn = self.ui.pushButton  # 确认按钮
    #
    # 
    #     # 绑定信号与槽函数
     #   self.login_btn.clicked.connect(self.login)
    #
    #     def login(self):
    #           print(1111)
    #     """登录按钮的槽函数"""
    #     user_name = self.user_name_qwidget.text()
    #     password = self.password_qwidget.text()
    #     if user_name == "admin" and password == "123456":
    #         self.textBrowser.setText("欢迎%s" % user_name)
    #         self.textBrowser.repaint()
    #     else:
    #         self.textBrowser.setText("用户名或密码错误....请重试")
    #         self.textBrowser.repaint()



    # w.setWindowOpacity(0.9)

