## print(list(range(0,10)))
## ^(range) is a basic generator

## def create_cubes(n):
##    result = []
##    for x in range(n):
##        result.append(x**3)
##   return result

def gen_fibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b

def create_cubes(n):
    for x in range(n):
        yield x**3

print(list(create_cubes(10)))
print(list(gen_fibon(10)))

def simple_generator():
    for x in range(3):
        yield x

g = simple_generator()
print(next(g))
s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(g))