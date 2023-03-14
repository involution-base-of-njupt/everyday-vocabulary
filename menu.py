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
    while word_manage.exist(en):
        print('The word already exists!')
        en = input('Please input the English word: ')
    zh = input_zh(en)
    if word_manage.add(en, zh):
        print('Add successfully!')
    else:
        print('Add failed!')

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
    if word_manage.exist(en):
        zh = input_zh(en)
        if word_manage.change(en, zh):
            print('Change successfully!')
        else:
            print('Change failed!')
    else:
        print('No such word!')
        choice = input('Add this word? (Y/N)')
        if choice == 'Y' or 'y':
            add_menu()
        else:
            change_menu()

# 展示单词菜单
def print_menu():
    print(word_manage.get_all())

# 输入中文菜单
def input_zh(en):
    print('''
    1. Get translation from Youdao
    2. Input the translation manually
    ''')
    choice = input()
    if choice == '1':
        zh = youdao.translate(en)
        if zh:
            return zh
        else:
            print('Failed to get translation from Youdao!')
            input_zh()
    elif choice == '2':
        zh = input('Please input the new Chinese translation: ')
        return zh
    else:
        print('Invalid input!')
        input_zh(en)
