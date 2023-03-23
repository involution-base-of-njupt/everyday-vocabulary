# -*- coding: utf-8 -*-
# 背单词汉译英
# TODO: 背错词模式
# TODO: 进度和正确率显示
import sys, os, time, random
from common import word, wrong_words
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from PyQt5 import uic


class ce(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        

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


    def init_ui(self):
        self.ui = uic.loadUi(f"{os.path.abspath('.')}/gui/ce.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件

        self.label = self.ui.label # “英文翻译是：”标签
        self.answer_qwidget = self.ui.lineEdit  # 答案输入框
        self.push_btn = self.ui.pushButton  # 提交按钮
        self.textBrowser = self.ui.textBrowser  # 文本显示区域

        self.get_dict()
        if self.get_dict_result[0]: # 获取字典时出错
            self.textBrowser.setText(f'获取字典时出错：{self.get_dict_result[0]}')
            self.label.setVisible(False)
            self.answer_qwidget.setVisible(False)
            self.push_btn.setText('重新获取字典')
            self.push_btn_func = 'reget_dict'
        elif self.amount_all == 0: # 没有单词
            self.textBrowser.setText('字典为空')
            self.label.setVisible(False)
            self.answer_qwidget.setVisible(False)
            self.push_btn.setText('重新获取字典')
            self.push_btn_func = 'reget_dict'
        else:
            self.label.setText('请输入：')
            self.label.setVisible(True)
            self.answer_qwidget.setVisible(True)
            self.push_btn.setText('准备背单词')
            self.push_btn_func = 'prepare_set_amount'


        # 绑定信号与槽函数
        self.push_btn.clicked.connect(self.clickedpush)   #按了提交按钮后开始一个叫clickedpush的函数


    # 设置背单词的数量
    def set_amount(self):
        self.word_dict_chinese_ver = {v: k for k, v in self.word_dict.items()}  #生成一个key为中文，valve为英文的字典
        self.textBrowser.setText("汉译英测试会展示你选择的单词及其中文含义，时间到后单词会消失，之后请根据汉语意思输入英文")
        self.label.setText('请输入要背的单词数量（个）：')
        self.push_btn.setText('确认')
        self.push_btn_func = 'set_amount'


    # 设置单词展示时间
    def set_time(self):
        self.textBrowser.setText('请输入单词展示时间（秒），展示时间过后单词会消失：')
        self.label.setText('请输入单词展示时间（秒）：')
        self.push_btn.setText('确认')
        self.push_btn_func = 'set_time'


    # 背单词准备
    def prepare_recite(self):
        self.words_test = random.sample(list(self.word_dict_chinese_ver.keys()), self.amount)


    # 背单词
    def recite(self):
        # TODO: 单独一个线程防止主线程阻塞
        self.answer_qwidget.enable = False
        self.current_word = self.words_test.pop()
        time_left = self.time_show
        self.label.setText('请记住英文')
        while time_left > 0:
            self.textBrowser.setText(f'''
    请记住单词的英文，时间到后单词会消失，之后请根据中文含义输入英文：
    单词：{self.word_dict_chinese_ver[self.current_word]}
    中文含义：{self.current_word}
    倒计时：{time_left}s
    ''')
            time.sleep(1)
            time_left -= 1
        self.textBrowser.setText(f'''
    请根据中文含义
    {self.current_word}
    输入英文：
    ''')
        self.label.setText('请输入英文：')
        self.answer_qwidget.enable = True
        self.push_btn_func = 'check_answer'


    # 确认按钮
    def clickedpush(self):
        # 根据不同的状态执行不同的操作
        if self.push_btn_func == 'reget_dict':
            self.get_dict()
            self.init_ui()
        elif self.push_btn_func == 'prepare_set_amount':
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
                    self.set_time()
            except ValueError:
                self.answer_qwidget.setText("请输入大于 0 的整数")
                self.set_amount()
        elif self.push_btn_func == 'prepare_set_time':
            self.set_time()
        elif self.push_btn_func == 'set_time':
            try:
                self.time_show = int(self.answer_qwidget.text())
                if self.time_show <= 0:
                    self.answer_qwidget.setText("请输入大于 0 的整数")
                    self.set_time()
                else:
                    self.prepare_recite()
                    self.recite()
            except ValueError:
                self.answer_qwidget.setText("请输入大于 0 的整数")
                self.set_time()
        elif self.push_btn_func == 'check_answer':
            if len(self.words_test) <=0:
                self.textBrowser.setText('背单词结束')
                self.label.setVisible(False)
                self.answer_qwidget.setVisible(False)
                self.push_btn.setText('继续背单词')
                self.push_btn_func = 'prepare_set_amount'
            if self.answer_qwidget.text() == self.word_dict_chinese_ver[self.current_word]:
                self.textBrowser.setText('回答正确')
                self.push_btn.setText('下一个')
                self.push_btn_func = 'next_word'
            else:
                self.textBrowser.setText(f'回答错误，正确答案是：{self.word_dict_chinese_ver[self.current_word]}')
                wrong_words.add_wrong_zh_word(self.current_word, self.word_dict_chinese_ver[self.current_word])
                self.push_btn.setText('下一个')
                self.push_btn_func = 'next_word'
        elif self.push_btn_func == 'next_word':
            self.recite()


def show():
    app = QApplication(sys.argv)

    w = ce()
    # 展示窗口
    w.ui.show()


    app.exec()

if __name__ == '__main__':
    show()