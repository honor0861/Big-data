import csv
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("area1")
coll = db.get_collection("table")

f = open('C:\\Users\\admin\\Desktop\\python_projects\\area\\busan.csv','r')
rdr = csv.reader(f)
next(rdr, None) # 컬럼 skip

for line in rdr:
    # print(type(line))
    # print(line)
    print(line[0])
    
conn.close()