# -*- coding: utf-8 -*-
import re
import requests
import time
from common.logs import apilog

def Time():
    tim = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return tim

def GetHttp(url, requests_data):
    try:
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data=requests_data,headers=headers)
        #print(req.status_code)

        # print(r.headers)
        # print(r.text)
        # print(r.json())
        #print(float(r.elapsed.microseconds) / 1000)

    except Exception as err:
        return (err)
    if req.status_code == 200:
        apilog().info(u"发送post请求: %s  服务器返回:  %s\n info: %s " % (req.url, req.status_code, req.text))
    else:
        apilog().error(u"发送post请求: %s   服务器返回:  %s\n error info: %s " % (req.url, req.status_code, req.text))
    return req


