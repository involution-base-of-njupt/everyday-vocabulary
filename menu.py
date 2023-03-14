#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import recite_words

# 管理员菜单
def admin_menu():
    print('''
    1. Add a word
    2. Delete a word
    3. Change a word
    4. Search a word
    5. Show words
    6. Exit
    ''')
    choice = input('Please input your choice: ')
    if choice == '1':
        add_word()
    elif choice == '2':
        delete_word()
    elif choice == '3':
        change_word()
    elif choice == '4':
        search_word()
    elif choice == '5':
        show_word()
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
        search_word()
    elif choice == '2':
        show_word()
    elif choice == '3':
        recite_words.chinese_translate_english()
    elif choice == '4':
        recite_words.english_translate_chinese()
    elif choice == '5':
        exit()
    else:
        print('Invalid input!')
        user_menu()