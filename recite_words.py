#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 背单词系统需要函数：
# DONE: 读取用户单词数
# 随机生成单词:读取单词数，生成对应数量的随机数，寻找对应的单词，展示
# 读取输入是否正确
# 读取选择是否正确
# 错误单词导入错题本
# 错题本修改，删除
# 等功能


import random
import word_manage


word_dict = word_manage.get_all()[1]  # 所有单词的字典
amount_all = len(word_dict)  # 单词总数
word_list = list(word_dict)  # 所有单词的列表，仅英文


# 选择背诵单词数目
def choose_amount():
    while True:
        amount = input('请选择你想背的单词数量，请选择好后回车确定：')
        try:
            amount = int(amount)
            if amount > amount_all or amount <= 0:
                print('单词总数为%d，请重新输入' % amount_all)
                continue
            else:
                return amount
        except ValueError:
            print('请输入整数数字')
            continue


# 进行选项数量选择
def choice_choose():
    while True:
        choice_number = input('请选择选项数量（数量在1到9之间），默认为4个，如果不想改变，请输入0退出选择')
        try:
            choice_number = int(choice_number)
        except Exception as e:
            print('发生错误：', e, '请重新输入')
            continue
        if choice_number < 0:
            print('请重新输入')
            continue
        elif choice_number == 0:
            choice_number = 4
            break
        elif 0 < choice_number < 10:
            break
        else:
            continue
    return choice_number


# 用于生成随机数
def random_words():
    amount = choose_amount()
    random_words = random.sample(word_list, amount)
    print(random_words)


# 英译中
def english_translate_chinese():
    amount = choose_amount()
    print('你选择了%d个单词' % amount)
    choice_number = choice_choose()
    words_test = random.sample(word_list, amount)
    for i in words_test:
        answer_list = {}
        for j in range(choice_number):
            if j == 1:
                answer_list[0] = word_dict[i]
            else:
                answer_list[j] = random.sample(word_dict.values(), choice_number)
        print('请选择单词的正确中文含义')
        print()


if __name__ == '__main__':
    english_translate_chinese()
