from car import Car
import math
from advance.simple import sum

sum(1, 2)


class Student:
    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


car1 = Car("BMW-SX", "2030", "black", False)

print(car1)
car1.model
car1.year
car1.color
car1.for_sale

car1.drive()

car2 = Car("Mustang", "2025", "yellow", True)

car2.drive()
car2.color

car2.stop()
car2.describe()

student1 = Student("John Wick", 35)
student2 = Student("Chien Lee", 36)
student2.class_year
student1.name
student2.name

student1.age
student2.age

Student.class_year
Student.num_students

print(
    f"Student Name: {student1.name} Age: {student1.age} Year: {Student.class_year} Total.no.of.students: {Student.num_students}"
)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Mouse(Animal):
    def speak(self):
        print("Squeek!")


dog = Dog("jimmy")
cat = Cat("Tom")
mouse = Mouse("Jerry")

dog.name
cat.name
mouse.name

dog.speak()

mouse.is_alive
mouse.eat()

cat.speak()

dog.sleep()


mouse.speak()
dog.is_alive


class Shape:
    number_of_shapes = 0

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def printingInfo(self, name):
        print(f"NAME: {name}")

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  # pass args to the parent constructor
        self.radius = radius

    def describe(self):
        print(f"The radius of the circle is {math.pi * (self.radius**2):.2f}cm^2")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width, name):
        super().__init__(color, is_filled)
        super().printingInfo(name)
        Shape.number_of_shapes += 2
        self.width = width

    def describe(self):
        print(f"Its an square with an area of {self.width * self.width}cm^2")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"Its an Triagne with an area of: {self.width * self.height / 2}cm^2")
        super().describe()


circle = Circle("Yellow", True, 8)

square = Square("red", False, 300, "ppl_call_me_hk")

triangle = Triangle(color="Orange", is_filled=True, width=300, height=500)


circle.color
circle.is_filled
circle.radius

square.color
square.is_filled
square.width


triangle.color
triangle.is_filled
triangle.width
triangle.height

Shape.number_of_shapes

circle.describe()
square.describe()
triangle.describe()


class Car:
    def turn_on(self):
        print("You can start the engine")
        return self

    def drive(self):
        print("You can drive")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You can turn off the engine")
        return self


c1 = Car()

c1.turn_on().drive().brake().turn_off()


def add_prefix(mul):
    print(f"Allowing additional params: {mul}")

    def addition(originalFn):
        print("Decorator function")

        def inner_fun(*args, **kwargs):
            print("Started adding wait!!")
            res = originalFn(*args, **kwargs) * mul
            return res

        return inner_fun

    return addition


tupleee = list(0, 1, 1)

tupleee[0]


@add_prefix(10)
def add(x, y):
    sum = x + y
    print(f"Addition: {sum}")
    return sum


add(10, 20)
