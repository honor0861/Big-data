import csv
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("area1")
coll = db.get_collection("table")

f = open('./py_projects/web/resources/daegu01.csv','r',encoding = "utf-8")
rdr = csv.reader(f)
next(rdr, None) # 컬럼 skip

edu = list()
area_zone = list()
is_cctv = list()
num_cctv = list()
road_width = list()

for line in rdr:
    edu.append(line[0])
    area_zone.append(line[2][0:9])
    is_cctv.append(line[8])
    num_cctv.append(line[9])
    road_width.append(line[10])

print(edu)
print(area_zone)
print(is_cctv)
print(num_cctv)
print(road_width)

conn.close()