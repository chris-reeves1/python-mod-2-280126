# Finish around 4 - last 30 mins for questions/extra help etc. 
# 12.30-13.30 for lunch
# 11.00 15 min break + 14.45 15 min break

# today:
# data types + vars
# complex data types - lists, tuples, sets, dicts

# Thursday:
# loops/conditionals
# mini project


# print("Hello, World!")  # this is a comment

# - web dev - Java, js
# - apps - java/swift/kotlin
# - data science - python
# - automation - python
# - AI/ML - pyhton
# - game dev - C#/C++
# - scripting - python
# - cyber security - python/C
# - os - c
# - IOT/edge - python

# interpreted vs compiled
# dynamically typed vs statically typed
# high level (highest)

# simple data types:

# int - number 
# float - decimal number
# string - text, - word to paragraph to an entire book. ""
# bool - True/False, 1/0, something or nothing. 

# variables (a reference):

# a = 5 - a reference, sets a value with '=', data obj is stored in mem.    

# x = 256
# y = 256

# print(x is y)   # == check for same data is checks for same obj.
#                 # internation - cannot be overridden - caching can. 

# print(id(x))
# print(id(y))

# def func():
#     a = int(str(256))
#     return a 

# def func2():
#     b = int(str(256))
#     return b
   
# print(func() is func2())  # false. 
    
# naming convention: consistant, follow a guide/style + be descriptive.

# 1age = 10  - cant start with a number.
# Age = 10  - reserve for class names. 
# AGE = 10 - constant - dont change.

#  print_ = "Hello"  # dont do this.    

# scope:
# global_variable = "accessible everywhere"


# def my_function():
#     local_variable = "accessible only inside this function"
#     global global_variable
#     global_variable = "will this change the actual global?"
#     # print(local_variable)
#     # print(global_variable)


# my_function()
# print(global_variable)


# design:
# efficiancy: speed, ram/cpu
# maintainability: readability, structure, comments/docstrings
# scalability: features, users, data

# inspect + traceback module:

# import inspect
# import traceback

# def function_a():
#     function_b()

# def function_b():
#     function_c()

# def function_c():
#     print("The call stack is: ")
#     traceback.print_stack()

# function_a()

# This will not be grabbed by inspect

# THis can be grabbed with inspect. 
# THis can be grabbed with inspect.
# def example(x: int, y: int) -> int:
#     """
#     Description: This is an example function that does simple addition.
#     inputs: x: int - first number and y: int - second number
#     outputs: int - sum of x and y
#     """
#     return x + y

# example("a", "10")
# print(inspect.getdoc(example))
# print(inspect.getcomments(example))
# print(inspect.signature(example))
# print(inspect.getsource(example))

# cocncatenation:

# name = input("Enter your name: ")
# age =  int(input("Enter your age: "))

# # print("name is " + name + " and age is " + str(age))  # type casting
# # print("name is", name, "and age is ", age)  # slightly better way
# print(f"name is {name.upper()} and age is {age**2}")  # best way - f strings

# pi = 3.14159
# print(f"Pi rounded to 2 decimal places is {pi:.2f}")
# print(f"{name:^20}")  # center within 20 spaces
# print(f"{name:<20}")  # left align within 20 spaces
# print(f"{name:>20}")  # right align within 20 spaces
# print(f"{age:0>5}")  # pad with zeros to make it 5 digits
# print(f"{1000000:,}")

# # .format - old java type way

# print(f"name is {} and age is {}".format(name, age))
# escap chars
# \n - new line, \t - tab, \\ - backslash, \' - single quote, \" - double quote

# print("Person1:\thello\nPerson2:\thello \U0001F600")  # unicode for emojis

# String methods:

print("hello world".upper())  # HELLO WORLD
print("HELLO WORLD".lower())  # hello world
print("hello world".count("o", 5, 8))
print("hello world world world world".replace("world", "there", 3))

# hello there
