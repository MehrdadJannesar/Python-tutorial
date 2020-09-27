# Access Mode:
# Read only 'r'
# Read and write "r+" / "w+"
# Write "w"
# Append only "a"
# Append and read "a+"
#
# name_var = open("Filename", "Access Mode")

# file1 = open("Python.txt")
# print(file1.read())
#
# file1.close()
#
# file2 = open("Python.txt",'r')
#
# for each in file2:
#     print(each)


# file2 = open("Python.txt",'r')
# print(file2.read())


# file3 = open("Python.txt", "w")
# file3.write("This is the write command")
# file3.write("It allows us to write in a file")
# file3.close()

#
# file4 = open("Python.txt", 'a')
# file4.write("\nThis will add this line!")
# file4.close()



# with open("Python.txt") as file:
#     data = file.read()
#
# with open("Python.txt", "w+") as f:
#     f.write("Hello World!")

# print(data)



with open("Python.txt","r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
