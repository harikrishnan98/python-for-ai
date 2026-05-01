from functools import reduce
import nestedClass


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # This method will customise the behaviour of the print statement, so wheneever our instance of the object priting this method will execute
    # It will return only as string
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # This method will check two objects are equal
    # # other is another book object to compare
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # less than method , it will check less than operator

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # greater than method, it will check greater than operator

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # Customize the addition operator between two objects

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    # Check whether the particular word present in the object attribute or not
    def __contains__(
        self, keyword
    ):  # Lion will be the keyword it will check the book2 obj (book2.title) => "Lion" in book2.title
        return keyword in self.title or keyword in self.author

    # get an item(attribute value) like dict from the object
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            raise ValueError("No such keys are there")


book1 = Book("Hobbit", "JR Tolkein", 310)
book2 = Book("HarryPotter", "JK Rowling", 223)
book3 = Book("The Lion, The Witch and the Wardrobe", "CS Lewis", 172)
book4 = Book("HarryPotter", "JK Rowling", 223)

print(book1)
print(book2 == book4)


# Even though the Object have same Book name, Author name and pages, In python the memory is differnt
# SO it will return false, we can able to change the behaviour using a dunder method

print(book1 < book2)

# We can't use less than between two objects but we can customise it using dunder less than method
# __lt__

# same for greater than > we have __gt__ method
print(book1 > book2)

print(book1 + book2)

# If we want to find the word or keyword from the object attribute
# like this: "Lion" in book2
# Searching for a keyword in an object

print("Lion" in book1)

# Checking the author

print("Rowling" in book2)

print("Lione" not in book4)

# If we want to get an item(attribute value) like dict from the object
# We need to use __getitem__
book1["title"]
book2["author"]
book3["num_pages"]
book4["audio"]

"a" + 5

print(type(10))
print(type(int))


class User:
    def __setattr__(self, key, value):
        if key == "age" and value < 0:
            raise ValueError("Age cannot be negative")
        super().__setattr__(key, value)


u = User()
u.age = -1
print(u.age)


# Property decorator


class Rectange:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            raise ValueError("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectange(3, 4)
rectangle.width
rectangle.height

rectangle.width = 0
rectangle.height = 0

del rectangle.width
del rectangle.height

rectangle.width = 14

rectangle._width
# We are using getters method

# Using property decorator when reading these attributes of width or height
# We can write some additional logic
# I need to display only one digit after the decimal then add cm


# Using setter methods we can add additional logic when writing or changing one of these attributes
class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age


t = Test("HK", 29)

t.age

del t.name

t.name = "MK"

t.name

(happy := True)

(age := t.age) > 19

if (ux := age) and t.age > 20 and t.name == "HK":
    print(ux)

while (text := input("Enter the fav book")) != "Exit":
    print(text)

nums = [1, 2, 3, 4, 5, 6, 7]


lit = [n for n in nums if (y := n * n) > 5]

num1 = reduce(lambda acc, x: acc * x, nums)

print(__name__)
print(nestedClass.__name__)
