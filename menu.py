#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 命令行交互模式菜单

import recite_words
import word_manage
import youdao
import account
import import_file
import os
import wrong_words
from colorama import Fore

# 管理员菜单
# TODO: 用户管理菜单
def admin_menu():
    while True:
        print('''
    1. 添加单词
    2. 删除单词
    3. 修改单词
    4. 搜索单词
    5. 输出单词列表
    6. 导入CSV文件
    7. 导入JSON文件
    8. 修改密码
    9. 返回上级菜单
    ''')
        choice = input('请输入：')
        if choice == '1':
            add_menu()
        elif choice == '2':
            delete_menu()
        elif choice == '3':
            change_menu()
        elif choice == '4':
            search_menu()
        elif choice == '5':
            print_menu()
        elif choice == '6':
            import_menu('csv')
        elif choice == '7':
            import_menu('json')
        elif choice == '8':
            account.change_password()
        elif choice == '9':
            return
        else:
            print(Fore.RED, '输入错误！', Fore.RESET)

# 用户菜单
def user_menu():
    while True:
        print('''
    1. 搜索单词
    2. 输出单词列表
    3. 英译中测试
    4. 中译英测试
    5. 英译中错词本管理
    6. 中译英错词本管理
    7. 修改密码
    8. 返回上级菜单
    ''')
        choice = input('请输入：')
        if choice == '1':
            search_menu()
        elif choice == '2':
            print_menu()
        elif choice == '3':
            recite_words.english_translate_chinese()
        elif choice == '4':
            recite_words.chinese_translate_english()
        elif choice == '5':
            en2zh_wrong_words_menu()
        elif choice == '6':
            zh2en_wrong_words_menu()
        elif choice == '7':
            account.change_password()
        elif choice == '8':
            return
        else:
            print(Fore.RED, '输入错误！', Fore.RESET)

# 添加单词菜单，可选传入英文单词
def add_menu(en = None):
    if en == None:
        en = input('请输入英文单词：')
    exist_query = word_manage.exist(en)
    if exist_query[0]: # 查询失败，重新尝试添加
        add_menu(en)
    else: # 查询成功
        while exist_query[1]: # 单词存在，重新输入
            print('此单词已存在！')
            add_menu()
        zh = input_zh(en, False)
        result = word_manage.write(en, zh) # 强制写入
        if result[0] == None:
            print(Fore.GREEN, '添加成功！', Fore.RESET)
            return
        else:
            print(Fore.RED, '添加失败：', result[0], Fore.RESET)
            return

# 删除单词菜单
def delete_menu():
    en = input('请输入英文单词：')
    result = word_manage.delete(en)
    if result == None:
        print('删除成功！')
        return
    else:
        print('删除失败：', result)
        return



# 搜索单词菜单
def search_menu():
    en = input('请输入英文单词：')
    result = word_manage.search(en)
    if not result[0]:
        print('此单词的中文含义是：' + result[1])
        return
    else:
        print(Fore.RED, '此单词不存在！', Fore.RESET)
        return
    

# 修改单词菜单
def change_menu():
    
    # 输入英文单词
    en = input('请输入英文单词：')
    
    # 查询单词是否存在
    exist_query = word_manage.exist(en)
    if not exist_query[0]: # 查询成功
        if exist_query[1]:# 如果存在，询问是否修改
            zh = input_zh(en, True)
            result = word_manage.change(en, zh)
            if result == None:
                print(Fore.GREEN, '修改成功！', Fore.RESET)
                return
            else:
                print(Fore.RED, '修改失败：', result, Fore.RESET)
                return
        else:# 如果不存在，询问是否添加
            print(Fore.RED, '此单词不存在！', Fore.RESET)
            choice = input('是否添加此单词(Y/N)？')
            if choice == 'Y' or choice == 'y':
                add_menu(en)
            else:
                return
    else: # 查询失败
        return


# 展示单词菜单
def print_menu():
    result = word_manage.get_all()
    word_dict = result[1]
    if word_dict:
        # 逐个打印
        for word in word_dict:
            print(word, '：', word_dict[word])
        return
    else:
        print(Fore.RED, '发生错误：', result[0], Fore.RESET)


# 输入中文菜单
def input_zh(en, enable_compare):
    choose_menu = '''
    1. 联网从有道翻译获取中文含义
    2. 手动输入中文含义
    '''
    if enable_compare:
        choose_menu += '''3. 对比有道和数据库中的中文含义
    '''
    print(choose_menu)
    choice = input()
    if choice == '1':
        zh = youdao.translate(en)
        if zh[1]:
            return zh[1]
        else:
            print('从有道获取中文含义失败：', zh[0])
            return input_zh(en, enable_compare)
    elif choice == '2':
        zh = input('请输入中文含义：')
        return zh
    elif choice == '3' and enable_compare:
        youdao_zh = youdao.translate(en)
        if youdao_zh[1]:
            print('有道翻译的中文含义是：' + youdao_zh[1])
            db_zh = word_manage.search(en)
            if not db_zh[0]:
                print('数据库中的中文含义是：' + db_zh[1])
            else:
                print(Fore.RED, '发生错误：', db_zh[0], Fore.RESET)
                return input_zh(en, enable_compare)
            choice = input('是否保存有道翻译结果(Y/N)？')
            if choice == 'Y' or choice == 'y':
                return youdao_zh[1]
            else:
                return input_zh(en, enable_compare)
        else:
            print(Fore.RED, '从有道获取中文含义失败：', youdao_zh[0], Fore.RESET)
            return input_zh(en, enable_compare)
    else:
        print(Fore.RED, '输入错误！', Fore.RESET)
        return input_zh(en, enable_compare)


