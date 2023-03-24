# -*- coding: utf-8 -*-
# 单词操作菜单
# TODO: 有道
import sys, os
from common import word, account, wrong_words

from gui import admin1_ui, user1_ui

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt


class new_words_manage(QWidget):

    def __init__(self, manage_mode):
        super().__init__()
        self.manage_mode = manage_mode
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/new_words_manage.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.label_en = self.ui.label_2  # 英文文本输入提示
        self.label_zh = self.ui.label_3  # 中文（正确）文本输入提示
        self.label_zh_wrong = self.ui.label  # 中文错词文本输入提示

        self.text_en = self.ui.plainTextEdit  # 英文文本输入区域
        self.text_zh = self.ui.plainTextEdit_2  # 中文（正确）文本输入区域
        self.text_zh_wrong = self.ui.plainTextEdit_3  # 中文错词文本输入区域

        self.secrch_en_btn = self.ui.pushButton_8  # 英文搜索按钮
        self.secrch_zh_btn = self.ui.pushButton_9  # 中文（正确）搜索按钮
        self.secrch_zh_wrong_btn = self.ui.pushButton_2  # 中文错词搜索按钮

        self.table = self.ui.tableWidget # 单词表格

        self.addword_btn = self.ui.pushButton  # 添加/修改单词
        #self.deleteword_btn = self.ui.pushButton_2  # 删除单词
        #self.changeword_btn = self.ui.pushButton_3  # 修改单词
        #self.searchword_btn = self.ui.pushButton_4  # 搜索单词

        self.showword_btn = self.ui.pushButton_5  # 读取单词列表

        self.exit_btn = self.ui.pushButton_6  # 返回上级菜单

        #self.label_current_mode = self.ui.label_5 # 当前操作
        #self.show_text = self.ui.textBrowser  # 操作结果展示

        self.save_btn = self.ui.pushButton_7 # 保存按钮

        self.show_text = self.ui.textBrowser  # 操作结果展示

        # 根据模式设置元素属性
        if self.manage_mode == 'admin':
            self.label_en.setVisible(True)
            self.label_en.setText('英文：')
            self.label_zh.setVisible(True)
            self.label_zh.setText('中文：')
            self.label_zh_wrong.setVisible(False)

            self.text_en.setVisible(True)
            self.text_zh.setVisible(True)
            self.text_zh_wrong.setVisible(False)


            self.secrch_en_btn.setVisible(True)
            self.secrch_zh_btn.setVisible(True)
            self.secrch_zh_wrong_btn.setVisible(False)

            #self.addword_btn.setVisible(True)
            #self.deleteword_btn.setVisible(True)
            #self.changeword_btn.setVisible(True)
            #self.searchword_btn.setVisible(True)
            self.showword_btn.setVisible(True)
            self.exit_btn.setVisible(True)
            self.save_btn.setVisible(True)
        elif self.manage_mode == 'user_default':
            self.label_en.setVisible(True)
            self.label_en.setText('英文：')
            self.label_zh.setVisible(True)
            self.label_zh.setText('中文：')
            self.label_zh_wrong.setVisible(False)

            self.text_en.setVisible(True)
            self.text_zh.setVisible(True)
            self.text_zh_wrong.setVisible(False)


            self.secrch_en_btn.setVisible(True)
            self.secrch_zh_btn.setVisible(True)
            self.secrch_zh_wrong_btn.setVisible(False)

            self.addword_btn.setVisible(False)
            #self.deleteword_btn.setVisible(False)
            #self.changeword_btn.setVisible(False)
            #self.searchword_btn.setVisible(True)
            self.showword_btn.setVisible(True)
            self.exit_btn.setVisible(True)
            self.save_btn.setVisible(False)
        elif self.manage_mode == 'user_en_wrong_words':
            self.label_en.setVisible(True)
            self.label_en.setText('英文：')
            self.label_zh.setVisible(True)
            self.label_zh.setText('正确中文：')
            self.label_zh_wrong.setVisible(True)
            self.label_zh_wrong.setText('错误中文：')

            self.text_en.setVisible(True)
            self.text_zh.setVisible(True)
            self.text_zh_wrong.setVisible(True)


            self.secrch_en_btn.setVisible(False)
            self.secrch_zh_btn.setVisible(False)
            self.secrch_zh_wrong_btn.setVisible(False)

            self.addword_btn.setVisible(False)
            #self.deleteword_btn.setVisible(True)
            #self.changeword_btn.setVisible(False)
            #self.searchword_btn.setVisible(True)
            self.showword_btn.setVisible(True)
            self.exit_btn.setVisible(True)
            self.save_btn.setVisible(False)
        elif self.manage_mode == 'user_zh_wrong_words':
            self.label_en.setVisible(True)
            self.label_en.setText('中文：')
            self.label_zh.setVisible(True)
            self.label_zh.setText('英文：')
            self.label_zh_wrong.setVisible(False)

            self.text_en.setVisible(True)
            self.text_zh.setVisible(True)
            self.text_zh_wrong.setVisible(False)


            self.secrch_en_btn.setVisible(False)
            self.secrch_zh_btn.setVisible(False)
            self.secrch_zh_wrong_btn.setVisible(False)

            self.addword_btn.setVisible(False)
            #self.deleteword_btn.setVisible(True)
            #self.changeword_btn.setVisible(False)
            #self.searchword_btn.setVisible(True)
            self.showword_btn.setVisible(True)
            self.exit_btn.setVisible(True)
            self.save_btn.setVisible(False)
        else:
            self.label_en.setVisible(False)
            self.label_zh.setVisible(False)
            self.label_zh_wrong.setVisible(False)

            self.text_en.setVisible(False)
            self.text_zh.setVisible(False)
            self.text_zh_wrong.setVisible(False)


            self.secrch_en_btn.setVisible(False)
            self.secrch_zh_btn.setVisible(False)
            self.secrch_zh_wrong_btn.setVisible(False)

            self.addword_btn.setVisible(False)
            #self.deleteword_btn.setVisible(False)
            #self.changeword_btn.setVisible(False)
            #self.searchword_btn.setVisible(False)
            self.showword_btn.setVisible(False)
            self.exit_btn.setVisible(True)
            self.save_btn.setVisible(False)
            self.show_text.setText(f'管理模式（{self.manage_mode}）或您的账户权限信息（{account.usertype}）有误')

        self.init_table() # 初始化单词表格

        # 绑定信号与槽函数

