#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 命令行交互模式菜单

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
    6. Exit
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
    if exist_query[0]: # 查询失败，重新尝试添加
        add_menu(en)
    else: # 查询成功
        while exist_query[1]: # 单词存在，重新输入
            print('The word already exists!')
            add_menu()
        zh = input_zh(en, False)
        result = word_manage.write(en, zh) # 强制写入
        if result[0] == None:
            print('Add successfully!')
        else:
            print('Add failed: ', result[0])

# 删除单词菜单
def delete_menu():
    en = input('Please input the English word: ')
    if word_manage.delete(en) == None:
        print('Delete successfully!')
    else:
        print('Delete failed!')



# 搜索单词菜单
def search_menu():
    en = input('Please input the English word: ')
    result = word_manage.search(en)
    if not result[0]:
        print('The Chinese translation is: ' + result[1])
    else:
        print('No such word!')
    

# 修改单词菜单
def change_menu():
    
    # 输入英文单词
    en = input('Please input the English word: ')
    
    # 查询单词是否存在
    exist_query = word_manage.exist(en)
    if not exist_query[0]: # 查询成功
        if exist_query[1]:# 如果存在，询问是否修改
            zh = input_zh(en, True)
            result = word_manage.change(en, zh)
            if result == None:
                print('Change successfully!')
            else:
                print('Change failed: ', result)
        else:# 如果不存在，询问是否添加
            print('No such word!')
            choice = input('Add this word (Y/N)? ')
            if choice == 'Y' or choice == 'y':
                add_menu(en)
            else:
                change_menu()
    else: # 查询失败
        change_menu()


# 展示单词菜单
def print_menu():
    result = word_manage.get_all()
    word_dict = result[1]
    if word_dict:
        # 逐个打印
        for word in word_dict:
            print(word, ' : ', word_dict[word])
    else:
        print('Error occured: ', result[0])


# 输入中文菜单
def input_zh(en, enable_compare):
    choose_menu = '''
    1. Get translation from Youdao
    2. Input the translation manually
    '''
    if enable_compare:
        choose_menu += '''3. Compare Youdao and the database
    '''
    print(choose_menu)
    choice = input()
    if choice == '1':
        zh = youdao.translate(en)
        if zh[1]:
            return zh[1]
        else:
            print('Failed to get translation from Youdao: ', zh[0])
            return input_zh(en, enable_compare)
    elif choice == '2':
        zh = input('Please input the new Chinese translation: ')
        return zh
    elif choice == '3' and enable_compare:
        youdao_zh = youdao.translate(en)
        if youdao_zh[1]:
            print('The Chinese translation from Youdao is: ' + youdao_zh[1])
            db_zh = word_manage.search(en)
            if not db_zh[0]:
                print('The Chinese translation from the database is: ' + db_zh[1])
            else:
                print('Error occured: ', db_zh[0])
                return input_zh(en, enable_compare)
            choice = input('Use the translation from Youdao (Y/N)? ')
            if choice == 'Y' or choice == 'y':
                return youdao_zh[1]
            else:
                return input_zh(en, enable_compare)
        else:
            print('Failed to get translation from Youdao: ', youdao_zh[0])
            return input_zh(en, enable_compare)
    else:
        print('Invalid input!')
        return input_zh(en, enable_compare)


# 导入文件菜单
def import_menu(file_type):
    
    # 输入文件位置
    if file_type == 'csv':
        file = input('Please input the file path (example: D:\\folder\\words.csv) (col1: word, col2: meaning): ')
    elif file_type == 'json':
        file = input('Please input the file path (example: D:\\folder\\words.json) (key: word, value: meaning): ')
    else:
        print('Invalid file type: ' + file_type + '!')
        return
    while not os.path.isfile(file):
        print('No such file!')
        file = input('Please input the file path (example: D:\\folder\\words.csv/json): ')
    
    # 输入文件编码方式
    codec = input('Please input the file codec (example: utf-8, gbk): ')

    # 输入处理重复单词的方式
    while True:
        choice = input('Overwrite duplicate words? (Y/N): ')
        if choice == 'Y' or choice == 'y':
            overwrite = True
            break
        elif choice == 'N' or choice == 'n':
            overwrite = False
            break
        else:
            print('Invalid input!')
    
    # 调用导入文件函数
    if file_type == 'csv':
        import_result = import_file.csv_import(file, codec, overwrite)
    elif file_type == 'json':
        import_result = import_file.json_import(file, codec, overwrite)
    else:
        print('Invalid file type: ' + file_type + '!')
        return
    
    # 显示导入结果
    if import_result == None:
        print('Import successfully!')
    else:
        print('Import failed: ', import_result)
