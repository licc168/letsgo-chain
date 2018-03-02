import  service
import  redisClient

while True:
    if service.setProxies():
        data = service.queryData("CREATETIME_DESC")
        redisClient.addLetsgoData(data)