#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv

word_file = 'words.csv'
codec = 'utf-8'

# 检查单词是否存在
def exist(en):
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        reader = csv.reader(f)
        for row in reader:
            if row[0] == en:
                return True
        return False
    except:
        print('Error when checking word!')
        return False
    finally:
        f.close()

# 写入新的单词
def write_word(en, zh):
    try:
        f = open(word_file, 'a', newline='', encoding=codec)
        writer = csv.writer(f)
        writer.writerow([en, zh])
        return True
    except:
        print('Error when writing word!')
        return False
    finally:
        f.close

# 添加单词
def add(en, zh):
    if not exist(en):
        if write_word(en, zh):
            return True
        else:
            return False
    else:
        return False

# 删除单词
def delete(en):
    if exist(en):
        try:
            f = open(word_file, newline='', encoding=codec)
            reader = csv.reader(f)
            if reader == None:
                return False
            for row in reader:
                if row[0] == en:
                    reader.remove(row)
                    writer = csv.writer(f)
                    writer.writerows(reader)
                    return True
        except:
            print('Error when deleting word!')
            return False
        finally:
            f.close()
    else:
        return False

# 搜索单词
def search(en):
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        reader = csv.reader(f)
        for row in reader:
            if row[0] == en:
                return True, row[1]
        return False, None
    except:
        print('Error!')
        return False, None
    finally:
        f.close()    
# 修改单词
def change(en,zh):
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        reader = csv.reader(f)
        if reader == None:
            return False
        for row in reader:
            if row[0] == en:
                row[1] = zh
                writer = csv.writer(f)
                writer.writerows(reader)
                return True
    except:
        print('Error!')
        return False

# 获取所有单词，返回字典
def get_all():
    wordlist = {}
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        reader = csv.reader(f)
        for row in reader:
            wordlist[row[0]] = row[1]
        return wordlist
    except:
        print('Error!')
        return None
    finally:
        f.close()

