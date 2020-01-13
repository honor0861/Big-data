# # 파일명 : json04.py - 웹에서 가져온 거
import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") # 없으면 db1 생성
table = db.get_collection("exam21") # Collection 생성

url = "http://ihongss.com/json/exam21.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict 형식으로 변경

"""
[
    {"boxOfficeResult":{
        "boxofficeType":"일별 박스오피스",
        "showRange":"20120101~20120101",
        "dailyBoxOfficeList":[
            {"rankOldAndNew":"OLD",
            "movieNm":"미션임파서블:고스트프로토콜",
            "salesShare":"36.3",
            "salesAcc":"40541108500",
            "scrnCnt":"697",
            "showCnt":"3223"},
]
"""
# insert_one({})
# insert_many([{},{},{}])
data2 = data1['boxOfficeResult']
data3 = data2['dailyBoxOfficeList']

for tmp in data3:

    print(tmp['rankOldAndNew'])cd
    print(tmp['movieNm'])
    print(tmp['salesShare'])
    print(tmp['salesAcc'])
    print(tmp['scrnCnt'])
    print(tmp['showCnt'])
  
    dict1 = dict()
    dict1['showRange'] = data2['showRange']
    dict1['rankOldAndNew'] = tmp['rankOldAndNew']
    dict1['movieNm'] = tmp['movieNm']
    dict1['salesShare'] = tmp['salesShare']
    dict1['salesAcc'] = tmp['salesAcc']
    dict1['scrnCnt'] = tmp['scrnCnt']
    dict1['showCnt'] = tmp['showCnt']
    table.insert_one(dict1)

conn.close()