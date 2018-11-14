# from pymongo import MongoClient
# from config import *
from tool import *
from config import *
# import datetime
# client = MongoClient(Mongo_host, Mongo_port)
# db_auth = client[Mongo_db]
# db_auth.authenticate(Mongo_user, Mongo_password)
# collection = db_auth['smscode']
# collection.insert({
#     "_id" : "13999999998",
#     "certificate_type" : "idcard",
#     "phone" : "13999999999",
#     "updatetime" : 1540715429,
#     "password" : "123456",
#     "certificate_number" : "123445693884640",
#     "invitecode" : "Y2R5E9",
#     "nickname" : "june",
#     "id" : "0000000001",
#     "createtime" : 1540715429,
#     "expire_time" : datetime.datetime.utcnow()
# })
# client.close()

# import hashlib
# # def md5encrypt(data):
# #     m = hashlib.md5()
# #     m.update(data)
# #     result = m.hexdigest()
# #     return result
# # print(md5encrypt(111))
# print(hashlib.md5('123'.encode(encoding='utf-8')).hexdigest())
# print(str(find_mongo('user',{}).count()).zfill(10))
a = "00000000000000010"
print(a.lstrip('0'))
a = ['111','2222']
a.remove('111')
print(a)
from tool import *
# import time
# tag = []
# inset_mongo('usertag',{'_id':'13999999998','createtime':int(time.time()),'updatetime':int(time.time()),'tags':tag})
# b = [{'asset':0.1,'updatetime':1541767754},{'asset':0.2,'updatetime':1541767700},{'asset':0.3,'updatetime':1541767799}]
# c = sorted(b, key=lambda x : x['updatetime'], reverse=True)
# print([{'asset':i['asset'],'updatetime':unixtotime(i['updatetime'])} for i in c])
# # print(for j in [i for i in c])
# for i in c:
#     for key in i.values():
#         if key == "updatetime":
#             i["updatetime"] = unixtotime(i['updatetime'])
# print(c)
# globalpower = [aggregate_mongo('asset',[{'$group' : {'_id' : '', 'total' : {'$sum' : "$power_increment"}}}]).next()][0]
# print(globalpower['total'])
# # toppower = sort_mongo('power', {"power_increment": 1, "userphone": 1, '_id': 0})
# # print(toppower.sort({"power_increment": -1}))
# # import pymongo
# # a = [{'nickname':find_mongo('user',{'_id':i['userphone']})[0]['truename'],'power':i['power_increment']}for i in find_mongo('power',{}).sort([("power_increment",pymongo.DESCENDING)])]
# # print(a)
# a = find_mongo("asset",{"items.updatetime":{"$gt":1541865600}})
# print(a[0])
a = aggregate_mongo('asset',[{"$match": {"items.updatetime": {"$gt":int(time.mktime((datetime.date.today()).timetuple()))}}},{"$unwind": "$items"},{"$match": {"items.updatetime": {"$gt":int(time.mktime((datetime.date.today()).timetuple()))}}},{'$group': {'_id': '', 'total': {'$sum': "$items.asset_increment"}}}])
print(a.next())