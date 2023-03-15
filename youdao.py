#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import requests

def translate(en):
    request_url = 'http://fanyi.youdao.com/translate'
    form_data = {}
    form_data['i'] = en
    form_data['doctype'] = 'json'
    form_data['type'] = 'EN2ZH_CN'
    try:
        r = requests.post(request_url, data=form_data)
    except Exception as e:
        print('Error when translating: ', e)
        return None
    finally:
        r.close()
    result = json.loads(r.text)
    if not result['translateResult']:
        return None
    else:
        return result['translateResult'][0][0]['tgt']
