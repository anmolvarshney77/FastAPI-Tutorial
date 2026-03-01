def decor(df):
    def wrapper(a, b):
        print("Hey")
        df(a, b)
        print("Bye")
    return wrapper
@decor
def greet(a, b):
    print(a+b)
greet(5, 10)