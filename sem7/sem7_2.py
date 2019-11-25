import datetime as dt

def decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result =  func(*args, **kwargs)
        except Exception as ex:
            with open('log.txt', 'a') as log:
                log.write(str(dt.datetime.now())+': In ' + func.__name__ + ' with ' + args + ' caught 'str(ex) + ' \n')
            print(str(dt.datetime.now())+': In ' + func.__name__ + ' with ' + args + ' caught 'str(ex) + ' \n')
            return None
        else:
            with open('log.txt', 'a') as log:
                log.write(str(dt.datetime.now())+': Finished ' + func.__name__ +' with ' + args + ' without errors \n')
            print(str(str(dt.datetime.now())+': Finished ' + func.__name__ +' with ' + args + ' without errors \n')
        return result
    return wrapper


@decorator
def my_func1(x, y):
    raise ValueError("Wrong value")
    return (x - y)

my_func1(20, 'a')

@decorator
def my_func2(x, y):
    return (x / y)

my_func2(13, 0)

@decorator
def my_func3(x, y):
    raise TimeoutError("Timed out")
    return (x + y)

my_func3(0, 0)

@decorator
def my_func4(x, y):
    return x*y

my_func4(1, 4)
