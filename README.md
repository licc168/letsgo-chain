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

   第三方验证码接口平台（https://www.showapi.com/api/sku/184）

   showapi_appid=""  #替换此值
   showapi_sign=""   #替换此值


    key：等级 0-4依次（普通-稀有-卓越-史诗-神话）
    value：最大价格
    rares = {0:100,1:100,2:300,3:500,4:1000}

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









