# Closure:
import logging
from functools import wraps


def square(x):
    return x * x


f = square
print(square)
print(f)


def my_map(func, args_list):
    result = []
    for i in args_list:
        result.append(func(i))
    return result


def cube(x):
    return x * x * x


squares = my_map(cube, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])

print(squares)
print(cubes)


def logger(msg):

    def log_msg():
        print(msg)

    return log_msg


logger_msg = logger("Hi")
logger_msg()


def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}<{tag}>")

    return wrap_text


print_h1 = html_tag("h1")
print_h1("Text Headline H1")

print_h1("Another Text Headline")

print_p = html_tag("p")

print_p("Paragraph Tag")

ev_cache = {4: 16, 2: 4}


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


my_inner_1 = outer_func("Hello")
my_inner_2 = outer_func("World")
my_inner_1()
my_inner_2()


logging.basicConfig(filename="example.log", level=logging.INFO)


def logger_fun(func):
    @wraps(func)
    def inner_logger_fun(*args):
        logging.info(f"Running with arguments {func.__name__}")
        print("Running before executing the original fun {}")
        print(func(*args))

    return inner_logger_fun


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger_fun(add)

add_logger.__name__

add_logger(10, 20)

sub_logger = logger_fun(sub)

sub_logger(88, 10)


#### Decorators #######
