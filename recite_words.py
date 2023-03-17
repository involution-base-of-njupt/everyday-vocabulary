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


def get_dict():
    global word_dict, amount_all, word_list
    word_dict = word_manage.get_all()[1]  # 所有单词的字典
    amount_all = len(word_dict)  # 单词总数
    word_list = list(word_dict)  # 所有单词的列表，仅英文
    if word_dict == {}:
        return False
    else:
        return True


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
        choice_number = input('请选择选项数量（数量在2到9之间），建议为4个')
        try:
            choice_number = int(choice_number)
        except Exception as e:
            print('发生错误：', e, '请重新输入')
            continue
        if choice_number < 0:
            print('请重新输入')
            continue
        elif choice_number < 2:
            print('请重新输入')
            continue
        elif 1 < choice_number < 10:
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
    if get_dict():
        amount = choose_amount()
        print('你选择了%d个单词' % amount)
        choice_number = choice_choose()
        words_test = random.sample(word_list, amount)
        for en in words_test:
            answer_list = {}
            for ans in range(choice_number):
                if not ans:
                    answer_list[0] = word_dict[en]
                else:
                    answer_list[ans] = word_dict.popitem()[1]
            print('请选择单词{}的正确中文含义：'.format(en))
            # 设置答案选项
            for ans in range(choice_number):
                answer = answer_list.popitem()[1]
                if answer == word_dict[en]:
                    correct_answer = ans + 1
                print('''
    {}. {}'''.format(ans + 1, answer))
            print('\n')
            while True:
                answer = input('请输入你的答案：')
                try:
                    answer = int(answer)
                    if answer == correct_answer:
                        print('回答正确')
                        break
                    elif answer > choice_number or answer <= 0:
                        print('请重新输入')
                        continue
                    else:
                        print('回答错误')
                        break
                except ValueError:
                    print('请输入数字')
                    continue
    else: # 数据库为空
        print('Dictionary is empty, please add words first.')
        return


if __name__ == '__main__':
    english_translate_chinese()
