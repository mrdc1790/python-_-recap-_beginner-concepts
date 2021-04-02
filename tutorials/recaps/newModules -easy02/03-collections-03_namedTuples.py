from collections import namedtuple

mytuple = (10,20,30)
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(5, 'Sheltie', 'Bella')
print(sammy.breed)