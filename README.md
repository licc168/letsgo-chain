


# [莱茨狗](pet-chain.baidu.com)

   - 支持微信提醒
   - 本地验证码（样本+google深度学习），成功率95%
   - 支持根据属性以及规则筛选莱茨狗
   ![图片](http://lichangchao.top/img/web/letgo.png)
   ![图片](http://lichangchao.top/img/web/tf_model.png)

## 安装
  具体不做详细介绍，可自行百度
- python3.6

- pip install pillow
- tensorflow
- redis



## 配置

 ```
   type = 0 # 0:手动刷狗  1：自动刷狗
   sendMsg=0 # 0:开启微信助手提醒 1：关闭微信信息提醒

    username = '' #用户名
    password = '' #密码

    #key: 等级 0-5依次（普通-稀有-卓越-史诗-神话）
    #value：最大价格
    rares = {0:100,1:100,2:300,3:500,4:1000}

 ```

## 条件帅选
截取一小部分，详细可见main.py
``` python
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

 if body=='天使' and (eye == "白眉斗眼") :

    # 卓越+金额
     if rareDegree == 2 and amount < 10000:
         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
         service.purchaseSubmit(request, petid, amount, rareDegree, validCode)
     if rareDegree == 2   and mouth == '樱桃' and  amount <100000 :
         service.printMsg(body, eye, mouth, rareDegree, amount, count, buyUrl)
         service.purchaseSubmit(request, petid, amount, rareDegree, validCode)



```


## 控制台输出

```
开始登录
天使:小对眼 小獠牙  卓越 0.09万 3 https://pet-chain.baidu.com/chain/detail?channel=market&petId=1898045622630280016&validCode=8f0ea6b9fc13cf1f1f339b59bfb96355
2018-03-08 18:52:38.784298: I C:\tf_jenkins\workspace\rel-win\M\windows\PY\36\tensorflow\core\platform\cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
卓越 900.0  有人抢先下单啦
天使:白眉斗眼 大胡子  卓越 0.09万 3 https://pet-chain.baidu.com/chain/detail?channel=market&petId=1898045656990016212&validCode=74e1ef0365ce5d36ae9231514d403ea0
卓越 900.0  有人抢先下单啦
天使:白眉斗眼 长舌头  卓越 0.2043万 3 https://pet-chain.baidu.com/chain/detail?channel=market&petId=1941267218561062553&validCode=3ee4a8eeb038f90fd83f97a306451dc3

```



```










