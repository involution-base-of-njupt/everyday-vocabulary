#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

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

def user_menu():
    print('''
    1. Search a word
    2. Show Words
    3. Exit
    ''')
    choice = input('Please input your choice: ')
    if choice == '1':
        search_word()
    elif choice == '2':
        show_word()
    elif choice == '3':
        exit()
    else:
        print('Invalid input!')
        user_menu()