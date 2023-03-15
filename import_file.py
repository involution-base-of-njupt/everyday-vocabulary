#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import json
import word_manage

# csv文件转json文件
def csv2json(csv_file, json_file):
    try:
        f = open(csv_file, 'r', newline='',encoding='utf-8')
        reader = csv.reader(f)
        if reader == None:
            return False
        json_data = {}
        for row in reader:
            json_data[row[0]] = row[1]
        f = open(json_file, 'w', encoding='utf-8')
        json.dump(json_data, f, indent=4)
        return True
    except Exception as e:
        print('Error when converting csv to json: ', e)
        return False
    finally:
        f.close()

# 导入CSV文件
def csv_import(file, mode):
    try:
        f = open(file, 'r', newline='',encoding='utf-8')
        reader = csv.reader(f)
        if reader == None:
            return False
        for row in reader:
            word_manage.add(row[0], row[1], mode)
        return True
    except Exception as e:
        print('Error when importing csv file: ', e)
        return False
    finally:
        f.close()

# 导入JSON文件
def json_import(file, mode):
    try:
        f = open(file, 'r', newline='',encoding='utf-8')
        reader = csv.reader(f)
        if reader == None:
            return False
        for row in reader:
            word_manage.add(row[0], row[1], mode)
        return True
    except Exception as e:
        print('Error when importing csv file: ', e)
        return False
    finally:
        f.close()
