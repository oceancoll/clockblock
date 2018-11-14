#coding:utf-8
import pymongo
import datetime
from tool import *
client=pymongo.MongoClient('chengdu.orangesea.cn',27017)
#链接数据库
#创建dbdb数据库
import time
db =client['clockdb']
#创建username_id集合
db.authenticate('clockuser1', 'clockuser1')
#db.username_id.createIndex({"expiretime":1},{'expireAfterSeconds':60})
username_id = db['user_id']
#username_id.create_index([("time", pymongo.ASCENDING)], expireAfterSeconds=60)
#username_id.create_index([{"expiretime":1},{'expireAfterSeconds':60})
# for i in range(30):
#     inset_mongo('user',
#                 {'_id': i, 'phone': i, 'updatetime': int(time.time()),
#                  'certificate_type': '', 'certificate_number': '', 'nickname': '',
#                  'createtime': int(time.time()), 'id': create_id('user', 10), 'headpic': Default_headpic,
#                  'truename': '', 'isident': 0})
#username_id.insert_one(({'_id': "name2", 'sequence_value': 0,'time':datetime.datetime.utcnow()}))
username_id.insert_one(({'_id': "userid", 'sequence_value': 0}))
#自增函数
def getNextValue(user_Name):
    ret = username_id.find_and_modify({"_id": user_Name}, {"$inc": {"sequence_value": 1}}, safe=True, new=True)
    new = ret["sequence_value"]
    return new
# if __name__=='__main__':
# # 插入username_id
#     username_id.insert_one(({'_id': "name1", 'sequence_value': 0}))
# for i in range(10):
#     print(getNextValue('name'))

