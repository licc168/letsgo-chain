import  service
import  redisClient
import  datetime

while True:

    try:


        print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #查狗數據
        data = service.queryData("CREATETIME_DESC",)
        redisClient.addLetsgoData(data)
    except Exception as e:
        print(e)
