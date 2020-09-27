from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client["PythonTutorial"]

collection = db["Student"]

for record in collection.find({"Branch":"CSE"}).limit(1):
    print(record)
