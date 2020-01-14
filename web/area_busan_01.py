import csv
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("area1")
coll = db.get_collection("table")

f = open('C:\\Users\\admin\\Desktop\\python_projects\\area\\busan1.csv','r')
rdr = csv.reader(f)
next(rdr, None) # 컬럼 skip

edu = list()
is_cctv = list()
num_cctv = list()
load_
for line in rdr:
    print(line[0])
    # print(type(line))
    # print(line)
    #del(line[1:7])
    #del(line[5])
    #print(line)
    
conn.close()