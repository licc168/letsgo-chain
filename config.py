#!/usr/bin/python
# -*- coding: UTF-8 -*-
username = '111'
password = '111'


# username = '111'
# password = '111-'





# 0:手动刷狗 1：自动刷狗接入第三方接口平台
type=1

# 0:开启微信助手提醒 1：关闭微信信息提醒
sendMsg=1

# 默认微信文件助手
toUserName = "filehelper"


'''
key：等级 0-4依次（普通-稀有-卓越-史诗-神话-传说）
value：最大价格
'''
rares = {0:600,1:1000,2:3000,3:10000,4:100000,5:30000}
rareDegrees = {0:"普通",1:"稀有",2:"卓越",3:"史诗",4:"神话",5:"传说"}

# 狗狗详情页面
urlDetail = "https://pet-chain.baidu.com/chain/detail?channel=market&petId="

'''
云服务器接口 验证码接口

'''

# apiurl = 'http://47.94.196.111:8080/ocr'
apiurl = 'https://route.showapi.com/184-5'

showapi_appid="57734"  #替换此值

showapi_sign="8d509b00564647f3afd4363c8b5d4017"   #替换此值












