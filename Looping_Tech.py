for key, value in enumerate(["The","Python","Course"]):
    print(key, value)


question = ["name","color","shape"]
answers = ["apple","red","a circle"]

for question, answer in zip(question, answers):
    print("What is your {} ? I am {}".format(question, answer))


list = [1,2,3,3,7,6,12,10,9,9,8,4,5]
for i in sorted(list):
    print(i, end = " ")

print("\n")

for i in sorted(set(list)):
    print(i, end = " ")
