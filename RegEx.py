import re

# p = re.compile('[a-e]')
#
# print(p.findall("Aye, said Mr. vilobi Stark"))

# p = re.compile('\d') # --> [0-9]
#
# print(p.findall("I went to him at 11 A.M on 4th july 1886"))
#
#
# p = re.compile('\d+') # --> [0-9]
#
# print(p.findall("I went to him at 11 A.M on 4th july 1886"))


p = re.compile('\w')

print(p.findall("He said * in some_lang."))

p = re.compile('\w+')

print(p.findall("I went to him at 11 A.M., he said *** "))

p = re.compile('\W')

print(p.findall("I went to him at 11 A.M., he said *** "))
