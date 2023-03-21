#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import os

wrong_words_file = 'wrong_words.json'
codec = 'utf-8'

# 添加错英文词，传入英文单词（str），正确答案（str），错误答案列表（list），返回值是发生的错误
def add_wrong_en_word(en, correct_answer = '', wrong_answers = ()):
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            word_dict = {'en':{}}
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
        en_wong_word = word_dict['en'].setdefault(en, {})
        # 错误次数
        if 'wrong_times' in en_wong_word:
            en_wong_word['wrong_times'] += 1
        else:
            en_wong_word['wrong_times'] = 1
        # 正确答案
        if correct_answer == '':
            en_wong_word['correct_answer'] = correct_answer
        # 错误答案
        if 'wrong_answers' in en_wong_word:
            en_wong_word['wrong_answers'] += wrong_answers
        else:
            en_wong_word['wrong_answers'] = wrong_answers
        en_wong_word['wrong_answers'] = list(set(en_wong_word['wrong_answers'])) # 去重
        f = open(wrong_words_file, 'w', newline='', encoding=codec)
        json.dump(word_dict, f, ensure_ascii=False, indent=4)
        return None
    except Exception as e:
        return e
    finally:
        if f:
            f.close()


# 添加错中文词，传入中文单词（str），正确答案（str），返回值是发生的错误
def add_wrong_zh_word(zh, correct_answer = ''):
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            word_dict = {'zh':{}}
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
            zh_wong_word = word_dict.setdefault('zh', {}).setdefault(zh, {})
        # 错误次数
        if 'wrong_times' in zh_wong_word:
            zh_wong_word['wrong_times'] += 1
        else:
            zh_wong_word['wrong_times'] = 1
        if correct_answer == '':
            zh_wong_word['correct_answer'] = correct_answer
        f = open(wrong_words_file, 'w', newline='', encoding=codec)
        json.dump(word_dict, f, ensure_ascii=False, indent=4)
        return None
    except Exception as e:
        return e
    finally:
        if f:
            f.close()


# 读取错英文词，传入单词，返回发生错误、错词次数、正确答案、错误答案
def read_wrong_en_word(en):
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            return '找不到该词', 0, '', []
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
            wrong_en_word = word_dict['en'][en]
        return None, wrong_en_word['wrong_times'], wrong_en_word['correct_answer'], wrong_en_word['wrong_answers']
    except Exception as e:
        return e, 0, '', []
    finally:
        if f:
            f.close()


# 读取错中文词，传入单词，返回发生错误、错词次数、正确答案
def read_wrong_zh_word(zh):
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            return '找不到该词', 0, ''
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
            wrong_zh_word = word_dict['zh'][zh]
        return None, wrong_zh_word['wrong_times'], wrong_zh_word['correct_answer']
    except Exception as e:
        return e, 0, ''
    finally:
        if f:
            f.close()


# 搜索错中文词，传入关键词，返回发生错误、可能匹配的错中文词列表
def search_wrong_zh_word(keyword):
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            return '找不到该词', {}
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
            zh_list = []
            for zh in word_dict['zh']:
                if keyword in zh:
                    zh_list += [zh]
        return None, zh_list
    except Exception as e:
        return e, []
    finally:
        if f:
            f.close()


# 删除错英文词，传入单词，返回发生错误
def delete_wrong_en_word(en):
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            return '找不到该词'
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
            wrong_en_words = word_dict['en']
            del wrong_en_words[en]
            f = open(wrong_words_file, 'w', newline='', encoding=codec)
            json.dump(word_dict, f, ensure_ascii=False, indent=4)
            return None
    except Exception as e:
        return e
    finally:
        if f:
            f.close()


# 删除错中文词，传入单词，返回发生错误
def delete_wrong_zh_word(zh):
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            return '找不到该词'
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
            wrong_zh_words = word_dict['zh']
            del wrong_zh_words[zh]
            f = open(wrong_words_file, 'w', newline='', encoding=codec)
            json.dump(word_dict, f, ensure_ascii=False, indent=4)
            return None
    except Exception as e:
        return e
    finally:
        if f:
            f.close()



# 获取所有错英文词，返回值是发生的错误、错词字典（key:单词，value:次数）
def get_all_wrong_en_words():
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            return None, None
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
            en_wong_words = word_dict['en']
            result = {}
            for en in en_wong_words:
                result[en] = en_wong_words[en]['wrong_times']
            return None, result
    except Exception as e:
        return e, {}


# 获取所有错中文词，返回值是发生的错误、错词字典（key:词，value:次数）
def get_all_wrong_zh_words():
    f = None
    try:
        if not os.path.isfile(wrong_words_file) or not os.path.getsize(wrong_words_file):
            return None
        else:
            f = open(wrong_words_file, 'r', newline='', encoding=codec)
            word_dict = json.load(f)
            zh_wrong_words = word_dict['zh']
            result = {}
            for zh in zh_wrong_words:
                result[zh] = zh_wrong_words[zh]['wrong_times']
            return None, result
    except Exception as e:
        return e, {}
