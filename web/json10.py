# # 파일명 : json10.py - 웹에서 가져온 거
import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") # 없으면 db1 생성
table = db.get_collection("exam10") # Collection 생성

url = "http://ihongss.com/json/exam10.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict 형식으로 변경

"""
[
    {"id":"id1","name":"가나다1","age":31,
        "score":{
            "math":50,
            "eng":90,
            "kor":69}},
    {"id":"id2","name":"가나다2","age":32,
        "score":{
            "math":90,
            "eng":68,
            "kor":80}},
    {"id":"id3","name":"가나다3","age":33,
        "score":{
            "math":70,
            "eng":76,
            "kor":60}},
    {"id":"id4","name":"가나다4","age":34,
        "score":{
            "math":80,
            "eng":79,
            "kor":50}},
    {"id":"id5","name":"가나다5","age":35,
        "score":{
            "math":80,
            "eng":78,
            "kor":90}}
]

"""
# insert_one({})
# insert_many([{},{},{}])
print(data1)
data2= data1['data']
print(data2)
for tmp in data2:
    print(tmp['id'])
    print(tmp['name'])
    print(tmp['age'])
    print(tmp['score']['math'])
    print(tmp['score']['kor'])
    dict2 = dict()
    dict2['id'] = tmp['id']
    dict2['name'] = tmp['name']
    dict2['age'] = tmp['age']
    dict2['score_math'] = tmp['score']['math']
    dict2['score_kor'] = tmp['score']['kor']

    table.insert_one(dict2)

conn.close()