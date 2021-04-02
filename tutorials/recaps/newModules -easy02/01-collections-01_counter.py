from collections import Counter

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]
print(Counter(mylist))
mylistLetters = ['a','a',10,10,10]
print(Counter(mylistLetters))
letters = 'aaaaabbbbbbbbbbbccccccccccccdddddddddddd'
c = Counter(letters)
print(c)
d = {'a' : 10}
print(d)
print(d['a'])