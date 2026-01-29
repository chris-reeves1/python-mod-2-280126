# collections of values - ways of storing data.
# lists, dictionaries, tuples, sets. 


# lists - ordered, mutable, allows duplicates, any type(mixed). []
# index 0       1        2/-1 
# ["apple", "banana", "cherry"] linear search - O(n)

# dictionaries - unordered(no indexed), mutable, no duplicates for keys, key-value pairs. {}
# {1: "apple", 2: "banana", 3: "cherry"}

# x = hash("hello1")
# print(x)
# y = x %(16 - 1)

# # print(y)
# import sys
# d = {}
# for i in range(80):
#     d[i] = i
#     print(sys.getsizeof(d))

# large_list = list(range(10_000_000))
# large_dict = {num : True for num in range(10_000_000)}

# target = 999_9900

# import time

# start = time.time()
# search = target in large_list
# stop = time.time()
# print(f"{stop - start:.10f} - list")

# start = time.time()
# search = target in large_dict
# stop = time.time()
# print(f"{stop - start:.10f} - dict")


# exercise:
#     - make a dictionary with keys as (2-3) authors and values as 2-3 books per author.
#     - input asking for an author name. (think about UX here).
#     - print the books as a STRING!!!
#     - error handling for incorrect author names. 
#     - USE only in built methods and things we have already covered.

#     - be prepared to justify your choices. 

#     Tomorrow: full schema for authors/books - write search/adds


# book_dictionary = {
# 	"N.T. Wright": ["The Bible for Everyone: A New Translation", "Surprised by Hope: Rethinking heaven, the resurrection and the mission of the Church"],
# 	"Martin Luther": ["95 Theses", "The Bondage of the Will", "Table Talk"],
# 	"Karl Barth": ["Church Dogmatics", "The Epistle to the Romans"]
# }

# author = input("Enter the name of the author: ")

# if author in book_dictionary:
# 	print("Books by " + author + ": ")
# 	books = ", ".join(book_dictionary[author])
# 	print(books)
# else:
# 	print("Cannot find any book by the author.")

# booklist = {

#     "J.K. Rowling": [
#         "Harry Potter and the Sorcerer's Stone",
#         "Harry Potter and the Chamber of Secrets",
#         "Harry Potter and the Prisoner of Azkaban"
#     ],
#     "Roald Dahl": [
#         "Charlie and the Chocolate Factory",
#         "Matilda",
#         "James and the Giant Peach"
#     ],
#     "Sheila McCullagh": [
#         "The Land of the Blue Flower",
#         "Tim and the Hidden People",
#         "The Village with Three Corners"
#     ]
# }

# print("Availible authors:")
# print(", ".join(booklist.keys()))

# author = input("please enter an authors name " )

# books = booklist.get(author, []) #or ["sorry no books found"] "sorry no books found"

# print(", ".join(books) or "no books found")


# JacksBookshop = {
#   "author1": {
#   "name": "Rick Riordan",
#   "book1": "The Lightning Thief", 
#   "book2": "The Sea of Monsters", 
#   "book3": "The Last Olympian",
# },
#   "author2": {
#   "name": "Jonathan Haidt",
#   "book1": "The Happiness Hypothesis", 
#   "book2": "The Righteous Mind",
#   "book3": "The Anxious Generation",  
# },
#   "author3": {
#   "name": "Colleen Hoover", 
#   "book1": "It Ends With Us",
#   "book2": "Verity",
#   "book3": "Hopeless",    
# }
# }
# y = JacksBookshop.get("author2").get("name")
# print(y)

# record  = JacksBookshop.get("author2")

# list_to_print = []

# for k, v in record.items():
#     if "book" in k:
#         list_to_print.append(v)

# print(", ".join(list_to_print))


# full schema for authors/books - write search/adds

# - needs to be a dictionary shape.
# - authors/books/title/type/genre/year/publisher/ISBN
# - 5 authors with 3 books each minimum.
