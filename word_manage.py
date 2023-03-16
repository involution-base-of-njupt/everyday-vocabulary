#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 单词管理模块
# 命令行交互和图形界面都用

import json

word_file = 'words.json'
codec = 'utf-8'

# 检查单词是否存在，返回两个值，第一个值表示发生的错误，第二个值表示单词是否存在
def exist(en):
    f = None
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        word_dict = json.load(f)
        if en in word_dict:
            return None, True
        else:
            return None, False
    except Exception as e:
        print('Error when checking word: ', e)
        return e, None
    finally:
        if f:
            f.close()

# 写入单词，传入的 overwrite 参数表示是否覆盖已有的单词（默认覆盖），返回值为发生的错误和是否发生了覆盖
def write(en, zh, overwrite=True):
    f = None
    try:
        f = open(word_file, 'a', newline='', encoding=codec)
        word_dict = json.load(f)
        if en in word_dict:
            if overwrite:
                word_dict[en] = zh
                f.seek(0)
                json.dump(word_dict, f, indent=4)
                return None, True
            else:
                return None, False
        else:
            word_dict[en] = zh
            f.seek(0)
            json.dump(word_dict, f, indent=4)
            return None, False
    except Exception as e:
        print('Error when writing word: ', e)
        return e, None
    finally:
        if f:
            f.close()

# 添加单词，与写入单词功能相同，但如果单词存在会报错
def add(en, zh):
    if exist(en)[1]:
        return write(en, zh)
    else:
        print('This word already exists!')
        return 'WordExistError', False

# 删除单词，传入英文，返回值为发生的错误
def delete(en):
    if exist(en):
        f = None
        try:
            f = open(word_file, newline='', encoding=codec)
            word_dict = json.load(f)
            del word_dict[en]
            return None
        except Exception as e:
            print('Error when deleting word: ', e)
            return e
        finally:
            if f:
                f.close()
    else:
        return 'WordExistError'

# 搜索单词，返回两个值，第一个是发生的错误，第二个是中文意思
def search(en):
    f = None
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        word_dict = json.load(f)
        if en in word_dict:
            return None, word_dict[en]
        else:
            return 'WordNotExistError'
    except Exception as e:
        print('Error when checking word!')
        return e
    finally:
        if f:
            f.close()

# 修改单词，传入英文和中文，返回值为发生的错误
def change(en,zh):
    f = None
    try:
        f = open(word_file, 'r+', newline='', encoding=codec)
        word_dict = json.load(f)
        word_dict[en] = zh
        return None
    except Exception as e:
        print('Error when checking word: ', e)
        return e
    finally:
        if f:
            f.close()

# 获取所有单词，返回是否发生错误和获取的字典
def get_all():
    f = None
    try:
        f = open(word_file, 'r', newline='', encoding=codec)
        return None, json.load(f)
    except Exception as e:
        print('Error when getting word dict: ', e)
        return e, None
    finally:
        if f:
            f.close()
