library = {
  "J.K. Rowling": [
    {
      "title": "Harry Potter and the Sorcerer's Stone",
      "genre": "Fantasy",
      "year": 1998,
      "publisher": "Bloomsbury",
      "ISBN": "978-0747532699",
    },
    {
      "title": "Harry Potter and the Chamber of Secrets",
      "genre": "Fantasy",
      "year": 1999,
      "publisher": "Bloomsbury",
      "ISBN": "978-0747538494",
    },
    {
      "title": "Harry Potter and the Prisoner of Azkaban",
      "genre": "Fantasy",
      "year": 1999,
      "publisher": "Bloomsbury",
      "ISBN": "978-0747542699",
    },
  ],
  "J.R.R. Tolkien": [
    {
      "title": "The Hobbit",
      "genre": "Fantasy",
      "year": 1937,
      "publisher": "George Allen & Unwin",
      "ISBN": "978-0547928227",
    },
    {
      "title": "The Lord of the Rings",
      "genre": "Fantasy",
      "year": 1954,
      "publisher": "George Allen & Unwin",
      "ISBN": "978-0544003415",
    },
    {
      "title": "The Silmarillion",
      "genre": "Fantasy",
      "year": 1977,
      "publisher": "George Allen & Unwin",
      "ISBN": "978-0544003438",
    },
  ],
  "George Orwell": [
    {
      "title": "1984",
      "genre": "Dystopian",
      "year": 1949,
      "publisher": "Secker & Warburg",
      "ISBN": "978-0451524935",
    },
    {
      "title": "Animal Farm",
      "genre": "Political Satire",
      "year": 1945,
      "publisher": "Secker & Warburg",
      "ISBN": "978-0451526342",
    },
    {
      "title": "Homage to Catalonia",
      "genre": "Political Non-fiction",
      "year": 1938,
      "publisher": "Secker & Warburg",
      "ISBN": "978-0141182711",
    },
  ],
  "Jane Austen": [
    {
      "title": "Pride and Prejudice",
      "genre": "Romance",
      "year": 1813,
      "publisher": "T. Egerton",
      "ISBN": "978-0141439518",
    },
    {
      "title": "Sense and Sensibility",
      "genre": "Romance",
      "year": 1811,
      "publisher": "T. Egerton",
      "ISBN": "978-0141439662",
    },
    {
      "title": "Emma",
      "genre": "Romance",
      "year": 1815,
      "publisher": "John Murray",
      "ISBN": "978-0141439587",
    },
  ],
  "Agatha Christie": [
    {
      "title": "Murder on the Orient Express",
      "genre": "Mystery",
      "year": 1934,
      "publisher": "Collins",
      "ISBN": "978-0062693556",
    },
    {
      "title": "And Then There Were None",
      "genre": "Mystery",
      "year": 1939,
      "publisher": "Collins",
      "ISBN": "978-0062073556",
    },
    {
      "title": "The ABC Murders",
      "genre": "Mystery",
      "year": 1936,
      "publisher": "Collins",
      "ISBN": "978-0062074002",
    },
  ],
}


for author, books in library.items():
    for book in books:
        print(book["title"])

update publisher:

author = "George Orwell"
target = "1984"

for book in library.get(author, []):
    if book["title"] == target:
        book["publisher"] = "png"
        break