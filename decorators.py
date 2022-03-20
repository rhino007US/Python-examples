# template for all decorator syntax
import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
# def print_name(): simple example w/o *args **kwargs
#     print('Alex') simple example
def add5(x):
    return x + 5
    
# Now wrap the function by passing it as argument to the decorator function
# and asign it to itself -> Our function has extended behaviour!
#
# print_name = start_end_decorator(print_name) simple form
# print_name()

print(help(add5))
print(add5.__name__)

# second example

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f'hello {name}')

greet('Alex')
