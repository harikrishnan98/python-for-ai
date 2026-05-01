# Aggregation

# Library Object can acts as Whole

# Book Object as a independent parts

# A Library can exist without Books And Books can exists without Library that the main difference between aggregation and composition

# These class are independent on one another and exists without each other


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # This variable will get created when an instance get created and this is instance variable

    def add_book(self, book):
        self.books.append(
            book
        )  # Storing the book from another object to this instance books variable

    def display_book(self):
        return [
            f"Author Name: {book.author} and Title of The Book: {book.title}"
            for book in self.books
        ]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("New York Public Library")

book1 = Book("Harry Potter...", "J.K Rowlings")

book2 = Book("The Hobbit", "J.R.R. Tolkein")

book3 = Book("The Color Of magic", "Terry Patchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.books

print(library.name)
print(library.display_book())

for book in library.display_book():
    print(book)


class Teacher:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, teacher):
        self.teacher = teacher


t1 = Teacher("Hari")
dep = Department(t1)

dep.teacher.name


## Composition


class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(
        self, make, model, horse_power, wheel_size
    ):  # We can't rename params to something different
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)  # Instance variable
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]  # Instance variable

    def display_car_info(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}inches"


# We are not creating objects(Wheels,Engine) outside of the class instead we are doing inside of the class


car1 = Car(make="Fort", model="Mustang", horse_power="8800", wheel_size=18)

car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

car1.display_car_info()
car2.display_car_info()
