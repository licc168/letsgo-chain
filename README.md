# 莱茨狗
    - 根据控制台输出的url手动刷狗
    - 接入第三方平台自动刷狗
    - 支持微信提醒（url默认发送到微信文件助手）

## 配置

 ```
   type = 0 # 0:手动刷狗  1：自动刷狗
   sendMsg=0 # 0:开启微信助手提醒 1：关闭微信信息提醒
   username = '' #用户名
   password = '' #密码

   云服务器接口
   apiurl = 'http://***:8080/ocr'



    key：等级 0-4依次（普通-稀有-卓越-史诗-神话）
    value：最大价格
    rares = {0:100,1:100,2:300,3:500,4:1000}

 ```

## 控制台输出
```
开始登录
等级： 0价格：0.0
https://pet-chain.baidu.com/chain/detail?channel=market&petId=1855392817803958644&validCode=60755c20a550be5f44b0ee2b7d22efa3
result_json data is: {'showapi_res_error': '', 'showapi_res_code': 0, 'showapi_res_body': {'Result': 'SARR', 'ret_code': 0, 'Id': 'af736be6-3031-4d52-b853-8fa10333c1e3'}}
{'errorNo': '10002', 'errorMsg': '有人抢先下单啦', 'timestamp': '2018-02-08 10:34:26', 'data': None}
等级： 0价格：0.0
等级： 0价格：0.0
等级： 0价格：0.0
https://pet-chain.baidu.com/chain/detail?channel=market&petId=1858195541663481935&validCode=f9f9bdad4582a52ae3d446a05626463b
result_json data is: {'showapi_res_error': '', 'showapi_res_code': 0, 'showapi_res_body': {'Result': 'menj', 'ret_code': 0, 'Id': '3455f765-012d-4a5f-b0e9-29ddf1c08476'}}
{'errorNo': '30009', 'errorMsg': '请从集市进入购买', 'timestamp': '2018-02-08 10:37:28', 'data': None}
等级： 1价格：50.0
https://pet-chain.baidu.com/chain/detail?channel=market&petId=1855389553628810160&validCode=d23b7b1c22ae9abe3bc082972f650c43
result_json data is: {'showapi_res_error': '', 'showapi_res_code': 0, 'showapi_res_body': {'Result': '8J7X', 'ret_code': 0, 'Id': 'bed14210-632e-4a9d-96b8-ea099851e75d'}}
{'errorNo': '10002', 'errorMsg': '有人抢先下单啦', 'timestamp': '2018-02-08 10:38:54', 'data': None}
等级： 0价格：0.0
https://pet-chain.baidu.com/chain/detail?channel=market&petId=1864795222772564731&validCode=246b8401feffa251848c66cf12f9337a
result_json data is: {'showapi_res_error': '', 'showapi_res_code': 0, 'showapi_res_body': {'Result': '4BPR', 'ret_code': 0, 'Id': 'd0407d02-36c7-47f8-8957-042d2d6f4aa7'}}
{'errorNo': '10002', 'errorMsg': '有人抢先下单啦', 'timestamp': '2018-02-08 10:40:01', 'data': None}
等级： 0价格：0.0
https://pet-chain.baidu.com/chain/detail?channel=market&petId=1855392714724744586&validCode=6f5e48496528618ab0e9ef9e06959a3a
result_json data is: {'showapi_res_error': '', 'showapi_res_code': 0, 'showapi_res_body': {'Result': 'apfr', 'ret_code': 0, 'Id': '56ef88b7-a5ea-43aa-81d4-1f76951c70e9'}}
{'errorNo': '10002', 'errorMsg': '有人抢先下单啦', 'timestamp': '2018-02-08 10:40:08', 'data': None}
等级： 0价格：0.0
等级： 0价格：0.0
等级： 0价格：0.0
等级： 1价格：1.0
```

## 安装
  ```
  微信接口
  pip install itchat
  自动登录
  pip install selenium

  ```

## 运行

```
 python3.0+
 python main.py

```










