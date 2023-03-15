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


word_dict = word_manage.get_all() # 所有单词的字典
amount_all = len(word_dict) # 单词总数
word_list = list(word_dict.keys()) # 所有单词的列表，仅英文


"""选择背诵单词数目"""


def choose_amount():
    while True:
        amount = input("请选择你想背的单词数量，请选择好后回车确定：")
        try:
            amount = int(amount)
            if amount > amount_all or amount <= 0:
                print("单词总数为%d，请重新输入" % amount_all)
                continue
            else:
                return amount
        except ValueError:
            print("请输入整数数字")
            continue
        


"""用于生成随机数"""


def random_words():
    amount = choose_amount()
    random_elements = random.sample(word_list, amount)
    print(random_elements)


"""英译中给出单词及对应中文含义"""


def english_translate_chinese():
    amount = choose_amount()
    print('你选择了%d个单词' % amount)
    for i in range(amount):
        print('请选择单词的正确中文含义')


if __name__ == '__main__':
    english_translate_chinese()
