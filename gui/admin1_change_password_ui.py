import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


class admin1_change_password(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./admin1_change_password.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.yes_btn = self.ui.pushButton  # 确认
        self.oldpasssword_qwidget = self.ui.lineEdit  # 原密码输入框
        self.newpassword_qwidget = self.ui.lineEdit_2  # 新密码输入框
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

        # 绑定信号与槽函数

        self.yes_btn.clicked.connect(self.clickedyes)

    # TODO
    def clickedyes(self):
        pass

    #     oldpasssword = self.oldpasssword_qwidget.text()
    #     newpassword = self.newpassword_qwidget.text()
    #
    #     self.textBrowser.setText(内容)
    #     self.textBrowser.repaint()
    #


def show():
    app = QApplication(sys.argv)

    w = admin1_change_password()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()





