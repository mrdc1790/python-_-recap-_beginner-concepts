def func():
    return 1
def hello():
    return "Hello"

greet = hello
if __name__ == "__main__":
    del hello
    print(greet())