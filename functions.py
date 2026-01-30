# Repeatabilty, contracts, abstaction.  

# def greet(name: str, age: int) -> str:
#     """Returns a greeting message."""
#     return f"Hello, {name}! You are {age} years old."

# y = greet(30,"Alice")
# print(y)

# def greet(name, age=18):
#     return f"Hello, {name}! You are {age} years old."

# y = greet("Alice")
# print(y)

# *args: if we dont know how many arguments will be passed.
# recieved as a tuple.


# def order_pizza(size, *toppings):
#     print(f"Order received for a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# order_pizza(12, "Mushrooms")
    

# **kwargs: if we dont know how many keyword arguments will be passed.
# send a dictionary.

# def combined(*args, **kwargs):
#     print(args)
#     print(kwargs)

# combined(1, 2, b=3, name="Alice", age=30)

# all args before / must be positional
# all args after * must be keywords arguments
# middle args can be either positional or keyword arguments.
# THIS IS ENFORCED!!!!!!

# def example(a, b, /, f, *, c, d):
#     print(f"a: {a}, b: {b}, c: {c}, d: {d}")

# example(1, 2, f=6, c=3, d=4)

# def maths_op(a, b, /, operation: str ="add", *, decimal_place=None):
#     if operation == "add":
#         result = a + b
#     elif operation == "subtract":
#         result = a - b
#     else:
#         raise ValueError("Unsupported operation")
#     return round(result, decimal_place)

# print(maths_op(5, 5))
# print(maths_op(5,5, "subtract"))
# print(maths_op(5, 5, operation="add"))
# print(maths_op(5.15687, 5.232656, operation="add", decimal_place=4))


# Recursion:

# def factorial(n: int) -> int:
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  # Output: 120 
     
# frame:  - store local variables and function state.
#         - locals() and globals()
#         - calling context:
#             - code object = (f_code)


# stack: stack of frames, ordered by call time.
# pops the function. 


# import inspect

# def trace_function_calls():
#     print("current frame info:",  inspect.currentframe().f_code.co_name)
#     print("stack info:", inspect.stack()[0].function)
#     x = 5
#     print(locals())
#     for frame in inspect.stack():
#        print(frame.function)

# def caller():
#     trace_function_calls()

# caller()
# print(locals())

# higher level functions:

# def square(x):
#     return x * x

# def apply_function(func, value):

#     return func(value)

# print(apply_function(square, 5))  # Output: 25

# lambdas: discrete, one line, unnamed(mostly) functions.

# square = lambda x: x * x
# print(square(6))  # Output: 36

# numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squared_numbers = list(map(lambda x: x ** 2, numbers))


# wrappers:

# def simle_wrapper(func):
#     def wrapped(*args, **kwargs):
#         print("Calling wrapped function")
#         return func(*args, **kwargs)
#     return wrapped


# @simle_wrapper
# def greet(name):
#     """
#     Returns a greeting message.
#     """
#     print(f"Hello, {name}!")
    
# print(greet.__doc__)  # Output: Returns a greeting message.
# greet(  "Alice") 

# from functools import wraps, lru_cache
# import time

# def simle_wrapper(func):
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         print("Calling wrapped function")
#         return func(*args, **kwargs)
#     return wrapped


# @simle_wrapper
# def greet(name):
#     """
#     Returns a greeting message.
#     """
#     print(f"Hello, {name}!")
    
# print(greet.__doc__)  # Output: Returns a greeting message.
# greet(  "Alice")

# @lru_cache(maxsize=None)
# def add(a, b):
#     print("Computing...")
#     time.sleep(10) # Simulate a time-consuming computation
#     return a + b

# print(add(5, 10))  # Computes and caches the result
# print(add(5, 10))  # Retrieves the result from the cache

