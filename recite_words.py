"""背单词系统需要函数：
读取用户单词数（已完成
随机生成单词:读取单词数，生成对应数量的随机数，寻找对应的单词，展示
读取输入是否正确
读取选择是否正确
错误单词导入错题本
错题本修改，删除
等功能"""


import random
import csv
import word_manage

"""选择背诵单词数目"""


def choose_amount():
    amount = input("请选择你想背的单词数量,请选择好后回车确定")
    return amount


"""用于生成随机数"""


def random_words():
    amount = int(choose_amount())
    word_list = list(word_manage.get_all())
    f = open('words.csv', 'r', encoding='utf-8')
    count = 0
    reader = csv.reader(f)
    for row in reader:
        count += 1
    #print(count)
    #words_list = f.readlines()
    #print(words_list)
    #max_number = len(f.readlines())
    #print(max_number)
    all_numbers = range(1, count)
    lines_choices = random.sample(all_numbers, int(amount))
    for lines in lines_choices:
        lines_real = lines-1
        print(lines_real)
        print(word_list[int(lines_real)::])


"""英译中给出单词及对应中文含义"""


def english_translate_chinese():
    choose_amount()


random_words()
