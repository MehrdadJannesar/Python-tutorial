from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client["PythonTutorial"]

# collection = db["Student"]
#
# mylist = [
#
#   { "_id": 1, "name": "Ali", "Roll No": "1001", "Branch":"CSE"},
#   { "_id": 2, "name": "Hamideh", "Roll No": "1002", "Branch":"IT"},
#   { "_id": 3, "name": "Mehrdad", "Roll No": "1003", "Branch":"ME"},
#   { "_id": 4, "name": "Mina", "Roll No": "1004", "Branch":"ECE"}
#
# ]


newCollection = db["Car"]

myCars = [

  {"Manufacturer":"Honda", "Model":"City", "Color":"Black"},
  {"Manufacturer":"Tata", "Model":"Altroz", "Color":"Golden"},
  {"Manufacturer":"Honda", "Model":"Civic", "Color":"Red"},
  {"Manufacturer":"Hyundai", "Model":"i20", "Color":"white"},
  {"Manufacturer":"Maruti", "Model":"Swift", "Color":"Blue"},


]


newCollection.insert_many(myCars)
