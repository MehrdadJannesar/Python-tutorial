from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client["PythonTutorial"]

collection = db["Student"]
# Delete_one
# myquery = {"name":"Ali"}
#
# collection.delete_one(myquery)

# Delete_Many

myquery = {"name":{"$regex":"^M"}}

d = collection.delete_many(myquery)

print(d.deleted_count," documents deleted!")

#
# for x in collection.find().sort("_id"):
#     print(x)
