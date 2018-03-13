# -*- coding:utf8 -*-
import base64
import datetime
import json
import re
import time
from io import BytesIO

import itchat
import numpy as np
import requests
from PIL import Image
from fake_useragent import UserAgent

import tf_code
import common
import config
import redisClient

ua = UserAgent()
'''
获取数据接口
'''
headers = {'content-type': 'application/json'}
proxies = { }


'''
根据分页以及排序查询狗狗列表
Args;
    pageNo:页号
    pageSize：每页条数
    querySortType:金额
    
Returns: 
    data：狗狗列表
Raises:
    BusinessException 
'''
def queryMarketData(pageNo,pageSize,querySortType,proxies):

    try:
        data ={
            "appId": 1,
            "lastAmount":None,
            "lastRareDegree":None,
            "pageNo": pageNo,
            "pageSize": pageSize,
            "petIds": [],
            "querySortType": querySortType,
            "tpl":"",
            "requestId":time.time()
        }
       # print(data)
        headers['User-Agent'] = ua.random
        s =  requests.post("https://pet-chain.baidu.com/data/market/queryPetsOnSale",proxies = proxies,data=json.dumps(data), headers=headers,timeout=10)
    except:
        raise BusinessException("查詢服务器异常")
    status =  s.status_code
    if status==200:
        res = json.loads(s.content)
        msg = res["errorMsg"]
        if msg == "success":
            data = res["data"]["petsOnSale"]
            return data

        else:
            raise BusinessException("查詢接口获取错误")
    else:
        raise BusinessException("查詢接口获取错误"+str(status))
'''
下单接口
Args;
    request
    petId
    pet_amount:金额
    pet_validCode:验证码
Returns: 
    code:返回状态  msg：信息
Raises:
    BusinessException 
'''
def purchase(request,petId,pet_amount,pet_validCode):
    try:

        data = {
            "appId":1,
            "petId":petId,
            "requestId":time.time(),
            "tpl":"",
            "amount":"{}".format(pet_amount),
            "validCode": pet_validCode
        }
        # seed, captcha =  get_captcha(request)
        # seed = str(redisClient.getSeed())
        # captcha = str(redisClient.getCode())
        # if seed == None:
        seed, captcha = get_captcha(request)
        data['captcha'] = captcha
        data['seed'] = seed

        proxies['http'] = redisClient.getProxyIp()
        res = request.post("https://pet-chain.baidu.com/data/txn/create",proxies = proxies,headers=headers, data=json.dumps(data), timeout=6)
        res = json.loads(res.content)
        code = res['errorNo']
        msg = res['errorMsg']

        return  code,msg,captcha
    except Exception as e:
        raise BusinessException(e)

'''
验证码接口
Args;
    request
Returns: 
    seed:  captcha：验证码
Raises:
    BusinessException 

'''
def get_captcha(request):
    seed = -1
    captcha = -1
    data = {
        "requestId": int(time.time() * 1000),
        "appId": 1,
        "tpl": ""
    }
    try:
        headers['User-Agent'] = ua.random
        proxies['http'] = redisClient.getProxyIp()
        page = request.post("https://pet-chain.baidu.com/data/captcha/gen", data=json.dumps(data),proxies=proxies,
                             headers=headers)
        res = json.loads(page.content)
        msg = res["errorMsg"]
        if msg == "success":
            img = res["data"]["img"]
            seed = res["data"]["seed"]
            image = decode_img(img_base64=img)
            captcha = tf_code.getCode(image)
        else:
            raise BusinessException("获取验证码图片异常")
    except Exception as e:
        raise BusinessException(e)
    return seed, captcha












'''
获取代理IP，判断代理IP是否有效，如果有效则设置代理IP
Args;
    无
Returns: 
    True:代理IP有效  False：代理IP无效
Raises:
    BusinessException 

'''
def setProxies():
    try:
        proxyips = redisClient.getProxyData()
        for ip, status in proxyips.items():
            ip = str(ip,"utf-8")
            if common.isUseIp(ip):
                print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"  有效代理:"+ip)
                redisClient.setPorxyIp(ip)
            else:
                #删除代理
                redisClient.deleteProxyData(ip)

    except Exception as e:
        raise BusinessException("代理IP获取异常，请检查接口是否配对")






# '''
# 易源数据验证码接口
# Args;
#     imgBase64 验证码图片base64信息
# Returns:
#     验证码
# Raises:
#     BusinessException
# '''
# def getValidCode(imgBase64):
#     showapi_appid,showapi_sign = redisClient.getCodeApi()
#     send_data = parse.urlencode([
#         ('showapi_appid', showapi_appid)
#         , ('showapi_sign', showapi_sign)
#         , ('img_base64', imgBase64)
#         , ('typeId', 34)
#         , ('convert_to_jpg', 0)
#
#     ])
#     for i in range(1,10):
#         req = request.Request('https://route.showapi.com/184-5')
#         try:
#             response = request.urlopen(req, data=send_data.encode('utf-8'), timeout=10)  # 10秒超时反馈
#             result = response.read().decode('utf-8')
#             result_json = json.loads(result)
#             print('result_json data is:', result_json)
#
#             if result_json["showapi_res_code"] == 0:
#                 redisClient.setImg(imgBase64)
#                 return result_json["showapi_res_body"]["Result"]
#             if result_json["showapi_res_code"] == -2:
#                 redisClient.delApiKey(showapi_appid)
#             else:
#                 raise BusinessException("第三方接口错误")
#             break
#         except Exception as e:
#             print("第三方接口服务器异常")



'''
将图片转化为向量形式
'''
def decode_img(img_base64):
    imgage = Image.open(BytesIO(base64.b64decode(img_base64)))
    try:
        image = np.array(imgage,dtype=np.uint8)
        return image
    except:
        image = np.array(imgage, dtype=np.float)
        return  image




