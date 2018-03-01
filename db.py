
import MySQLdb

# 打开数据库连接
from common import BusinessException



def getApiConfig():
    db = MySQLdb.connect("47.94.196.111", "root", "111111", "lccf")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select id, appid,sign from  api where delete_flag=0  limit 0,1 "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        id = results[0][0]
        appid = results[0][1]
        sign = results[0][2]
        # 打印结果
        return id,appid, sign
    except:
        raise BusinessException("没有获取到第三方接口")

    # 关闭数据库连接
    db.close()

def updateNum(id):
    db = MySQLdb.connect("47.94.196.111", "root", "111111", "lccf")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "update api set num=num+1 where id="+str(id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        # 关闭数据库连接
    db.close()

def updateDelete(id):
    db = MySQLdb.connect("47.94.196.111", "root", "111111", "lccf")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "update api set delete_flag=1 where id="+str(id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        # 关闭数据库连接
    db.close()
#getApiConfig()

