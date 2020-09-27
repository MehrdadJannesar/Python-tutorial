from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client["PythonTutorial"]

collection = db["Student"]

# filter = {"_id": 1}
#
# newValue = {"$set":{"Roll No": "1011"}}

# collection.update_one(filter, newValue)

collection.update_many(

    {"_id":{"$gt":5} },
    {
        "$set":{"Branch":"CSE"}
    }
)

c = collection.find()
for r in c:
    print(r)
