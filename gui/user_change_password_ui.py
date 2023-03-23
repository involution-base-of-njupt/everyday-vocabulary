import sys


from PyQt5.QtWidgets import *
from PyQt5 import uic





class user_change_password(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./user_change_password.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.old_yes_btn = self.ui.pushButton  # 确认原始密码
        self.new_yes_btn = self.ui.pushButton_2  # 确认新密码密码
        self.oldpasssword_qwidget = self.ui.lineEdit  # 原密码输入框
        self.newpassword_qwidget = self.ui.lineEdit_2  # 新密码输入框
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

         # 绑定信号与槽函数

        self.old_yes_btn.clicked.connect(self.clickedold_yes)
        self.new_yes_btn.clicked.connect(self.clickednew_yes)




# TODO
    def clickedold_yes(self):
        pass

    def clickednew_yes(self):
        pass



    #     oldpasssword = self.oldpasssword_qwidget.text()
    #     newpassword = self.newpassword_qwidget.text()
    #
    #     self.textBrowser.setText(内容)
    #     self.textBrowser.repaint()
    #
def show():
    app = QApplication(sys.argv)

    w = user_change_password()
    # 展示窗口
    w.ui.show()

    # w.setWindowOpacity(0.9)
    app.exec()


if __name__ == '__main__':
    show()





