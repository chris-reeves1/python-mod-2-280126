library = {
  1: {
    "title": "Why We Sleep: The New Science of Sleep and Dreams",
    "author": "Matthew Walker",
    "type": "Non-fiction",
    "genre": "Science",
    "year": 2017,
    "publisher": "Scribner",
    "ISBN-13": "978-0735211292"
  },
  2: {
    "title": "Atomic Habits: An Easy & Proven Way to Build Good Habits",
    "author": "James Clear",
    "type": "Non-fiction",
    "genre": "Personal Development",
    "year": 2018,
    "publisher": "Avery",
    "ISBN-13": "978-0735211292"
  },
  3: {
    "title": "Prisoners of Geography: Ten Maps That Tell You Everything You Need to Know About Global Politics",
    "author": "Tim Marshall",
    "type": "Non-fiction",
    "genre": "Politics",
    "year": 2015,
    "publisher": "Elliott & Thompson",
    "ISBN-13": "978-1783962433"
  },
  4: {
    "title": "Divided: Why We’re Living in an Age of Walls",
    "author": "Tim Marshall",
    "type": "Non-fiction",
    "genre": "World Politics",
    "year": 2018,
    "publisher": "Penguin Books",
    "ISBN-13": "978-1783963973"
  },
  5: {
    "title": "Macbeth",
    "author": "William Shakespeare",
    "type": "Fiction",
    "genre": "Tragedy",
    "year": 1606,
    "publisher": "Penguin Classics",
    "ISBN-13": "978-0141396507"
  }
}

# print all books:

for book_id, book_info in library.items():
    print(book_info["title"])

# update publisher:

target = "Macbeth"

for book_id, book_info in library.items():
    if book_info["title"].lower() == target.lower():
        book_info["publisher"] = "png"
        break