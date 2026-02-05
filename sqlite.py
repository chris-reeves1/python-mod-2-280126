import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()

# commands:
# - CREATE - creates a new table
# - INSERT - insert data into a table
# - SELECT - query data from a table
# - UPDATE - updating 
# - DELETE - deleting
# - WHERE - filtering

# Create

c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT 
        )
""")

# unique, check, default, fk. 

conn.commit()


# INSERT DATA
# ? - just a placholder for data. - safer! 


c.execute("SELECT * FROM students WHERE name = ? and age = ? and grade = ?", ("c", 10, "b"))
if c.fetchone() is None:
    c.execute("""
            INSERT INTO students (name, age, grade)
            VALUES (?, ?, ?)
    """, ("c", 10, "b"))
else:
    ("already in the table")

# UPDATING

c.execute("""
    UPDATE students
    SET grade = ?
    WHERE name = ?
""", ("A", "c"))
conn.commit()

c.execute("SELECT * FROM students")
x = c.fetchall()

for data in x:
    print(data)

# DELETE

c.execute("""
    DELETE FROM students
    WHERE name = ?
""", ("c"))
conn.commit()


c.execute("SELECT * FROM students")
x = c.fetchall()

for data in x:
    print(data)


# add many

student_data = [
    ("person1", 11, "A"),
    ("Person2", 12, "B"),
    ("Person3", 13, "C")
]

c.executemany("""
            INSERT INTO students (name, age, grade)
            VALUES (?, ?, ?)
""", student_data)
conn.commit()


# c.execute("SELECT * FROM students")
# x = c.fetchall()

# for data in x:
#     print(data)

for data in c.execute("SELECT * FROM students"):
    print(data)


c.execute("""
    CREATE INDEX IF NOT EXISTS idx_students_names
    ON students(name)
""")
conn.commit()
