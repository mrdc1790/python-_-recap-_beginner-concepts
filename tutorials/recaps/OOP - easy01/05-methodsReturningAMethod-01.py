def hello(name ='Jose'):
    print("The hello() function has been executed!")

    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'
    
    print("I am going to return a function!!")
    if name == 'Jose':
        return greet
    else:
        return welcome

def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool

hello()
## welcome() not defined outside of hello
my_new_func = hello('Jose')
print(my_new_func() )
some_func = cool()
print(some_func() )