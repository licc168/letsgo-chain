#!/usr/bin/python
# -*- coding: UTF-8 -*-
username = '1111'
password = '11111'
# username = '11'
# password = '1111'


# 0:手动刷狗 1：自动刷狗接入第三方接口平台
type=1

# 0:开启微信助手提醒 1：关闭微信信息提醒
sendMsg=0
# 默认微信文件助手
toUserName = "filehelper"


'''
key：等级 0-5依次（普通-稀有-卓越-史诗-神话-传说）
value：最大价格
'''
rares = {0:400,1:400,2:1000,3:10000,4:100000,5:30000}
rareDegrees = {0:"普通",1:"稀有",2:"卓越",3:"史诗",4:"神话",5:"传说"}



'''
云服务器接口 验证码接口
appid,sign 配置在redis里面了
'''


apiurl = 'https://route.showapi.com/184-5'













