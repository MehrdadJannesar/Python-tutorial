# SELECT * FROM tbname

# from pymongo import MongoClient
#
# client = MongoClient('localhost',27017)
#
# db = client["PythonTutorial"]
#
# collection = db["Student"]
#
# for x in collection.find():
#     print(x)


# SELECT col1,col2,...,coln FROM tbname

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client["PythonTutorial"]

collection = db["Student"]

for x in collection.find({},{"_id":0, "name":1,"Roll No":1}):
    print(x)
