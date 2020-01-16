import pandas as pd 
import pymongo
import csv

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db2")
coll = db.get_collection("task_info")

f = open('./py_projects/web/resources/exam1.csv','r')
rdr = csv.reader(f)
column = next(rdr, None)
print(column)

for line in rdr:
    dict1 = dict()
    for idx, val in enumerate(line):
        """
        0 Rohit Srivastav
        1 Aaran Puri
        2 male
        3 34
        4 7.5
        5 0.3
        """
        print(column[idx])
        """
        manager_name
        client_name
        client_gender
        client_age
        response_time
        statisfaction_level
        """
        dict1[column[idx]]= val
        coll.insert_one(dict1)
conn.close

# csv는 구분자,  \t
# df = pd.read_csv('./py_projects/web/resources/exam1.csv',delimiter=",")
# print(df)

# df = df.dropna() # NaN 제거 : 결측치 제거
# print(df)

# list1 = df.values.tolist()  # DF -> list로 변경
# print(list1)
# dict1 = df.to_dict()        # DF -> dict로 변경
# print(dict1)






