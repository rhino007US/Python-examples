
import functools
def start_end_decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Start')
            result = func(*args, **kwargs)
            print('End')
            return result
        return wrapper

def debug(func):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # "!r" == return value
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")  # "!r" == return value
        return result
    return wrapper


@debug
@start_end_decorator
def say_hello(name):
    greeting = f'hello {name}'
    print(greeting)
    return greeting

say_hello('Alex')
