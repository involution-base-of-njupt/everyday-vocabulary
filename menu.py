#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import recite_words
import word_manage

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
    elif choice == '2':
        delete_menu()
    elif choice == '3':
        change_menu()
    elif choice == '4':
        search_menu()
    elif choice == '5':
        print_menu()
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
    elif choice == '2':
        show_menu()
    elif choice == '3':
        recite_words.chinese_translate_english()
    elif choice == '4':
        recite_words.english_translate_chinese()
    elif choice == '5':
        exit()
    else:
        print('Invalid input!')
        user_menu()

# 添加单词菜单
def add_menu():
    en = input('Please input the English word: ')
    zh = input('Please input the Chinese translation: ')
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
        print('The Chinese translation is: ' + zh)
    else:
        print('No such word!')
    
# 修改单词菜单
def change_menu():
    en = input('Please input the English word: ')
    zh = input('Please input the new Chinese translation: ')
    if word_manage.change(en, zh):
        print('Change successfully!')
    else:
        print('Change failed!')

# 展示单词菜单
def print_menu():
    print(word_manage.get_all())