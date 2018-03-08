import service
import config
import itchat
from cache import Cache
import login
import redisClient
import json



#letgo列表数据
data=[]

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

        try:
            #"AMOUNT_DESC"  CREATETIME_DESC
         data = redisClient.getLetsgoData()
         for item in data:
             item = json.loads(item)
             #没猜错的话这个是等级  0-4
             rareDegree = item["rareDegree"]
             amount = float(item["amount"])
             petid = item["petId"]
             validCode = item["validCode"]
             # 拼接购买链接
             buyUrl = "https://pet-chain.baidu.com/chain/detail?channel=market&petId=" + petid + "&validCode=" + validCode
             if (buyUrl == cache.get(petid)):
                 continue
             #缓存购买链接
             cache.set(petid, buyUrl, 300)

             #获取详情信息
             id,body,eye,mouth,count =service.getLetGoDetail(petid)
             #service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
             x, y = service.getLiangHao(id)


             '''
               判断是否是连续数字
            '''
             lixu = service.lixushuzi(id)
             if x==7 and lixu ==  4 and amount< 5000 :
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
             if  x==7 and lixu == 5 and amount<30000:
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
             if lixu == 6 and amount < 200000:
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
             if lixu == 7 and amount < 300000:
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
             if lixu == 8 and amount < 500000:
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
             '''
             判断是否是靓号-start 
            '''

             # 4位数靓号
             if(x==4 and amount< 100000 ):
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                 if y == 1 and  amount<200000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
             # 3位数靓号
             if (x == 3 and amount < 150000):
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                 if y == 1 and amount < 250000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
             # 2位数靓号
             if (x == 2 and amount < 300000):
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                 if y == 1 and amount < 500000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
             # 1位数靓号
             if (x == 1 and amount < 1000000):
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)

             '''
            根据属性匹配价格 
            '''
             # 卓越+天使
             if body == "天使" and eye=='小对眼' and rareDegree == 2 and amount <1000:
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
              #史诗+金额+5稀
             if body == "天使" and count == 5 and amount < 16000:
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 service.purchaseSubmit(request, petid, amount, rareDegree, validCode)

             if body=='天使' and (eye == "白眉斗眼") :



                 # 卓越+金额
                 if rareDegree == 2 and amount < 10000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                 if rareDegree == 2   and mouth == '樱桃' and  amount <100000 :
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)

                 # 史诗+金额
                 if rareDegree==3 and amount<60000:
                     service.printMsg(body,eye,mouth,rareDegree,amount,count,buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                 if rareDegree == 3 and mouth == '樱桃' and amount < 200000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                 if rareDegree == 3 and amount < 100000 and count==5:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                 if rareDegree == 3 and amount < 250000 and count==5 and mouth == '樱桃':
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
                 # 神话+金额
                 if rareDegree == 4 and amount < 800000:
                     service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                     service.purchaseSubmit(request, petid, amount, rareDegree, validCode)

              #神话+金额
             if  rareDegree>=4 and amount<=300000:
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)



             if(amount<=config.rares[rareDegree]):
                 service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
                 # 发送微信提醒
                 service.purchaseSubmit(request,petid,amount,rareDegree,validCode)
        except service.BusinessException as e:
            print(e.value)
            continue



main()