# 导入文件菜单
def import_menu(file_type):
    
    # 输入文件位置
    if file_type == 'csv':
        file = input('请输入文件路径（如：D:\\folder\\words.csv）（第一列为英文单词，第二列为中文含义）：')
    elif file_type == 'json':
        file = input('请输入文件路径（如：D:\\folder\\words.json）（单个object，键为英文单词，值为中文含义）：')
    else:
        print('错误的文件类型：', file_type, '！')
        return
    while not os.path.isfile(file):
        print(Fore.RED, '此文件不存在！', Fore.RESET)
        return
    
    # 输入文件编码方式
    codec = input('请输入文件编码（如：utf-8，gbk）：')

    # 输入处理重复单词的方式
    while True:
        choice = input('覆盖重复单词中文含义(Y/N)？')
        if choice == 'Y' or choice == 'y':
            overwrite = True
            break
        elif choice == 'N' or choice == 'n':
            overwrite = False
            break
        else:
            print(Fore.RED, '输入错误！', Fore.RESET)
    
    # 调用导入文件函数
    if file_type == 'csv':
        import_result = import_file.csv_import(file, codec, overwrite)
    elif file_type == 'json':
        import_result = import_file.json_import(file, codec, overwrite)
    else:
        print(Fore.RED, '错误的文件类型：' + file_type + '！', Fore.RESET)
        return
    
    # 显示导入结果
    if import_result == None:
        print(Fore.GREEN, '导入成功！', Fore.RESET)
    else:
        print(Fore.RED, '导入失败：', import_result, Fore.RESET)


# 英译中错词本菜单
def en2zh_wrong_words_menu():
    while True:
        print('''
    1. 查看所有错词
    2. 搜索错词
    3. 删除错词
    4. 背错词
    5. 返回上一级
    ''')
        choice = input()
        
        if choice == '1':
            result = wrong_words.get_all_wrong_en_words()
            if not result[0] == None:
                # 逐个打印
                for word, wrong_times in result[1]:
                    print(f'{word}：错误次数：{wrong_times}')
            else:
                print(Fore.RED, '发生错误：', result[0], Fore.RESET)
        
        elif choice == '2':
            en = input('请输入要搜索的英文单词：')
            result = wrong_words.read_wrong_en_word(en)
            if not result[0] == None:
                print(f'错词次数：{result[1]}，正确中文含义：{result[2]}，错误中文含义：{result[3]}')
            else:
                print(Fore.RED, '发生错误：', result[0], Fore.RESET)

        elif choice == '3':
            en = input('请输入要搜索的英文单词：')
            result = wrong_words.delete_wrong_en_word(en)
            if not result == None:
                print(Fore.RED, '发生错误：', result, Fore.RESET)
            else:
                print(Fore.GREEN, '删除成功！', Fore.RESET)
        
        elif choice == '4':
            recite_words.english_translate_chinese_wrong()

        elif choice == '5':
            return
        
        else:
            print(Fore.RED, '输入错误！', Fore.RESET)
            continue


# 中译英错词本菜单
def zh2en_wrong_words_menu():
    while True:
        print('''
    1. 查看所有错词
    2. 搜索错词
    3. 删除错词
    4. 背错词
    5. 返回上一级
    ''')
        choice = input()
        
        if choice == '1':
            result = wrong_words.get_all_wrong_zh_words()
            if not result[0] == None:
                # 逐个打印
                for word, wrong_times in result[1]:
                    print(f'{word}：错误次数：{wrong_times}')
            else:
                print(Fore.RED, '发生错误：', result[0], Fore.RESET)
        
        elif choice == '2':
            zh = input('请输入要搜索的中文释义：')
            result = wrong_words.read_wrong_zh_word(zh)
            if not result[0] == None:
                print(f'错词次数：{result[1]}，正确英文单词：{result[2]}')
            else:
                print(Fore.RED, '发生错误：', result[0], Fore.RESET)

        elif choice == '3':
            zh = input('请输入要删除的中文释义：')
            result = wrong_words.delete_wrong_zh_word(zh)
            if not result == None:
                print(Fore.RED, '发生错误：', result, Fore.RESET)
            else:
                print(Fore.GREEN, '删除成功！', Fore.RESET)

        elif choice == '4':
            recite_words.chinese_translate_english_wrong()

        elif choice == '5':
            return
        
        else:
            print(Fore.RED, '输入错误！', Fore.RESET)
            continue