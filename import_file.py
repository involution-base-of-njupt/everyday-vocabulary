#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import json
import word_manage

# csv文件转json文件，返回值是发生的错误
def csv2json(csv_file, json_file, codec):
    f = None
    try:
        f = open(csv_file, 'r', newline='',encoding=codec)
        reader = csv.reader(f)
        json_data = {}
        for row in reader:
            json_data[row[0]] = row[1]
        f = open(json_file, 'w', encoding=codec)
        json.dump(json_data, f, indent=4)
        return None
    except Exception as e:
        print('Error when converting csv to json: ', e)
        return e
    finally:
        if f:
            f.close()

# 导入CSV文件，返回值是发生的错误
def csv_import(file, codec, mode):
    f = None
    try:
        f = open(file, 'r', newline='',encoding=codec)
        reader = csv.reader(f)
        for row in reader:
            word_manage.add(row[0], row[1], mode)
        return None
    except Exception as e:
        print('Error when importing csv file: ', e)
        return e
    finally:
        if f:
            f.close()

# 导入JSON文件，返回值是发生的错误
def json_import(file, codec, overwrite):
    try:
        f = open(file, 'r', newline='',encoding=codec)
        word_dict = json.load(f)
        for en in word_dict:
            word_manage.add(en, word_dict[en], overwrite)
        return None
    except Exception as e:
        print('Error when importing json file: ', e)
        return e
    finally:
        f.close()
