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
import time
import wrong_words


def get_dict():
    global word_dict, amount_all, word_list
    word_dict = word_manage.get_all()[1]  # 所有单词的字典
    amount_all = len(word_dict)  # 单词总数
    word_list = list(word_dict)  # 所有单词的列表，仅英文
    if word_dict:
        return True
    else:
        return False


# 选择背诵单词数目


def input_amount():
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
def input_option_num():
    while True:
        option_num = input('请选择选项数量（数量在2到9之间），建议为4个：')
        try:
            option_num = int(option_num)
        except Exception as e:
            print('发生错误：', e, '请重新输入')
            continue
        if option_num < 0:
            print('请重新输入')
            continue
        elif option_num < 2:
            print('请重新输入')
            continue
        elif 1 < option_num < 10:
            break
        else:
            continue
    return option_num


# 英译中
def english_translate_chinese():
    if get_dict():
        word_amount = input_amount() # 要背的单词数量
        option_num = input_option_num() # 选项数量
        print('你要背 {} 个单词，每个单词有 {} 个选项。\n'.format(word_amount, option_num))
        test_words = random.sample(word_list, word_amount) # 抽取单词列表
        for en in test_words: # 遍历每个要背的单词
            correct_answer = random.randint(1, option_num) # 随机选择正确答案序号
            option_list = { correct_answer - 1 : word_dict[en] } # 选项字典，key为序号，value为选项内容，正确答案放入选项字典
            word_dict_without_correct_answer = word_dict
            del word_dict_without_correct_answer[en] # 获得不包含正确答案的字典
            wrong_options = [] # 错误答案列表
            wrong_options += random.sample(list(word_dict_without_correct_answer.values()), option_num - 1) # 添加错误答案
            print('请选择单词 {} 的正确中文含义：'.format(en))
            i = 0
            for option_no in range(option_num): # 遍历每个选项
                if option_no not in option_list: # 如果此选项不是正确选项则设置错误答案
                    option_list[option_no] = wrong_options[i]
                    i += 1
                print('''
    {}. {}'''.format(option_no + 1, option_list[option_no])) # 打印选项
            while True:
                choice = input('\n请输入你的答案：')
                try:
                    choice = int(choice)
                    if choice == correct_answer:
                        print('回答正确')
                        break
                    elif choice > option_num or choice <= 0:
                        print('请重新输入')
                        continue
                    else:
                        print('回答错误')
                        wrong_words.add_wrong_en_word(en, option_list[correct_answer - 1], wrong_options)
                        break
                except ValueError:
                    print('请输入数字')
                    continue
                except Exception as e:
                    print('发生错误：', e)
                    continue
    else: # 数据库为空
        print('数据库为空或错误，请检查数据库文件是否存在或是否正确')
        return


# 英译中背错词
def english_translate_chinese_wrong():
    result = wrong_words.get_all_wrong_en_words()
    wrong_en_words = result[1]
    word_data = ('', 0, '', [])
    if not wrong_en_words == {}:
        global amount_all
        amount_all = len(wrong_en_words)
        word_amount = input_amount() # 要背的单词数量
        print('你要背 {} 个单词。\n'.format(word_amount))
        test_words = random.sample(list(wrong_en_words.keys()), word_amount) # 抽取单词列表
        for en in test_words: # 遍历每个要背的单词
            word_data = wrong_words.read_wrong_en_word(en)
            if word_data[0]:
                print('发生错误：', word_data[0])
                break
            option_num = len(word_data[3]) + 1 # 选项数量
            correct_answer = random.randint(1, option_num) # 随机选择正确答案序号
            option_list = { correct_answer - 1 : word_data[2] } # 选项字典，key为序号，value为选项内容，正确答案放入选项字典
            wrong_options = word_data[3] # 错误答案列表
            print('请选择单词 {} 的正确中文含义：'.format(en))
            print('这个词之前错了 {} 次'.format(word_data[1]))
            i = 0
            for option_no in range(option_num): # 遍历每个选项
                if option_no not in option_list: # 如果此选项不是正确选项则设置错误答案
                    option_list[option_no] = wrong_options[i]
                    i += 1
                print('''
    {}. {}'''.format(option_no + 1, option_list[option_no])) # 打印选项
            while True:
                choice = input('\n请输入你的答案：')
                try:
                    choice = int(choice)
                    if choice == correct_answer:
                        print('回答正确')
                        break
                    elif choice > option_num or choice <= 0:
                        print('请重新输入')
                        continue
                    else:
                        print('回答错误')
                        wrong_words.add_wrong_en_word(en)
                        break
                except ValueError:
                    print('请输入数字')
                    continue
                except Exception as e:
                    print('发生错误：', e)
                    continue
    else: # 数据库为空或出错
        print('数据库为空或错误，请检查数据库文件是否存在或是否正确')
        if result[0]:
            print('错误信息：', result[0])
        if word_data[0]:
            print('错误信息：', word_data[0])
        return


# 中译英
def chinese_translate_english():
    if get_dict():
        word_dict_chinese_ver = {v: k for k, v in word_dict.items()}  #生成一个key为中文，valve为英文的字典
        print("汉译英测试会展示你选择的单词及其中文含义，时间到后单词会消失，之后请根据汉语意思输入英文")
        amount = input_amount()
        print("你选择了%d个单词" % amount)
        while True:
            print('请选择单词展示时间（秒），展示时间过后单词会消失：')
            try:
                time_left = int(input(''))
                break
            except ValueError:
                print("请输入数字")
                continue
        words_test = random.sample(list(word_dict.values()), amount)
        for zh in words_test:
            print(zh, end='\n')
            time_real = time_left
            while time_real > 0:
                print(word_dict_chinese_ver[zh], ' 倒计时：', time_real, 's', end='')
                time.sleep(1)
                print('\r', end='')
                time_real = time_real - 1
            print('\r', end='')
            user_answer = input("请输入答案，按回车确定：\n")
            if user_answer == word_dict_chinese_ver[zh]:
                print('回答正确')
            else:
                print("回答错误")
                wrong_words.add_wrong_zh_word(zh, word_dict_chinese_ver[zh])
    else: # 数据库为空
        print('数据库为空或错误，请检查数据库文件是否存在或是否正确')
        return


# 中译英背错词
def chinese_translate_english_wrong():
    result = wrong_words.get_all_wrong_zh_words()
    wrong_zh_words = result[1]
    word_data = ('', 0, '', [])
    if not wrong_zh_words == {}:
        global amount_all
        amount_all = len(wrong_zh_words)
        word_amount = input_amount() # 要背的单词数量
        print('你要背 {} 个单词。\n'.format(word_amount))
        test_words = random.sample(list(wrong_zh_words.keys()), word_amount) # 抽取单词列表
        for zh in test_words: # 遍历每个要背的单词
            word_data = wrong_words.read_wrong_zh_word(zh)
            if word_data[0]:
                print('发生错误：', word_data[0])
                continue
            print('输入中文含义 {} 的正确英文单词，这个词之前错了 {} 次'.format(zh, word_data[1]))
            answer = input('\n请输入你的答案：')
            if answer == word_data[2]:
                print('回答正确')
            else:
                print('回答错误')
                wrong_words.add_wrong_zh_word(zh)
    else: # 数据库为空或出错
        print('数据库为空或错误，请检查数据库文件是否存在或是否正确')
        if result[0]:
            print('错误信息：', result[0])
        if word_data[0]:
            print('错误信息：', word_data[0])
        return
