# -*- coding: utf-8 -*-
# 单词操作菜单
# TODO:直接操作表格来更改
import sys, os
from common import word, account


from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt


class new_words_manage(QWidget):

    def __init__(self, manage_mode):
        self.manage_mode = manage_mode
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/new_words_manage.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.label_en = self.ui.label_2  # 英文文本输入提示
        self.label_zh = self.ui.label_3  # 中文文本输入提示
        self.text1 = self.ui.plainTextEdit  # 英文文本输入展示区域
        self.text2 = self.ui.plainTextEdit_2  # 中文文本输入展示区域
        self.table = self.ui.tableWidget # 单词表格
        self.addword_btn = self.ui.pushButton  # 添加单词
        self.deleteword_btn = self.ui.pushButton_2  # 删除单词
        self.changeword_btn = self.ui.pushButton_3  # 修改单词
        self.searchword_btn = self.ui.pushButton_4  # 搜索单词.
        self.showword_btn = self.ui.pushButton_5  # 输出单词列表
        self.exit_btn = self.ui.pushButton_6  # 返回上级菜单.
        self.label_current_mode = self.ui.label_5 # 当前操作
        self.text3 = self.ui.label_4  # 操作结果展示
        self.enter_btn = self.ui.pushButton_7 # 确认按钮

        # 根据模式设置元件可见性
        if self.manage_mode == 'admin':
            self.label_en.setVisible(False)
            self.label_zh.setVisible(False)
            self.text1.setVisible(False)
            self.text2.setVisible(False)
            self.addword_btn.setVisible(True)
            self.deleteword_btn.setVisible(True)
            self.changeword_btn.setVisible(True)
            self.searchword_btn.setVisible(True)
            self.showword_btn.setVisible(True)
            self.exit_btn.setVisible(True)
            self.enter_btn.setVisible(True)
        elif self.manage_mode == 'user_default':
            self.label_en.setVisible(False)
            self.label_zh.setVisible(False)
            self.text1.setVisible(False)
            self.text2.setVisible(False)
            self.addword_btn.setVisible(False)
            self.deleteword_btn.setVisible(False)
            self.changeword_btn.setVisible(False)
            self.searchword_btn.setVisible(True)
            self.showword_btn.setVisible(True)
            self.exit_btn.setVisible(True)
            self.enter_btn.setVisible(True)
        elif self.manage_mode == 'user_wrong_words':
            self.label_en.setVisible(False)
            self.label_zh.setVisible(False)
            self.text1.setVisible(False)
            self.text2.setVisible(False)
            self.addword_btn.setVisible(False)
            self.deleteword_btn.setVisible(True)
            self.changeword_btn.setVisible(False)
            self.searchword_btn.setVisible(True)
            self.showword_btn.setVisible(True)
            self.exit_btn.setVisible(True)
            self.enter_btn.setVisible(True)
        else:
            self.label_en.setVisible(False)
            self.label_zh.setVisible(False)
            self.text1.setVisible(False)
            self.text2.setVisible(False)
            self.addword_btn.setVisible(False)
            self.deleteword_btn.setVisible(False)
            self.changeword_btn.setVisible(False)
            self.searchword_btn.setVisible(False)
            self.showword_btn.setVisible(False)
            self.exit_btn.setVisible(True)
            self.enter_btn.setVisible(False)
            self.text3.setText(f'管理模式（{self.manage_mode}）您的账户权限信息（{account.usertype}）有误')

        self.init_table() # 初始化单词表格

        # 绑定信号与槽函数

        self.addword_btn.clicked.connect(self.clickedaddword)   #按了添加单词按钮后开始一个函数
        self.deleteword_btn.clicked.connect(self.clickeddeleteword)   #按了删除单词按钮后开始一个函数
        self.changeword_btn.clicked.connect(self.clickedchangeword)  # 按了修改单词按钮后开始一个函数
        self.searchword_btn.clicked.connect(self.clickedsearchword)  # 按了搜索单词按钮后开始一个函数
        self.showword_btn.clicked.connect(self.clickedshowword)  # 按了输出单词列表按钮后开始一个函数
        self.exit_btn.clicked.connect(self.clickedexit)  # 按了返回上级菜单按钮后开始一个函数
        self.enter_btn.clicked.connect(self.click_enter) # 按确认按钮

        # 定义以上函数


    # 在界面上显示当前操作模式
    def show_current_mode(self):
        if self.current_mode == None:
            self.label_current_mode.setText('无')
        elif self.current_mode == 'add':
            self.label_current_mode.setText('添加单词')
        elif self.current_mode == 'del':
            self.label_current_mode.setText('删除单词')
        elif self.current_mode == 'change':
            self.label_current_mode.setText('修改单词')
        elif self.current_mode == 'search':
            self.label_current_mode.setText('搜索单词')
        elif self.current_mode == 'read':
            self.label_current_mode.setText('读取单词列表')
        else:
            self.label_current_mode.setText(f'未知：{self.current_mode}')


    def clickedaddword(self):
        self.current_mode = 'add'
        self.show_current_mode()

    def clickeddeleteword(self):
        self.current_mode = 'del'
        self.show_current_mode()

    def clickedchangeword(self):
        self.current_mode = 'change'
        self.show_current_mode()

    def clickedsearchword(self):
        self.current_mode = 'search'
        self.show_current_mode()

    def clickedshowword(self):
        self.read_word()
        self.init_table()

    def clickedexit(self):
        pass
        # self.admin1_window = admin1_ui.admin1()
        # self.admin1_window.ui.show()

    def click_enter(self):
        self.save_word()
        if False:
            if self.current_mode == None:
                self.text3.setText('没有选择模式')
            elif self.current_mode == 'add':
                self.add_word()
            elif self.current_mode == 'del':
                self.delete_word()
            elif self.current_mode == 'change':
                self.change_word()
            elif self.current_mode == 'search':
                self.search_word()
            elif self.current_mode == 'read':
                self.read_word()
            else:
                self.text3.setText(f'未知模式：{self.current_mode}）')


    def add_word(self):
        word = self.text1.toPlainText()
        meaning = self.text2.toPlainText()
        if word == '' or meaning == '':
            self.text3.setText('输入不能为空')
        else:
            if word in self.word_dict:
                self.text3.setText(f'单词 {word} 已存在')
            else:
                self.word_dict[word] = meaning
                self.text3.setText(f'单词 {word} 添加成功')


    def delete_word(self):
        en = self.text1.toPlainText()
        if en == '':
            self.text3.setText('输入不能为空')
        else:
            if en in self.word_dict:
                del self.word_dict[en]
                self.text3.setText(f'单词 {en} 删除成功')
            else:
                self.text3.setText(f'单词 {word} 不存在')


    def change_word(self):
        word = self.text1.toPlainText()
        meaning = self.text2.toPlainText()
        if word == '' or meaning == '':
            self.text3.setText('输入不能为空')
        else:
            if word in self.word_dict:
                self.word_dict[word] = meaning
                self.text3.setText(f'单词 {word} 修改成功')
            else:
                self.text3.setText(f'单词 {word} 不存在')


    def search_word(self):
        word = self.text1.toPlainText()
        if word == '':
            self.text3.setText('输入不能为空')
        else:
            if word in self.word_dict:
                self.text3.setText(f'单词 {word} 的意思是：{self.word_dict[word]}')
            else:
                self.text3.setText(f'单词 {word} 不存在')
    

    def init_table(self):
        self.table.setColumnCount(3) # 设置表格一共有两列
        self.table.setHorizontalHeaderLabels(['英文', '中文', '选择']) # 设置表头文字
        self.table.sortItems(0, Qt.AscendingOrder) # 按第一列升序排列
        self.table.verticalHeader().setStretchLastSection(True) # 最后一列自适应


    def read_word(self):
        self.get_dict()
        row = 0
        for en, zh in self.word_dict.items():
            self.table.setRowCount(row + 1)
            self.table.setItem(row,0,QTableWidgetItem(en))
            self.table.setItem(row,1,QTableWidgetItem(zh))
            row += 1
        self.text3.setText(f'读取完成，单词总数：{self.amount_all}')


    def save_word(self): # 保存单词
        if account.usertype == 'admin':
            self.save_result = word.save_all(self.word_dict)
            if self.save_result: # 出错
                self.text3.setText(f'保存时出错：{self.save_result}')
            else:
                self.text3.setText('保存成功')
        else:
            self.text3.setText('只有管理员才能保存单词')

    def get_dict(self):
        # 获取字典
        self.get_dict_result = word.get_all()
        if not self.get_dict_result[0]: # 没出错
            self.word_dict = self.get_dict_result[1]  # 所有单词的字典
            self.amount_all = len(self.word_dict)  # 单词总数
            self.word_list = list(self.word_dict)  # 所有单词的列表，仅英文
        else: # 出错
            self.word_dict = {}
            self.amount_all = 0
            self.word_list = []


def show():
    app = QApplication(sys.argv)
    try:
        w = new_words_manage()
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
