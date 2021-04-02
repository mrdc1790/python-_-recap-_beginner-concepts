def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function')
    return wrap_func

    ## def func_needs_decorator():
    ##    print("\tI want to be enwrapped!!")
    ## decorated_func = new_decorator(func_needs_decorator)
    ## decorated_func()

@new_decorator
def func_needs_decorator():
    print("\tI want to be enwrapped!!")
