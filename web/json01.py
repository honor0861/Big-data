# 파일명 : json01.py - 파일에서 가져온 거
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding ='utf-8')
cursor = conn.cursor()
"""
# 파일 읽기
file1 = open('./resources/exam1.json')

# str to dict로 변경
data1 = json.load(file1)

print(data1)
print(type(data1))
"""
# 파일 읽기
file2 = open('./resources/exam2.json', encoding ='utf-8')
data2 = json.load(file2)
print(data2)
# {"ID","aaa","PW":"34"}
sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, :PW, :NAME, :AGE, SYSDATE)
    """ # 한글 인식이 안됨, 순서도 상관없음(알아서 찾아감)
cursor.execute(sql, data2)
conn.commit()

# print(data2)
# print(type(data2))