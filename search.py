import ipaddress
import json
import sys

import requests
from requests import exceptions

'''
def baidu_search(ip):
    # 使用百度API进行查询，无城市信息
    se_url = "https://qifu-api.baidubce.com/ip/geo/v1/district?"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Host": "qifu-api.baidubce.com",
        "Origin": "https://www.baidu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }
    params = {
        "ip": ip
    }
    res = requests.get(url=se_url, headers=headers, params=params)
    res = json.loads(res.text)
    # print(type(res))
    print(res)
    if 'Success' in res['code']:
        print("查询成功\n")
        print("--------------------\n")
        print(ip + '\n' + "归属地:", res['data']['country'] + res['data']['prov'] + '\t' + 'IPS:' + res['data']['isp'])
    else:
        print("查询失败")

'''


def al_search(ip):
    # 使用AL_API进行查询，可以返回城市信息
    url = "https://v2.alapi.cn/api/ip"
    token = "" # ALAPI的token
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }
    payload = {
        "token": token,
        "ip": ip
    }
    try:
        res = requests.post(url=url, data=payload, headers=headers)
        # print(res.text)
        res = json.loads(res.text)
        if res['code'] == 200 and 'success' in res['msg']:
            print('查询成功')
            print('-------------')
            print(ip + '\n' + '归属地:' + res['data']['pos'] + '\tisp:' + res['data']['isp'])
        else:
            print('没有找到信息')

    except exceptions.RequestException:
        print("API请求失败")


def my_ip():
    # 查询自己的ip地址
    url = 'http://myip.ipip.net/'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }
    res = requests.get(url=url,headers=headers)
    print(res.text)


def is_valid_ipv4_address(ip_address):
    # IPv4 地址判断
    try:
        ip_obj = ipaddress.IPv4Address(ip_address)
        if ip_obj.is_global:   # 判断是否为公网IP
            return True
        else:
            print(f'{ip_obj}是局域网IP')

    except ipaddress.AddressValueError:
        print('IP地址不正确')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('需要携带IP地址')
    else:
        ip = str(sys.argv[1])
        if is_valid_ipv4_address(ip) is True:
            # baidu_search(ip)
            my_ip()
            al_search(ip)
        else:
            my_ip()
