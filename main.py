#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import random
import csv
import account

dict_file = 'words.csv'

def main():
    print('Welcome to the English Dictionary!')
    if account.init():
        print('This is the first time you use this dictionary!\nDefault admin username: admin\nDefault admin password: admin')

main()