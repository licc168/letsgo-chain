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
        time.sleep(random.randint(1,2))
        # 设置代理
        if service.setProxies():
            try:
                #"AMOUNT_DESC"  CREATETIME_DESC
             data = service.queryData("AMOUNT_ASC")
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

                 if body=='天使' and (eye == "白眉斗眼") :
                     # 稀有+金额
                     if rareDegree == 1 and amount < 40000:
                         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)

                     # 卓越+金额
                     if rareDegree == 2 and amount < 50000:
                         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)

                     # 史诗+金额
                     if rareDegree==3 and amount<180000:
                         service.printMsg(body,eye,mouth,rareDegree,amount,count,buyUrl)

                     # 神话+金额
                     if rareDegree == 4 and amount < 2000000:
                         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)


                  #神话+金额
                 if  rareDegree>=4 and amount<=400000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)



                 if(amount<=config.rares[rareDegree]):
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     # 发送微信提醒
                     if config.sendMsg==0:
                         itchat.send("等级： " + str(rareDegree) + "价格：" + str(amount), toUserName=config.toUserName)
                         itchat.send(buyUrl, toUserName=config.toUserName)
                      #根据petid 缓存url 过期时间为30秒 刷过链接就不在刷了

                     # 下单
                     if config.type==1:

                         service.purchaseSubmit(request,petid,amount,rareDegree,validCode)

            except service.BusinessException as e:
                print(e.value)
                continue



main()