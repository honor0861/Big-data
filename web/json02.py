# # 파일명 : json02.py - 웹에서 가져온 거
import requests
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding ='utf-8')
cursor = conn.cursor()

"""
{
    'ret' :{'id': 'a386,'name':'123','age':34},
    'ret1':{'id': 'a383','name':'123','age':36}
}
"""

url = "http://ihongss.com/json/exam2.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict 형식으로 변경
print(data1)
ret = data1['ret']
#ret1 = data1['ret1']

print(type(ret))
print(ret)

ret['pw']= 1234
print(ret)

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, :PW, :NAME, :AGE, SYSDATE)
    """ # key를 넣어줘야 인식이 됨(:ID, :PW를 넣어줘야 함) / 리스트와 튜플은 (:1, :2, :3, :4)
cursor.execute(sql, ret)
conn.commit()


