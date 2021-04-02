def square (num):
    result = num**2
    return result

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)
print(list(map(square, my_nums)))

def splicer(myString):
    if len(myString) % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'

names = ['Andy','Eve','Sally']
print(list(map(splicer,names)))

print(list(map(lambda num: num**2, my_nums)))