import service
import config
import itchat
import time
from cache import Cache
import random
import login








def main():
    # 开启微信助手提醒需要扫码登录
    if config.sendMsg ==0:
        itchat.auto_login()
    request = None
    # 自动刷狗则需要登录
    if config.type==1:
        request = login.login(config.username,config.password)
    cache =  Cache()
    while True:

        # 设置代理
        if service.setProxies():
            try:
                #"AMOUNT_DESC"  CREATETIME_DESC
             data = service.queryData("CREATETIME_DESC")
             for item in data:
                 #没猜错的话这个是等级  0-4
                 rareDegree = item["rareDegree"]
                 amount = float(item["amount"])
                 petid = item["petId"]
                 validCode = item["validCode"]
                 # 拼接购买链接
                 buyUrl = config.urlDetail + petid + "&validCode=" + validCode
                 if (buyUrl == cache.get(petid)):
                     continue
                 #缓存购买链接
                 cache.set(petid, buyUrl, 30)

                 #获取详情信息
                 body,eye,mouth,count =service.getLetGoDetail(petid)
                 #service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 if body=="天使" and count==5 and amount<70000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)

                 if body=='天使' and (eye == "白眉斗眼") :

                     # 稀有+金额
                     if rareDegree == 1 and amount < 40000:
                         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                         service.purchaseSubmit(request, petid, amount, rareDegree, validCode)

                     # 卓越+金额
                     if rareDegree == 2 and amount < 50000:
                         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                         service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                     # 史诗+金额
                     if rareDegree==3 and amount<160000:
                         service.printMsg(body,eye,mouth,rareDegree,amount,count,buyUrl)
                         service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                     if rareDegree == 3 and amount < 220000 and count==5:
                         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                         service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                     # 神话+金额
                     if rareDegree == 4 and amount < 2000000:
                         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                         service.purchaseSubmit(request, petid, amount, rareDegree, validCode)

                  #神话+金额
                 if  rareDegree>=4 and amount<=400000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)



                 if(amount<=config.rares[rareDegree]):
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     # 发送微信提醒
                     service.purchaseSubmit(request,petid,amount,rareDegree,validCode)

            except service.BusinessException as e:
                print(e.value)
                continue



main()