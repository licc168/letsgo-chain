#!/usr/bin/python
# -*- coding: UTF-8 -*-
username = '111111'
password = '1111'

# 0:手动刷狗 1：自动刷狗接入第三方接口平台
type=1

# 0:开启微信助手提醒 1：关闭微信信息提醒
sendMsg=0

# 默认微信文件助手
toUserName = "filehelper"


'''
key：等级 0-4依次（普通-稀有-卓越-史诗-神话）
value：最大价格
'''
rares = {0:10000,1:100,2:300,3:500,4:1000}


# 狗狗详情页面
urlDetail = "https://pet-chain.baidu.com/chain/detail?channel=market&petId="

'''
第三方接口 

'''
apiurl = 'https://route.showapi.com/184-5'

showapi_appid="56415"  #替换此值

showapi_sign="111111"   #替换此值









