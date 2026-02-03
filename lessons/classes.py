# OOP principles:
#     - abstraction: dont need to see the code.
#     - encapsulation: privacy + safety.
#     - inheritance: parent - child - child inherits all.   
#     - polymorphism: overridding(changing what a method does).

# gives us structure, object creation (custom), state(dictionaries), coupling, behaviour through methods.

# class Example:
#     # attributes
#     name = "chris"

#     # methods
#     def greet(self):
#         print(f"hello {self.name}")


# obj1 = Example()
# obj2 = Example()
# obj1.name = "c"
# obj1.email = "djhdfhdh@jcjfcjhdkj.com"

# print(obj1)
# print(obj1.name)
# print(obj1.email)

# print(obj1.greet())
# print(Example.greet(obj1))


# class Students:
#     def __init__(self, first_name, last_name, age=40):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name + " " + last_name

# student1 = Students("c", "r")
# print(student1.full_name)

# class Students:
#     def __init__(self, first_name, last_name, age=40):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         # self.full_name = first_name + " " + last_name

#     def fullName(self):
#         return self.first_name + " " + self.last_name

# student1 = Students("c", "r")
# print(student1.fullName())

# clsmethod, inheritance(repr + eval), external method (monkey patching), __dict__. 

# from types import MethodType
# import builtins

# def outside(self):
#     return f"{self.first_name} was the caller of this outside method"

# student1.outside = MethodType(outside, student1)

# print(student1.outside())

# def outside_class(self):
#     return f"{self.first_name} was the caller of this outside method"

# Students.outside_class = outside_class

# print(Students.outside_class(student1))


# self-class vars

# class Students:

#     age_increase_amount = 1

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         # self.full_name = first_name + " " + last_name

#     def fullName(self):
#         return self.first_name + " " + self.last_name

#     def changeAge(self):
#         self.age = self.age + self.age_increase_amount

# student1 = Students("c", "r", 10)
# student2 = Students("a", "b", 10)
# print(student1.__dict__)
# print(student2.__dict__)
# student1.changeAge()
# print(student1.__dict__)
# print(student2.__dict__)
# student2.age_increase_amount = 20
# student2.changeAge()
# print(student1.__dict__)
# print(student2.__dict__)
# print(Students.__dict__)

# non self class vars

# class Students:
#     __num_of_students = 0 
#     age_increase_amount = 1

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         # self.full_name = first_name + " " + last_name
#         Students.__num_of_students += 1

#     def fullName(self):
#         return self.first_name + " " + self.last_name

#     def changeAge(self):
#         self.age = self.age + self.age_increase_amount

#     @classmethod
#     def get_num_of_students(cls):
#         return cls.__num_of_students 

# print(Students.get_num_of_students())

# student1 = Students("c", "r", 10)
# student2 = Students("a", "b", 10)

# print(Students.get_num_of_students())
# print(Students._Students__num_of_students)

# inheritance:

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        print(f"{self.name} as an animal eats")

    def __str__(self):
        return f"Animal({self.name}, {self.species})"

    # def __repr__(self):
    #     return f"Animal({self.name!r}, {self.species!r})"

# a = Animal("a", "b")

# print(a)

# b = eval(repr(a))  # runs a single line of python code
# print(b)

# class Cat(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

#     # @Override
#     def eat(self):
#         print(f"{self.name} as an cat eats")

#     def __str__(self):
#         return super().__str__() + f"{self.__class__.__name__}-{self.__dict__}-{self.breed}"

# cat1 = Cat("a", "b", "c")
# print(cat1)
# cat1.eat()

TODO:

- Simple class design:
    1. Create a Rectangle class with attributes length and width. 
    Add methods to calculate the area and perimeter of the rectangle. 

    2. Create a BankAccount class with attributes account_number and balance. 
    Add methods to deposit and withdraw money from the account. 

    3. Create a Car class with attributes make, model, and year. 
    Add methods to get and set the values of the attributes. 

    4. Create a Product class with attributes name, price, and quantity. 
    Add methods to calculate the total value of the product (price * quantity) 
    and add or remove items from the product inventory. 

- Class lab
- RPS class based design.
- Research/reading/revision
- fix broken script practice. 
- finish previous tasks. 

# ADVANCED:

from abc import ABC, ABCMeta, abstractmethod
from datetime import datetime, timedelta
from enum import Enum, auto


