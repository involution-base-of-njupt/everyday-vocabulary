# -*- coding: utf-8 -*-
# 背单词英译中界面
import sys, os, time, random
from common import word, wrong_words

from PyQt5.QtWidgets import *
from PyQt5 import uic


class ec(QWidget):

    def __init__(self, wrong_words_mode = False):
        super().__init__()
        self.wrong_words_mode = wrong_words_mode
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/ec.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件


        self.push_btn = self.ui.pushButton_5  # 啥都有的按钮
        self.A_btn = self.ui.pushButton_4  # A按钮
        self.B_btn = self.ui.pushButton_3  # B按钮
        self.C_btn = self.ui.pushButton_2  # C按钮
        self.D_btn = self.ui.pushButton  # D按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域
        self.answer_qwidget = self.ui.lineEdit  # 输入框

        # 绑定信号与槽函数
        self.A_btn.clicked.connect(self.clickedA)   #按了A按钮后开始一个叫clickedA的函数
        self.B_btn.clicked.connect(self.clickedB)   #按了B按钮后开始一个叫clickedB的函数
        self.C_btn.clicked.connect(self.clickedC)   #按了C按钮后开始一个叫clickedC的函数
        self.D_btn.clicked.connect(self.clickedD)   #按了D按钮后开始一个叫clickedD的函数

        self.A_btn.setVisible(False)
        self.B_btn.setVisible(False)
        self.C_btn.setVisible(False)
        self.D_btn.setVisible(False)


        self.get_dict()
        if self.get_dict_result[0]: # 获取字典时出错
            self.textBrowser.setText(f'获取字典时出错：{self.get_dict_result[0]}')
            self.push_btn.setText('重新获取字典')
            self.push_btn_func = 'reget_dict'
        elif self.amount_all == 0: # 没有单词
            self.textBrowser.setText('字典为空')
            self.push_btn.setText('重新获取字典')
            self.push_btn_func = 'reget_dict'
        else:
            self.push_btn.setText('准备背单词')
            self.push_btn_func = 'prepare_set_amount'


        # 绑定信号与槽函数
        self.push_btn.clicked.connect(self.clickedpush)   #按了提交按钮后开始一个叫clickedpush的函数

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

    # 设置背单词的数量
    def set_amount(self):
        self.textBrowser.setText("英译汉测试会展示你选择的单词，请根据英文选择汉语意思，请输入要背的单词数量（个）：")
        self.push_btn.setText('确认')
        self.push_btn_func = 'set_amount'


    # 背单词准备
    def prepare_recite(self):
        self.words_test = random.sample(list(self.word_dict.keys()), self.amount)


    # 背单词
    def recite(self):
        self.push_btn.setVisible(False)
        self.answer_qwidget.setVisible(False)
        self.A_btn.setVisible(True)
        self.B_btn.setVisible(True)
        self.C_btn.setVisible(True)
        self.D_btn.setVisible(True)

        self.current_word = self.words_test.pop()

        option_num = 4 # 选项数量
        correct_answer = random.randint(1, option_num)  # 随机选择正确答案序号
        self.correct_answer_text = self.word_dict[self.current_word]  # 正确答案文本
        option_list = { correct_answer - 1 : self.correct_answer_text }  # 选项字典，key为序号，value为选项内容，正确答案放入选项字典
        word_dict_without_correct_answer = self.word_dict
        del word_dict_without_correct_answer[self.current_word]  # 获得不包含正确答案的字典
        wrong_options = []  # 错误答案列表
        wrong_options += random.sample(list(word_dict_without_correct_answer.values()), option_num - 1)  # 添加错误答案

        i = 0
        for option_no in range(option_num): # 遍历每个选项
            if option_no not in option_list: # 如果此选项不是正确选项则设置错误答案
                option_list[option_no] = wrong_options[i]
                i += 1
        self.textBrowser.setText(f'''
你正在背第 {self.amount - len(self.words_test)} / {self.amount} 个单词
请根据英文选择汉语意思：
单词：{self.current_word}
A：{option_list[0]}
B：{option_list[1]}
C：{option_list[2]}
D：{option_list[3]}
''')
        self.wrong_options = wrong_options
        self.correct_answer = correct_answer


    def clickedA(self):
        if self.correct_answer == 1:
            self.textBrowser.setText('回答正确')
        else:
            self.textBrowser.setText(f'回答错误，正确答案是：{self.correct_answer_text}')
            wrong_words.add_wrong_en_word(self.current_word, self.correct_answer_text, self.wrong_options)
        if len(self.words_test) <= 0:
            self.textBrowser.setText('背单词结束')
            self.push_btn.setVisible(True)
            self.push_btn.setText('继续背单词')
            self.push_btn_func = 'prepare_set_amount'
        else:
            self.A_btn.setVisible(False)
            self.B_btn.setVisible(False)
            self.C_btn.setVisible(False)
            self.D_btn.setVisible(False)
            self.push_btn.setText('下一个')
            self.push_btn.setVisible(True)
            self.push_btn_func = 'next_word'


    def clickedB(self):
        if self.correct_answer == 2:
            self.textBrowser.setText('回答正确')
        else:
            self.textBrowser.setText(f'回答错误，正确答案是：{self.correct_answer_text}')
            wrong_words.add_wrong_en_word(self.current_word, self.correct_answer_text, self.wrong_options)
        if len(self.words_test) <= 0:
            self.textBrowser.setText('背单词结束')
            self.push_btn.setVisible(True)
            self.push_btn.setText('继续背单词')
            self.push_btn_func = 'prepare_set_amount'
        else:
            self.A_btn.setVisible(False)
            self.B_btn.setVisible(False)
            self.C_btn.setVisible(False)
            self.D_btn.setVisible(False)
            self.push_btn.setText('下一个')
            self.push_btn.setVisible(True)
            self.push_btn_func = 'next_word'

    def clickedC(self):
        if self.correct_answer == 3:
            self.textBrowser.setText('回答正确')
        else:
            self.textBrowser.setText(f'回答错误，正确答案是：{self.correct_answer_text}')
            wrong_words.add_wrong_en_word(self.current_word, self.correct_answer_text, self.wrong_options)
        if len(self.words_test) <= 0:
            self.textBrowser.setText('背单词结束')
            self.push_btn.setVisible(True)
            self.push_btn.setText('继续背单词')
            self.push_btn_func = 'prepare_set_amount'
        else:
            self.A_btn.setVisible(False)
            self.B_btn.setVisible(False)
            self.C_btn.setVisible(False)
            self.D_btn.setVisible(False)
            self.push_btn.setText('下一个')
            self.push_btn.setVisible(True)
            self.push_btn_func = 'next_word'

    def clickedD(self):
        if self.correct_answer == 4:
            self.textBrowser.setText('回答正确')
        else:
            self.textBrowser.setText(f'回答错误，正确答案是：{self.correct_answer_text}')
            wrong_words.add_wrong_en_word(self.current_word, self.correct_answer_text, self.wrong_options)
        if len(self.words_test) <= 0:
            self.textBrowser.setText('背单词结束')
            self.push_btn.setVisible(True)
            self.push_btn.setText('继续背单词')
            self.push_btn_func = 'prepare_set_amount'
        else:
            self.A_btn.setVisible(False)
            self.B_btn.setVisible(False)
            self.C_btn.setVisible(False)
            self.D_btn.setVisible(False)
            self.push_btn.setText('下一个')
            self.push_btn.setVisible(True)
            self.push_btn_func = 'next_word'




    # 确认按钮
    def clickedpush(self):
        # 根据不同的状态执行不同的操作
        if self.push_btn_func == 'reget_dict':
            self.get_dict()
            self.init_ui()
        elif self.push_btn_func == 'prepare_set_amount':
            self.answer_qwidget.setVisible(True)
            self.set_amount()
        elif self.push_btn_func == 'set_amount':
            try:
                self.amount = int(self.answer_qwidget.text())
                if self.amount <= 0:
                    self.answer_qwidget.setText("请输入大于 0 的整数")
                    self.set_amount()
                elif self.amount > self.amount_all:
                    self.answer_qwidget.setText(f"请输入小于等于单词总数 {self.amount_all} 的整数")
                    self.set_amount()
                else:
                    self.prepare_recite()
                    self.recite()
            except ValueError:
                self.answer_qwidget.setText("请输入大于 0 的整数")
                self.set_amount()
        elif self.push_btn_func == 'next_word':
            self.recite()


def show():
    app = QApplication(sys.argv)
    try:
        w = ec()
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