'''
组合查询出来的狗狗分页列表
Args;
    paixu 排序
    pageNum 页数
    proxyIp 代理IP
Returns: 
    狗狗信息列表
'''

def queryData(paixu,pageNum,proxyIp):
    datas=[]
    for num in range(1,pageNum):

        data = queryMarketData(num, 10, paixu,proxyIp)
        datas = datas+data

    return datas




'''
根据petId查询狗狗的详情信息
Args;
    petId 狗狗ID
Returns: 
    体型,眼睛,嘴巴,几稀
Raises:
    BusinessException    
'''
def getLetGoDetail(petId):
    data = {
        "appId": 1,
        "petId":petId,
        "nounce": None,
        "timeStamp": None,
        "token":None,
        "tpl": "",
        "requestId": time.time()
    }
    headers['User-Agent'] = ua.random
    try:
        s = requests.post("https://pet-chain.baidu.com/data/pet/queryPetById", data=json.dumps(data),
                          headers=headers, timeout=10)
        res = json.loads(s.content)
        errorNo = res['errorNo']
        count = 0
        if errorNo == '00':
            id = res['data']['id']
            attributesArray = res['data']['attributes']

            # 体型
            body=attributesArray[0]['value']
            #眼睛
            eye = attributesArray[2]['value']
            #嘴巴
            mouth = attributesArray[4]['value']
            #几稀
            for atr in attributesArray:
                rareDegree = atr['rareDegree']
                if(rareDegree=="稀有"):
                   count =  count+1

            return id, body,eye,mouth,count

        else:
            raise  BusinessException("狗狗详情解析错误")
    except Exception as e:
        raise BusinessException("狗狗详情接口异常")

'''
打印信息
Args;
    body:体型   
    eye:眼睛  
    mouth:嘴巴 
    rareDegree 级别
    amount 金额
    count 几稀
    buyUrL:购买链接

'''
def printMsg(body,eye,mouth,rareDegree,amount,count,buyUrl):
    msg = body + ":" + eye + " " + mouth + "  " + config.rareDegrees[rareDegree] + " " + str(
        amount / 10000) + "万 " + str(count) + " " + buyUrl
    print(msg)
    if config.sendMsg==0:
        itchat.send(msg, toUserName=config.toUserName)



'''
下单 如果验证码出错则重试100次直到成功
Args;
    request:   
    petid:  
    amount:金额 
    rareDegree 等级
    validCode 验证码
'''
def purchaseSubmit(request,petid,amount,rareDegree,validCode):
    if config.type == 1:
        count = 0
        while count < 8:
            code, msg, captcha = purchase(request, petid, amount, validCode)
            #存储图片作为样本
            #saveImage(code, captcha)
            if msg=='success':
                redisClient.setBuySuccess(config.username+"  "+config.rareDegrees[rareDegree] )

            if config.sendMsg == 0:
                itchat.send(config.rareDegrees[rareDegree] + " " + str(amount) + "  " + msg, toUserName=config.toUserName)
            else:
                print(config.rareDegrees[rareDegree] + " " + str(amount) + "  " + msg)
                # 如果是验证码错误则重新买
            if code != '100':
                break
            else:
                count = count + 1
                continue
'''
判断是否是靓号
args：
    id
return：x y
     x：代表位数  
     y：代表是否是同一数字
    
    
'''
def getLiangHao(id):
    x=8
    y=0 #默认不是
    if re.match(r'0{1}[1-9]{7}',id,re.I):
        x =7
    if re.match(r'0{2}[1-9]{6}', id, re.I):
        x =6
    if re.match(r'0{3}[1-9]{5}', id, re.I):
        x =5
    if re.match(r'0{4}[1-9]{4}',id,re.I):
        x =4
    if re.match(r'0{5}[1-9]{3}',id,re.I):
        x = 3
    if re.match(r'0{6}[1-9]{2}',id,re.I):
        x = 2
    if re.match(r'0{7}[1-9]{1}',id,re.I):
        x = 1

    if x==8 and re.match(r"(.)\1{7}",id,re.I):
        y = 1
        return  x,y
    if x==7 and re.match(r"\d{1}(.)\1{6}",id,re.I):
        y = 1
        return x, y
    if x==6 and re.match(r"\d{2}(.)\1{5}",id,re.I):
        y = 1
    if x==5 and re.match(r"\d{3}(.)\1{4}",id,re.I):
        y = 1
        return x, y
    if x==4 and re.match(r"\d{4}(.)\1{3}",id,re.I):
        y = 1
        return x, y
    if x==3 and re.match(r"\d{5}(.)\1{2}",id,re.I):
        y = 1
        return x, y
    if x==2 and re.match(r"\d{6}(.)\1{1}",id,re.I):
        y = 1
        return x, y
    if x==1:
        y = 1
        return x, y

    return  x,y


'''
将图片提取出来作为样本

'''

def saveImage(code,captcha):
    if code == "10002" or code=='00':
        img = redisClient.getImg()
        imagedata = base64.b64decode(img)

        print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + captcha )

        file = open("D:/img_code/" + captcha + ".jpg", "wb")
        file.write(imagedata)
        file.close()



#自定义异常
class BusinessException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


'''
找出ID中的最长连续数字

'''
def lixushuzi(pid):
    count = 0
    ids = list(pid)
    tempId = ids[0]
    legth = len(ids)
    tempCount = 0
    for num in range(0,legth):
        id = ids[num]
        if tempId == id:
            count = count+1
        else:
            if tempCount<count:
                tempCount = count
            count = 1
        if num == legth-1:
            if tempCount<count:
                tempCount = count

        tempId = id
    return  tempCount

