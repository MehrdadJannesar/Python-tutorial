# SELECT * FROM tbname LIMIT 1

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client["PythonTutorial"]

collection = db["Student"]

x = collection.find_one()

print(x)