# Enum for Library Item Types
class ItemType(Enum):
    BOOK = auto()
    JOURNAL = auto()

# Singleton Class for LibrarySystem
class LibrarySystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LibrarySystem, cls).__new__(cls)
        return cls._instance

# Subclass ABCMeta to avoid metaclass conflicts
class LibraryItemMeta(ABCMeta):
    def __new__(cls, name, bases, attrs):
        if 'get_details' not in attrs or not callable(attrs['get_details']):
            raise TypeError(f"Missing or non-callable 'get_details' method in {name}")
        return super().__new__(cls, name, bases, attrs)


class LibraryItem(ABC, metaclass=LibraryItemMeta):
    def __init__(self, title, creation_date, author, item_type):
        self.title = title
        self.creation_date = creation_date
        self.author = author
        self.item_type = item_type

    @abstractmethod
    def get_details(self):
        pass


class ItemAgeMixin:
    def get_age(self):
        return datetime.now() - self.creation_date


class Book(ItemAgeMixin, LibraryItem):
    def __init__(self, title, creation_date, author, series=None, edition=None):
        super().__init__(title, creation_date, author, ItemType.BOOK)
        self.series = series
        self.edition = edition

    def get_details(self):
        details = f"Book: {self.title} by {self.author}"
        if self.series:
            details += f", Series: {self.series}"
        if self.edition:
            details += f", Edition: {self.edition}"
        return details


class Journal(ItemAgeMixin, LibraryItem):
    def __init__(self, title, creation_date, author, frequency=None):
        super().__init__(title, creation_date, author, ItemType.JOURNAL)
        self.frequency = frequency

    def get_details(self):
        details = f"Journal: {self.title} by {self.author}"
        if self.frequency:
            details += f", Frequency: {self.frequency}"
        return details


class LibraryItemFactory:
    @staticmethod
    def create_item(item_type, title, creation_date, author, **kwargs):
        if item_type == ItemType.BOOK:
            builder = BookBuilder(title, creation_date, author)
            if 'series' in kwargs:
                builder.with_series(kwargs['series'])
            if 'edition' in kwargs:
                builder.with_edition(kwargs['edition'])
            return builder.build()

        elif item_type == ItemType.JOURNAL:
            builder = JournalBuilder(title, creation_date, author)
            if 'frequency' in kwargs:
                builder.with_frequency(kwargs['frequency'])
            return builder.build()

        else:
            raise ValueError("Invalid item type")


# Builders
class BookBuilder:
    def __init__(self, title, creation_date, author):
        self.title = title
        self.creation_date = creation_date
        self.author = author
        self.series = None
        self.edition = None

    def with_series(self, series):
        self.series = series
        return self

    def with_edition(self, edition):
        self.edition = edition
        return self

    def build(self):
        return Book(self.title, self.creation_date, self.author, self.series, self.edition)


class JournalBuilder:
    def __init__(self, title, creation_date, author):
        self.title = title
        self.creation_date = creation_date
        self.author = author
        self.frequency = None

    def with_frequency(self, frequency):
        self.frequency = frequency
        return self

    def build(self):
        return Journal(self.title, self.creation_date, self.author, self.frequency)


class BookShelf(ItemAgeMixin):
    capacity = 100

    def __init__(self, creation_date):
        self.creation_date = creation_date
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        for item in self.items:
            print(f"{item.item_type.name}: {item.get_details()}")


# Example Usage
bookshelf = BookShelf(creation_date=datetime(2022, 1, 1))

# Adding Books
book_builder = BookBuilder("The Great Gatsby", datetime(1925, 4, 10), "F. Scott Fitzgerald")
book = book_builder.with_edition("First").with_series("Classics").build()
bookshelf.add_item(book)

# Adding Journals
journal_builder = JournalBuilder("Nature", datetime(2021, 5, 12), "Various Authors")
journal = journal_builder.with_frequency("Monthly").build()
bookshelf.add_item(journal)

# Adding Items Using the Factory
factory_book = LibraryItemFactory.create_item(
    ItemType.BOOK, "1984", datetime(1949, 6, 8), "George Orwell", series="Dystopian", edition="Second")
factory_journal = LibraryItemFactory.create_item(
    ItemType.JOURNAL, "Science", datetime(2022, 7, 1), "Various Authors", frequency="Weekly")

bookshelf.add_item(factory_book)
bookshelf.add_item(factory_journal)

