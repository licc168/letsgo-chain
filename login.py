# -*- coding: UTF-8 -*-
#!/usr/bin/python
import time
import requests
import config
import re

def login():
    return set_sessions()


def set_sessions():
    time.sleep(10)
    request = requests.Session()
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    request.headers.update(headers)
    cookies = config.cookies
    cooklist = re.split("; ",cookies)
    for cookie in cooklist:
        cookie1 = re.split("=",cookie)
        request.cookies.set(cookie1[0], cookie1[1])


    return request




# 验证登录是否成功  看看个人中心页面就知道啦
# def isSuccess():
#     request = login(config.username,config,password)
#     html_index = request.get('http://i.baidu.com/')
#     with open("tieba.html", 'wb') as f:
#         f.write(html_index.content)
#         f.close()
