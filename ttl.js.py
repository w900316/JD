# -*- coding: utf-8 -*- 
"""
Project: SHGT.py
Creator: carlo
Create time: 2021-12-23 11:08
IDE: PyCharm
Introduction:
"""
import argparse
import json
import time

import requests


def get_headers(host='www.ttljf.com', referer='', user_agent=''):
    headers = {
        "User-Agent": user_agent,
        "Host": host,
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "Accept-Language": "en-CN;q=1, zh-Hans-CN;q=0.9",
        "Accept-Encoding": "gzip, deflate"
        # "Referer": referer
    }
    return headers


def sign_in(username='', password=''):
    t = int(time.time())
    url = 'https://www.ttljf.com/ttl_site/user.do'
    post_data = 'username={}&password={}&device_brand=apple&device_model=iPhone11,8&device_uuid=&device_version=13.5&mthd=login&platform=ios&sign='.format(
        username, password)
    headers = get_headers(user_agent="otole/1.4.8 (iPhone; iOS 13.5; Scale/2.00)")
    response = requests.post(url, data=post_data, timeout=(2, 2), headers=headers)
    data = json.loads(response.text)
    token = data['user']['loginToken']
    print(data)
    print(token)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--username', type=str, default=None)
    parser.add_argument('--password', type=str, default=None)
    args = parser.parse_args()
    print(args.username)
    print(args.password)
    # exit()
    sign_in(args.username, args.password)
