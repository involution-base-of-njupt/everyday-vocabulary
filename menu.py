#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import recite_words
import word_manage
import youdao

# 管理员菜单
def admin_menu():
    print('''
    1. Add a word
    2. Delete a word
    3. Change a word
    4. Search a word
    5. Print wordlist
    6. Exit
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
        exit()
    else:
        print('Invalid input!')
        user_menu()

# 添加单词菜单
def add_menu():
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
        add_menu()

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
    en = input('Please input the English word: ')
    exist_query = word_manage.exist(en)
    if exist_query[0]:
        if exist_query[1]:
            zh = input_zh(en, True)
            if word_manage.change(en, zh):
                print('Change successfully!')
            else:
                print('Change failed!')
        else:
            print('No such word!')
            choice = input('Add this word? (Y/N)')
            if choice == ('Y' or 'y'):
                add_menu()
            else:
                change_menu()
    else:
        change_menu()

# 展示单词菜单
def print_menu():
    print(word_manage.get_all())

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
    