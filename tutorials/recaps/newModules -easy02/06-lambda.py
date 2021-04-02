def square (num):
    result = num**2
    return result

my_nums = [1,2,3,4,5]

print(list(map(square, my_nums)))

print(list(map(lambda num: num**2, my_nums)))