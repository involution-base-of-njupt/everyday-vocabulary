#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import recite_words
import word_manage
import youdao
import account
import import_file
import os

# 管理员菜单
def admin_menu():
    print('''
    1. Add a word
    2. Delete a word
    3. Change a word
    4. Search a word
    5. Print wordlist
    6. Import a CSV file
    7. Import a JSON file
    8. Change my password
    9. Exit
    ''')
    choice = input('Please input your choice: ')
    if choice == '1':
        add_menu()
        admin_menu()
    elif choice == '2':
        delete_menu()
        admin_menu()
    elif choice == '3':
        change_menu()
        admin_menu()
    elif choice == '4':
        search_menu()
        admin_menu()
    elif choice == '5':
        print_menu()
        admin_menu()
    elif choice == '6':
        import_menu('csv')
        admin_menu()
    elif choice == '7':
        import_menu('json')
        admin_menu()
    elif choice == '8':
        account.change_password()
        admin_menu()
    elif choice == '9':
        exit()
    else:
        print('Invalid input!')
        admin_menu()

# 用户菜单
def user_menu():
    print('''
    1. Search a word
    2. Show Words
    3. Chinese to English
    4. English to Chinese
    5. Change my password
    5. Exit
    ''')
    choice = input('Please input your choice: ')
    if choice == '1':
        search_menu()
        user_menu()
    elif choice == '2':
        print_menu()
        user_menu()
    elif choice == '3':
        recite_words.chinese_translate_english()
        user_menu()
    elif choice == '4':
        recite_words.english_translate_chinese()
        user_menu()
    elif choice == '5':
        account.change_password()
        user_menu()
    elif choice == '6':
        exit()
    else:
        print('Invalid input!')
        user_menu()

# 添加单词菜单，可选传入英文单词
def add_menu(en = None):
    if en == None:
        en = input('Please input the English word: ')
    exist_query = word_manage.exist(en)
    if exist_query[0]:
        while exist_query[1]:
            print('The word already exists!')
            en = input('Please input the English word: ')
        zh = input_zh(en, False)
        if word_manage.add(en, zh):
            print('Add successfully!')
        else:
            print('Add failed!')
    else:
        
        # 查询失败，重新尝试添加
        add_menu(en)

# 删除单词菜单
def delete_menu():
    en = input('Please input the English word: ')
    if word_manage.delete(en):
        print('Delete successfully!')
    else:
        print('Delete failed!')



# 搜索单词菜单
def search_menu():
    en = input('Please input the English word: ')
    result = word_manage.search(en)
    if result[0]:
        print('The Chinese translation is: ' + result[1])
    else:
        print('No such word!')
    

# 修改单词菜单
def change_menu():
    
    # 输入英文单词
    en = input('Please input the English word: ')
    
    # 查询单词是否存在
    exist_query = word_manage.exist(en)
    if exist_query[0]: # 查询成功
        if exist_query[1]:# 如果存在，询问是否修改
            zh = input_zh(en, True)
            if word_manage.change(en, zh):
                print('Change successfully!')
            else:
                print('Change failed!')
        else:# 如果不存在，询问是否添加
            print('No such word!')
            choice = input('Add this word? (Y/N)')
            if choice == ('Y' or 'y'):
                add_menu()
            else:
                change_menu()
    else: # 查询失败
        change_menu()


# 展示单词菜单
def print_menu():
    word_dict = word_manage.get_all()
    if word_dict:
        # 逐个打印
        for word in word_dict:
            print(word + ' : ' + word_dict[word])
    else:
        print('No word in the database!')


# 输入中文菜单
def input_zh(en, enable_compare):
    choose_menu = '''
    1. Get translation from Youdao
    2. Input the translation manually
    '''
    if enable_compare:
        choose_menu += '3. Compare Youdao and the database'
    print(choose_menu)
    choice = input()
    if choice == '1':
        zh = youdao.translate(en)
        if zh:
            return zh
        else:
            print('Failed to get translation from Youdao!')
            return input_zh(en, enable_compare)
    elif choice == '2':
        zh = input('Please input the new Chinese translation: ')
        return zh
    elif choice == '3' and enable_compare:
        youdao_zh = youdao.translate(en)
        if youdao_zh:
            print('The Chinese translation from Youdao is: ' + youdao_zh)
            db_zh = word_manage.search(en)[1]
            if db_zh:
                print('The Chinese translation from the database is: ' + word_manage.search(en)[1])
            else:
                print('No such word in the database!')
                return input_zh(en, enable_compare)
            choice = input('Use the translation from Youdao? (Y/N)')
            if choice == ('Y' or 'y'):
                return youdao_zh
            else:
                return input_zh(en, enable_compare)
        else:
            print('Failed to get translation from Youdao!')
            return input_zh(en, enable_compare)
    else:
        print('Invalid input!')
        return input_zh(en, enable_compare)


# 导入文件菜单
def import_menu(file_type):
    
    # 输入文件位置
    file = input('Please input the file path (example: D:\\folder\\words.csv/json): ')
    while not os.path.isfile(file):
        print('No such file!')
        file = input('Please input the file path (example: D:\\folder\\words.csv/json): ')
   
    # 输入处理重复单词的方式
    mode = input('How to deal with duplicate words? (1: Overwrite, 2: Skip, 3: Abort): ')
    if mode == '3':
        return
    while mode != '1' and mode != '2' and mode != '3':
        print('Invalid input!')
        mode = input('How to deal with duplicate words? (1: Overwrite, 2: Skip, 3: Abort): ')
    
    # 调用导入文件函数
    if file_type == 'csv':
        import_result = import_file.csv_import(file, mode)
    elif file_type == 'json':
        import_result = import_file.json_import(file, mode)
    else:
        print('Invalid file type: ' + file_type + '!')
        return
    
    # 显示导入结果
    if import_result:
        print('Import successfully!')
    else:
        print('Import failed!')
