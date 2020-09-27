# x = 5
# print("x is ", x)
#
# print("Python", end='@')
# print("Tutorial")
#
# print("Python", end='\n')
# print("Tutorial")
#
# print('G','M','H', sep='-')
#
# print('09','05','2020', sep='-')
                             # 4.51%
print("Apple : %2d, Orange: %5.2f" %(1,05.333))

print("%7.3o" %(25))

print("%10.3E" %(356.08966))

year = 2020
event = 'Referndum'

print(f'Result of the {year} {event}')

yes_votes = 42_572_658
no_votes = 43_132_490
per = yes_votes / (yes_votes + no_votes)

print('{:-9} yes vots {:.5%}'.format(yes_votes, per))


print('{0} and {1}'.format('python3', 'python2'))

print('{1} and {0}'.format('python3', 'python2'))


print('Number first : {0}, Number second : {1}, Other Number : {other}'.format('2','5', other = '7.5'))

data = dict(fun = "Python", version = '3.8')
print('{fun} version is {version} '.format(**data))
