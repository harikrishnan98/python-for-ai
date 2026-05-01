from functools import wraps


def decorator_outer(original_func):
    def decorator_inner():
        print(f"Wrapper executed before {original_func.__name__}")
        return original_func()

    return decorator_inner


@decorator_outer
def display_func():
    print("Displaying the text")


display_func()

display_decorator = decorator_outer(display_func)
display_decorator()


def decorator_outer_func(original_func):
    def wrapper_func(*args, **kwargs):
        print(f"Wrapper executed before {original_func.__name__}")
        return original_func(*args, **kwargs)

    return wrapper_func


@decorator_outer_func
def display_info(name, age):
    print(f"display info ran with arguments {name}, {age}")


class DisplayUser:
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("call method executed before")
        return self.original_func(*args, **kwargs)


@DisplayUser
def display_user(name, age):
    print(f"display info ran with arguments {name}, {age}")


display_user("Hari Krishnan", "23")

display_dec01 = DisplayUser(display_user)

display_dec01("Man of Steel", "34")


## Practical Example:


def my_logger(original_func):
    import logging

    print(f"Name of the original func: {original_func.__name__}")
    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.INFO)

    @wraps(original_func)
    def wrapper_func(*args, **kwargs):
        logging.info(f"Runs with args: {args}")
        logger = logging.getLogger()
        file_han = logging.FileHandler(f"{original_func.__name__}.log")
        logger.addHandler(file_han)
        logger.setLevel(logging.INFO)
        return original_func(*args, **kwargs)

    return wrapper_func


@my_logger
def display_detail_info(name, age, num):
    print(f"Display Info: {name} and {age} and {num}")


display_detail_info("Hank", "29", "12112")

import logging

logging.basicConfig(filename="sample-decorator.log", level=logging.INFO)

logging.info("THis is for testing")

logger = logging.getLogger("decorator-sample")

console = logging.StreamHandler()
logger.addHandler(console)
logger.setLevel(logging.DEBUG)

file_logger = logging.FileHandler("test-decorator.log")
logger.addHandler(file_logger)
logger.debug("THis is a test debugger log")


def my_timer(original_func):
    import time
    import math

    print("My timer decorator in outer fn")

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        t2 = (time.time()) - t1
        result = original_func(*args, **kwargs)
        print(f"Time taken for the {original_func.__name__} to execute: Time1:{t2}")
        return result

    return wrapper


import time


@my_logger
@my_timer
def display_some(*args, **kwargs):
    time.sleep(2)
    print(f"Display Value:{args} and KW: {kwargs}")


@my_logger  # This function will execute second
@my_timer  # This function execute first
def display_detail(name, age, num):
    print(f"Display Info: {name} and {age} and {num}")


display_detail("WICK", "29", "098")
display_two = my_timer(display_detail)

display_two.__name__
display_two.__doc__

display_two("AKK", "27", "SWE")

# my_timer will return a wrapper function with timer result and that will send as argument to logger_function to execute
# To overcome this we need to use wraps from functools


## Decorator wit arguments


def prefix_decorator(prefix):
    def decorator_function(original_func):
        def wrapper_func(*args, **kwargs):
            print(prefix, "Executed Before", original_func.__name__)
            result = original_func(*args, **kwargs)
            print(prefix, "Executed After", original_func.__name__)
            return result

        return wrapper_func

    return decorator_function


@prefix_decorator("This is a prefix")
def display_info_1(name, age):
    print(f"display info ran with args: {name} and {age}")


display_info_1("JK", 89)
display_hk = prefix_decorator("TEST:LOG$")(display_info_1)("AJ", "28")

# or

display_09 = prefix_decorator("TEST:LOG$")
display_02 = display_09(display_info_1)
display_02("AJ", "28")


def executeApi(execPrefix):

    def outer_func(original_func):
        print(f"Original funciton that have prefix {execPrefix}")

        def wrapper_inner_func(*args, **kwargs):
            print(f"Executing the before inner function with prefix {execPrefix}")
            result = original_func(args, kwargs)
            print(f"Executing the after inner function with prefix {execPrefix}")
            return result

        return wrapper_inner_func

    return outer_func


@executeApi("/PostAPI")
def display_summary(name, detail):
    print(f"Summary of the report of {name} and Detail: {detail}")


display_summary("John Hari", "Ploymath")

display_summary_test = executeApi("TEST")(display_summary)(
    "Hari", "HK is an Polymath Developer"
)


display_info_prefix = prefix_decorator("Prefix Check")(display_info_1)

display_info_prefix.__name__

display_info_1.__name__

display_info_prefix("Hari", "28")
display_info_1("John Wick", "28")


(lambda x, y: lambda z1, y1: x + y + z1 + y1)(10, 20)(30, 40)

set1 = {1, 2, 3, 4, 5}


set2 = {2, 3, 4, 10, 11}

set1.difference_update(set2)