#        self.addword_btn.clicked.connect(self.clickedaddword)   #按了添加单词按钮后开始一个函数
#        self.deleteword_btn.clicked.connect(self.clickeddeleteword)   #按了删除单词按钮后开始一个函数
#        self.changeword_btn.clicked.connect(self.clickedchangeword)  # 按了修改单词按钮后开始一个函数
#        self.searchword_btn.clicked.connect(self.clickedsearchword)  # 按了搜索单词按钮后开始一个函数
        self.showword_btn.clicked.connect(self.clickedshowword)  # 按了输出单词列表按钮后开始一个函数
        self.exit_btn.clicked.connect(self.clickedexit)  # 按了返回上级菜单按钮后开始一个函数
        self.save_btn.clicked.connect(self.click_save) # 按保存按钮
        self.secrch_en_btn.clicked.connect(self.search_word)  # 按了搜索单词按钮后开始一个函数
        self.secrch_zh_btn.clicked.connect(self.search_word)  # 按了搜索单词按钮后开始一个函数
        self.secrch_zh_wrong_btn.clicked.connect(self.clickedsearchword_zh_wrong)  # 按了搜索单词按钮后开始一个函数
        self.table.itemSelectionChanged.connect(self.cell_clicked)  # 点击单词表格后开始一个函数

        # 定义以上函数


    def clickedshowword(self):
        self.get_dict()
        self.read_word()
        self.init_table()

    def clickedexit(self):
        # 关闭当前窗口
        # self.close()
        if self.manage_mode == 'admin':
            self.admin1_window = admin1_ui.admin1()
            self.admin1_window.ui.show()
        else:
            self.user1_window = user1_ui.user1()
            self.user1_window.ui.show()

    def click_save(self):
        self.save_word()


    def add_word(self):
        word = self.text_en.toPlainText()
        meaning = self.text_zh.toPlainText()
        if word == '' or meaning == '':
            self.show_text.setText('输入不能为空')
        else:
            if word in self.word_dict:
                self.show_text.setText(f'单词 {word} 已存在')
            else:
                self.word_dict[word] = meaning
                self.read_word()
                self.show_text.setText(f'单词 {word} 添加成功')


    def delete_word(self):
        en = self.text_en.toPlainText()
        if en == '':
            self.show_text.setText('输入不能为空')
        else:
            if en in self.word_dict:
                del self.word_dict[en]
                self.read_word()
                self.show_text.setText(f'单词 {en} 删除成功')
            else:
                self.show_text.setText(f'单词 {en} 不存在')


    def change_word(self):
        word = self.text_en.toPlainText()
        meaning = self.text_zh.toPlainText()
        if word == '' or meaning == '':
            self.show_text.setText('输入不能为空')
        else:
            if word in self.word_dict:
                self.word_dict[word] = meaning
                self.read_word()
                self.show_text.setText(f'单词 {word} 修改成功')
            else:
                self.show_text.setText(f'单词 {word} 不存在')

    def clickedsearchword_en(self):
        self.search_word('en')

    def clickedsearchword_zh(self):
        self.search_word('zh')
    
    def clickedsearchword_zh_wrong(self):
        self.search_word('zh_wrong')
    

    def search_word(self, mode):
        # TODO: 搜索错词
        if self.manage_mode == 'user_zh_wrong_words' and mode == 'zh':
            self.show_text.setText('未实现')
            #word = self.text_zh.toPlainText()
        elif self.manage_mode == 'user_en_wrong_words' and mode == 'en':
            self.show_text.setText('未实现')
            #word = self.text_en.toPlainText()
        else:
            self.show_text.setText('此模式下不支持该搜索')
        if word == '':
            self.show_text.setText('输入不能为空')
        else:
            if word in self.word_dict:
                self.show_text.setText(f'单词 {word} 的意思是：{self.word_dict[word]}')
            else:
                self.show_text.setText(f'单词 {word} 不存在')
    

    def cell_clicked(self):
        selected_items = self.table.selectedItems()  # 获取选中的单元格列表
        if selected_items:
            row = selected_items[0].row()  # 获取选中的单元格所在的行
            self.text_en.setPlainText(self.table.item(row, 0).text())
            self.text_zh.setPlainText(self.table.item(row, 1).text())
            if self.table.columnCount() == 3:
                self.text_zh_wrong.setPlainText(self.table.item(row, 2).text())


    def init_table(self):
        if self.manage_mode == 'admin':
            self.table.setColumnCount(2) # 设置表格一共有两列
            self.table.setHorizontalHeaderLabels(['英文', '中文']) # 设置表头文字
        elif self.manage_mode == 'user_default':
            self.table.setColumnCount(2) # 设置表格一共有两列
            self.table.setHorizontalHeaderLabels(['英文', '中文']) # 设置表头文字
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # 设置表格不可编辑
        elif self.manage_mode == 'user_en_wrong_words':
            self.table.setColumnCount(4) # 设置表格一共有四列
            self.table.setHorizontalHeaderLabels(['英文', '错误次数', '正确中文', '错误中文']) # 设置表头文字
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # 设置表格不可编辑
        elif self.manage_mode == 'user_zh_wrong_words':
            self.table.setColumnCount(3) # 设置表格一共有三列
            self.table.setHorizontalHeaderLabels(['中文', '错误次数', '正确英文']) # 设置表头文字
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # 设置表格不可编辑
        else:
            self.show_text.setText('未知模式')
        #self.table.setSectionResizeMode(QHeaderView.ResizeToContents) # 设置表格自适应宽度


    def read_word(self):
        row = 0
        error_messages = ''
        if self.manage_mode == 'user_en_wrong_words':
            for en in self.word_dict.items():
                self.table.setRowCount(row + 1)
                read_reault = wrong_words.read_wrong_zh_word(en)
                if read_reault[0]: # 出错
                    error_messages += read_reault[0] + '\n'
                else:
                    self.table.setItem(row,0,QTableWidgetItem(en))
                    self.table.setItem(row,1,QTableWidgetItem(str(self.word_dict[en])))
                    self.table.setItem(row,2,QTableWidgetItem(read_reault[1]))
                    self.table.setItem(row,3,QTableWidgetItem(str(read_reault[2])))
                    row += 1
            done_text = f'读取完成，错词总数：{row}'
            if error_messages:
                done_text += '\n' + error_messages
            self.show_text.setText(done_text)
        elif self.manage_mode == 'user_zh_wrong_words':
            for zh in self.word_dict.items():
                self.table.setRowCount(row + 1)
                read_reault = wrong_words.read_wrong_zh_word(zh)
                if read_reault[0]: # 出错
                    error_messages += read_reault[0] + '\n'
                else:
                    self.table.setItem(row,0,QTableWidgetItem(zh))
                    self.table.setItem(row,1,QTableWidgetItem(str(self.word_dict[zh])))
                    self.table.setItem(row,2,QTableWidgetItem(read_reault[1]))
                    row += 1
            done_text = f'读取完成，错词总数：{row}'
            if error_messages:
                done_text += '\n' + error_messages
            self.show_text.setText(done_text)
        else:
            for en, zh in self.word_dict.items():
                self.table.setRowCount(row + 1)
                self.table.setItem(row,0,QTableWidgetItem(en))
                self.table.setItem(row,1,QTableWidgetItem(zh))
                row += 1
            self.show_text.setText(f'读取完成，单词总数：{row}')


    def save_word(self): # 保存单词
        if self.manage_mode == 'admin':
            row_num = self.table.rowCount()
            empty_row = []
            new_word_dict = {}
            amount = 0
            for row in range(1, row_num):
                en = self.table.item(row, 0).text()
                zh = self.table.item(row, 1).text()
                if en == '' or zh == '':
                    empty_row.append(row)
                else:
                    new_word_dict[en] = zh
                    amount += 1
            else:
                if not amount:
                    if len(empty_row):
                        save_result = word.save_all(new_word_dict)
                        if save_result: # 出错
                            self.show_text.setText(f'保存时出错：{save_result}')
                        else:
                            self.word_dict = new_word_dict
                            self.show_text.setText(f'成功保存了 {amount} 个单词，第 {empty_row} 行有空内容未保存')
                    else:
                        save_result = word.save_all(new_word_dict)
                        if save_result: # 出错
                            self.show_text.setText(f'保存时出错：{save_result}')
                        else:
                            self.word_dict = new_word_dict
                            self.show_text.setText(f'成功保存了 {amount} 个单词')
                else:
                    if len(empty_row):
                        self.show_text.setText(f'第 {empty_row} 行有空内容，未检测到有效内容，未保存')
                    else:
                        self.show_text.setText('未检测到有效内容，未保存')
        else:
            self.show_text.setText('无权限')

    # 获取字典
    def get_dict(self):
        if self.manage_mode == 'user_en_wrong_words':
            get_dict_result = wrong_words.get_all_wrong_en_words()
            if not get_dict_result[0]: # 没出错
                self.word_dict = get_dict_result[1] # 所有错英文词的字典
            else: # 出错
                self.word_dict = {}
                self.show_text.setText(f'获取错词字典时错误：{get_dict_result[0]}')
        elif self.manage_mode == 'user_zh_wrong_words':
            get_dict_result = wrong_words.get_all_wrong_zh_words()
            if not get_dict_result[0]: # 没出错
                self.word_dict = get_dict_result[1] # 所有错中文词的字典
            else: # 出错
                self.word_dict = {}
                self.show_text.setText(f'获取错词字典时错误：{get_dict_result[0]}')
        else:
            get_dict_result = word.get_all()
            if not get_dict_result[0]: # 没出错
                self.word_dict = get_dict_result[1] # 所有单词的字典
            else: # 出错
                self.word_dict = {}
                self.show_text.setText(f'获取字典时错误：{get_dict_result[0]}')
    
    
    #def closeEvent(self, event):
        # 关闭窗口时触发
        #event.accept()


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
