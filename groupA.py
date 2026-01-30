library = {
  "George Orwell": {
    "1984": {
      "Genre": "Dystopian",
      "Year": 1949,
      "Publisher": "Secker & Warburg",
      "ISBN": "9780451524935"
    },
    "Animal Farm": {
      "Genre": "Political Satire",
      "Year": 1945,
      "Publisher": "Secker & Warburg",
      "ISBN": "9780451526342"
    },
    "Homage To Catalonia": {
      "Genre": "Memoir",
      "Year": 1938,
      "Publisher": "Secker & Warburg",
      "ISBN": "9780156421171"
    },
    "Down And Out In Paris And London": {
      "Genre": "Memoir",
      "Year": 1933,
      "Publisher": "Victor Gollancz",
      "ISBN": "9780156262248"
    },
    "Coming Up For Air": {
      "Genre": "Fiction",
      "Year": 1939,
      "Publisher": "Victor Gollancz",
      "ISBN": "9780156196253"
    }
  },
  "J.K. Rowling": {
    "Harry Potter And The Sorcerer's Stone": {
      "Genre": "Fantasy",
      "Year": 1997,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747532699"
    },
    "Harry Potter And The Chamber Of Secrets": {
      "Genre": "Fantasy",
      "Year": 1998,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747538493"
    },
    "Harry Potter And The Prisoner Of Azkaban": {
      "Genre": "Fantasy",
      "Year": 1999,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747542155"
    },
    "Harry Potter And The Goblet Of Fire": {
      "Genre": "Fantasy",
      "Year": 2000,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747546245"
    },
    "Harry Potter And The Order Of The Phoenix": {
      "Genre": "Fantasy",
      "Year": 2003,
      "Publisher": "Bloomsbury",
      "ISBN": "9780747551003"
    }
  },
  "J.R.R. Tolkien": {
    "The Hobbit": {
      "Genre": "Fantasy",
      "Year": 1937,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780547928227"
    },
    "The Fellowship Of The Ring": {
      "Genre": "Fantasy",
      "Year": 1954,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780547928210"
    },
    "The Two Towers": {
      "Genre": "Fantasy",
      "Year": 1954,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780547928203"
    },
    "The Return Of The King": {
      "Genre": "Fantasy",
      "Year": 1955,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780547928197"
    },
    "The Silmarillion": {
      "Genre": "Fantasy",
      "Year": 1977,
      "Publisher": "George Allen & Unwin",
      "ISBN": "9780618126989"
    }
  },
  "Agatha Christie": {
    "Murder On The Orient Express": {
      "Genre": "Mystery",
      "Year": 1934,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062693662"
    },
    "And Then There Were None": {
      "Genre": "Mystery",
      "Year": 1939,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062073488"
    },
    "The Murder Of Roger Ackroyd": {
      "Genre": "Mystery",
      "Year": 1926,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062693662"
    },
    "Death On The Nile": {
      "Genre": "Mystery",
      "Year": 1937,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062073556"
    },
    "The ABC Murders": {
      "Genre": "Mystery",
      "Year": 1936,
      "Publisher": "Collins Crime Club",
      "ISBN": "9780062073563"
    }
  },
  "Stephen King": {
    "The Shining": {
      "Genre": "Horror",
      "Year": 1977,
      "Publisher": "Doubleday",
      "ISBN": "9780307743657"
    },
    "It": {
      "Genre": "Horror",
      "Year": 1986,
      "Publisher": "Viking",
      "ISBN": "9781501142970"
    },
    "Misery": {
      "Genre": "Psychological Horror",
      "Year": 1987,
      "Publisher": "Viking",
      "ISBN": "9780450417399"
    },
    "Pet Sematary": {
      "Genre": "Horror",
      "Year": 1983,
      "Publisher": "Doubleday",
      "ISBN": "9781501156700"
    },
    "Doctor Sleep": {
      "Genre": "Horror",
      "Year": 2013,
      "Publisher": "Scribner",
      "ISBN": "9781476727653"
    }
  }
}


for author, books in library.items():
    for title in books:
        print(title)

library["George Orwell"]["1984"]["Publisher"] = "Penguin Books"