import redis
import json
r = redis.Redis(host="localhost", port=6379, db=0)

letgoDataKey = "letgo-data"
#获取第三方验证码秘钥
def getCodeApi():
    apis = r.hgetall("apis")
    for appid, sign in apis.items():
        return  appid,sign

# 删除秘钥
def delApiKey(key):
    r.hdel("apis",key)


# 存储莱茨狗列表数据
def addLetsgoData(data):
    r.delete(letgoDataKey)
    for item in data:
        r.lpush(letgoDataKey, json.dumps(item))


#获取列表数据
def getLetsgoData():
    length = r.llen(letgoDataKey)
    return r.lrange(letgoDataKey,0,length)