# Print Items on Bookshelf
print("\nItems on the bookshelf:")
bookshelf.get_items()


# Dynamic class generation: 

def create_model(name, fields):
    def __init__(self, **kwargs):
        for field_name, default_value in fields.items():
            setattr(self, field_name, kwargs.get(field_name, default_value))

    def __repr__(self):
        field_strings = [f"{k}={getattr(self, k)!r}" for k in fields]
        return f"{name}({', '.join(field_strings)})"

    return type(name, (object,), {
        "__init__": __init__,
        "__repr__": __repr__,
    })


user_schema = {
    "name": "",
    "email": "",
    "is_admin": False,
}

User = create_model("User", user_schema)


user1 = User(name="chris", email="chris@chris.com", is_admin=True)
print(user1)


challenges solutions:

#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

#class Rectangle:
#    def __init__(self, length, width)
#        self.length = length
#        self.width = width

#    def area(self):
#        return self.length * self.width
    
 #   def perimeter(self):
 #       return 2 * (self.length + self.width)

#rect = Rectangle(5, 10)
#print(rect.area())
#print(rect.perimeter())        

#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account. 

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

acct = BankAccount("1234")

print(acct.get_balance())
acct.deposit(100)
print(acct.get_balance())
acct.withdraw(50)
print(acct.get_balance())
acct.withdraw(1000)




#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

car = Car("ford", "focus", 2000)

print(car.get_make())
print(car)
car.set_make("toyota")
car.set_model("pickup")
car.set_year(2005)
print(car)

#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def add_items(self, quantity):
        self.quantity += quantity

    def remove_items(self, quantity):
        if quantity > self.quantity:
            print("not enough stock")
        else:
            self.quantity -= quantity

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"


prod = Product("macbook", 1000, 5)

print(prod.total_value())
prod.add_items(5)
print(prod.quantity)
prod.remove_items(9)
print(prod.quantity)
print(prod) 


lab:

# Task 2

class Students:
    def __init__(self, name, age, class_="classroom"):
        self.name = name
        self.age = age
        self.class_ = class_

    def average_test_score(self, score_1, score_2, score_3):
        x = (score_1 + score_2 + score_3) /300 * 100
        return f"{self.name} - avergae test score is {x}%"
    
student_1 = Students("person", 5)

print(student_1.average_test_score(20, 60, 60))

# task 2 - improved:

class Students:
    def __init__(self, name, age, class_="classroom"):
        self.name = name
        self.age = age
        self.class_ = class_

    def average_test_score(self, scores):
        total_score = sum(scores)
        average_percentage = total_score / (len(scores) * 100) * 100
        return f"{self.name} - average test score is {average_percentage}%"

student_1 = Students("person", 5)
print(student_1.average_test_score([20, 60, 60]))


# task 3

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} cm")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"

class Owl(Bird):
    def __init__(self, name, wingspan, nocturnal=True):
        super().__init__(name, wingspan)
        self.nocturnal = nocturnal

    def hoot(self):
        print(f"{self.name} is hooting")

    def __str__(self):
        return super().__str__() + f" - nocturnal: {self.nocturnal}"
    
class Dodo(Bird):
    def __init__(self, name, wingspan, extinct=True):
        super().__init__(name, wingspan)
        self.extinct = extinct

    def __str__(self):
        return super().__str__() + f" - extinct: {self.extinct}"
    


bird1 = Bird("eagle", 20)
owl1 = Owl("barn owl", 90)
dodo1 = Dodo("the dodo", 100)


bird1.fly()
print(bird1)

owl1.fly() 
owl1.hoot()
print(owl1)

dodo1.fly()
print(dodo1)


# improved:

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} cm")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}), {id(self)}, {self.__dict__}"

class Owl(Bird):

    nocturnal = True

    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)

    def hoot(self):
        print(f"{self.name} is hooting")

    def __str__(self):
        return super().__str__() + f" - nocturnal: {self.nocturnal}"
    
class Dodo(Bird):

    extinct = True

    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)
        
    def fly(self):
        print(f"{self.name} doesnt fly")

    def __str__(self):
        return super().__str__() + f" - extinct: {self.extinct}"
    


bird1 = Bird("eagle", 20)
owl1 = Owl("barn owl", 90)
dodo1 = Dodo("the dodo", 100)


bird1.fly()
print(bird1)

owl1.fly() 
owl1.hoot()
print(owl1)

dodo1.fly()
print(dodo1)