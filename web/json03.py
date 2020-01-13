# # 파일명 : json03.py - 웹에서 가져온 거
import requests
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding ='utf-8')
cursor = conn.cursor()

url = "http://ihongss.com/json/exam3.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict 형식으로 변경
# data1 => {ret:[{},{},{}], ret1:[{},{},{}]}
ret = data1['ret'] # [{},{},{}] => [A, B, C]
for tmp in ret:
    print(tmp) # {id: "a2001", name: "123", age: 34}
    sql="""
        INSERT INTO MEMBER(ID,PW, NAME,AGE, JOINDATE)
        VALUES(:id, 'aaa',:name,:age,SYSDATE)
        """
    cursor.execute(sql, tmp)
conn.commit()