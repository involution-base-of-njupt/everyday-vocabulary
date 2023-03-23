#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
from requests import post

# 有道翻译，返回值为发生的错误和翻译结果
def translate(en):
    request_url = 'http://fanyi.youdao.com/translate'
    form_data = {}
    form_data['i'] = en
    form_data['doctype'] = 'json'
    form_data['type'] = 'EN2ZH_CN'
    r = None
    try:
        r = post(request_url, data=form_data)
    except Exception as e:
        return e, None
    finally:
        if r:
            r.close()
    result = json.loads(r.text)
    if not result['translateResult']:
        return '有道翻译错误', None
    else:
        return None, result['translateResult'][0][0]['tgt']
