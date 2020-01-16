import csv
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("area1")
coll = db.get_collection("daegu3")

f = open('./py_projects/web/resources/daegu03.csv','r',encoding = "utf-8")
rdr = csv.reader(f)
column = next(rdr, None) # 컬럼 skip

edu = list()
area_zone_si = list()
area_zone_gu = list()
is_cctv = list()
num_cctv = list()
road_width = list()

for line in rdr:
    dict1 = dict()
    edu.append(line[0])
    area_zone_si.append(line[2][0:5])
    area_zone_gu.append(line[2][6:9])
    is_cctv.append(line[8])
    num_cctv.append(line[9])
    road_width.append(line[10])
    
    for idx, val in enumerate(line):
        dict1[column[idx]]= val
    coll.insert_one(dict1)
  
print(edu)
print(area_zone_si)
print(area_zone_gu)
print(is_cctv)
print(num_cctv)
print(road_width)

conn.close()