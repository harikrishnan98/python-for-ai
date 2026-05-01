from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, toppings, radius):
        self.toppings = toppings
        super().__init__(radius)


# Each class (circle,square,triangle) - have two forms - Its also have Shape class and its own class(Square, or Circle or Triangle)

# pizza class is inherits from the circle class , Circle class inherits from the Shape class

# So our pizza have three forms:

# Its consider as Pizza, Also consider as Circle and its also consider as Shape -> This is known as Polymorphism in Inheritance
shapes = [Circle(4), Square(5), Triangle(7, 10), Pizza("cheesebust", 60)]

for shape in shapes:
    print(f"{shape.area()}cm²")


## Duck typing


class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("MEOW")


class Car:
    alive = False

    def speak(self):
        print("HONK!!")


animals_1 = [Dog(), Cat(), Car()]

for animal in animals_1:
    animal.speak()
    print(animal.alive)

# Now the Car Object doesn't have minimum neccessary attributes or methods

# Since it have horn() method not speak() method, after we renamed the honk() method to speak() its works

# Car Object doesn't have alive attribute

# If we add that alive attribute

# Car Object must have minimum neccessary attributes and methods to be consider as Animal class Object
