import  service
import  redisClient
import  datetime
proxies = {}
import  cache
cache =  cache.Cache()
while True:
    try:

        print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        #查狗數據
        proxy = cache.get("proxies")
        if(proxy == None):
            proxies['http'] = redisClient.getProxyIp()
        else:
            proxies['http'] = proxy
        data = service.queryData("CREATETIME_DESC",3,proxies)
        cache.set("proxies",proxies,30)
        redisClient.addLetsgoData(data)
    except Exception as e:
        print(e)
