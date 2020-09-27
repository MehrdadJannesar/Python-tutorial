# $gt
# $ls
# $gte
# $lse
# $and
# $or
# $not

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client["PythonTutorial"]

collection = db["Student"]

query_1 = collection.find({"Roll No":{"$gt":"1003"}})

print("The data having Roll No greater than 1003 is :")
for record in query_1:
    print(record)


query_2 = collection.find({"Roll No":{"$lt":"1003"}})
print("\nThe data having Roll No less than 1003 is :")
for record in query_2:
    print(record)


query_3 = collection.find({"$or":[{"Roll No":{"$gt":"1003"}},
                                  {"Roll No":{"$gt":"1004"}}]})

print("Query 3 is :")
for record in query_3:
    print(record)
