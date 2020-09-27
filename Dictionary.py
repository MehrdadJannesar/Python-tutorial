Dict = {1:"Python", 4:"Tutorial", "Year":2020}

print("Create Dict with {}")
print(Dict)
Dict_1 = dict([(1,"Python"),("Year",2020)])
print("\nDictionary with each itme as a pair: ")
print(Dict_1)

NDict = {1:"Python", 2:{"year":2020, 5:"Fall"}}

Dict[0] = "Mehrdad"
Dict[3] = "Jannesar"
Dict[3] = "Jannesars"
Dict[2] = 4,5,6,7,8
Dict[5] = {'Nested':{'1':'Life','2':'Python'}}
print(Dict)


for val in Dict.values():
    print(val)


for key,val in Dict.items():
    print(key,val)

print(Dict.keys())

if "Year" in Dict:
    print("Yes!")
