import csv
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("area1")
coll = db.get_collection("sangdo2")

f = open('./py_projects/web/resources/sangdo2.csv','r',encoding = "utf-8")
rdr = csv.reader(f)
column = next(rdr, None) # 컬럼 skip

edu = list()
b_address = list()
s_address = list()
is_cctv = list()
num_cctv = list()
road_width = list()

for line in rdr:
    dict1 = dict()
    for idx, val in enumerate(line):
        if val =="":
            val="0"
        dict1[column[idx]]= val
    # print(dict1)
    addr = dict1["소재지도로명주소"].split(" ")
    print(addr)
    # coll.insert_one(dict1)
    edu.append(dict1["시설종류"])
    is_cctv.append(dict1["CCTV설치여부"])
    num_cctv.append(dict1["CCTV설치대수"])
    road_width.append(dict1["보호구역도로폭"])
    b_address.append(addr[0])
    s_address.append(addr[1])

print(edu)
print(is_cctv)
print(num_cctv)
print(road_width)
print(b_address)
print(s_address)

# conn.close()