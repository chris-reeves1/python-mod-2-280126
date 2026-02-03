#  while loops + for loops:

# # Example of a while loop
# need a condition to be true to start the loop.
# a condition to stop the loop.

count = 0
while count < 5:
    print("Count is:", count)
    count += 1  
      

# # Example of a for loop
# needs an interable to loop over.

# fruits = [, , ]

# for fruit in fruits:
#     print(fruit)

# l = 0
# while l < len(fruits):
#     print(fruits[l])
#     l += 1

# list comprehensions
# make a list or change a list
    # expression    item     iterable
# squares = [x**2 for x in range(10)]
# print(squares)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#                         #  express  item  iterable        condition
# squared_even_numbers = [num**2 for num in numbers if num % 2 == 0]
# print(squared_even_numbers)

# inner
# [input("Enter something: ") for n in range(3)]
# outer
# x = [print(f"Error - {y}") for y in [input("Enter something: ") for n in range(3)]]

# print(x)

Schamas are locked per group (ask me if you need it) -- NO CHANGES!!!
Queries will use a mix of for loops and conditionals. 

basic:
Print every title in the library (one per line)
Count total number of books
List all books by a given author
Find a book by title (case insensitive)
Filter by year: all books published before 1970
Count books by genre and display all

harder:
Find a book by ISBN (exact match only)
Detect duplicate ISBNs
What publisher has the most books in the library?
Update a single books publisher



