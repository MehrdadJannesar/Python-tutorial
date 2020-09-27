from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27107/")

db = myclient["PythonTutorial"]

collection = db["Student"]

record = { "_id":5,
            "name": "Mehrdad",
            "Roll No" : "1005",
            "Branch": "CSE"}

rec_id1 = collection.insert_one(record)
