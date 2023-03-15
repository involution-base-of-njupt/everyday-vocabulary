#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json

word_file = 'words.json'
codec = 'utf-8'

# 检查单词是否存在，返回两个值，第一个值表示是否查询成功，第二个值表示单词是否存在
def exist(en):
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        word_dict = json.load(f)
        if en in word_dict:
            return True, True
        else:
            return False
    except Exception as e:
        print('Error when checking word: ', e)
        return False
    finally:
        f.close()

# 写入新的单词，传入的 mode 参数表示是否覆盖已有的单词，mode=1 表示覆盖（默认），mode=2 表示跳过
def write(en, zh, mode='1'):
    try:
        f = open(word_file, 'a', newline='', encoding=codec)
        word_dict = json.load(f)
        if en in word_dict:
            if mode == '1':
                word_dict[en] = zh
                f.seek(0)
                json.dump(word_dict, f, indent=4)
                return True
            elif mode == '2':
                return True
            else:
                print('Error when writing word: mode error!')
                return False
        return True
    except Exception as e:
        print('Error when writing word: ', e)
        return False
    finally:
        f.close()

# 添加单词
def add(en, zh):
    return write(en, zh)

# 删除单词
def delete(en):
    if exist(en):
        try:
            f = open(word_file, newline='', encoding=codec)
            word_dict = json.load(f)
            del word_dict[en]
            return True
        except Exception as e:
            print('Error when deleting word: ', e)
            return False
        finally:
            f.close()
    else:
        return False

# 搜索单词，返回两个值，第一个是是否找到，第二个是中文意思
def search(en):
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        word_dict = json.load(f)
        if en in word_dict:
            return True, word_dict[en]
        else:
            return False
    except Exception as e:
        print('Error when checking word!')
        return False
    finally:
        f.close()

# 修改单词，传入英文和中文，返回值为是否成功
def change(en,zh):
    try:
        f = open(word_file, 'r+', newline='', encoding=codec)
        word_dict = json.load(f)
        if en in word_dict:
            return True, word_dict[en]
        else:
            return False
    except Exception as e:
        print('Error when checking word: ', e)
        return False

# 获取所有单词，返回字典
def get_all():
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        return json.load(f)
    except Exception as e:
        print('Error when getting word dict: ', e)
        return None
    finally:
        f.close()
