class Animal:
    num_of_animal = 0

    def __init__(self, name):
        self.name = name
        Animal.num_of_animal += 1

    def eat(self):
        print(f"{self.name} This animal is eating...")

    def sleep(self):
        print(f"{self.name} This animal is sleeping...")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} This animal is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Predator, Prey):
    pass


rabbit = Rabbit("Bunny")
hawk = Hawk("Tony")
fish = Fish("Nemo")


hawk.eat()
hawk.sleep()

rabbit.flee()
hawk.hunt()
rabbit.sleep()

fish.flee()
fish.hunt()
fish.eat()
fish.sleep()

Animal.num_of_animal

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def type(self):
        print("Type of Vehicle: Manual or Automatic")

    # Normal method of the class
    def horn(self):
        print("Pressed Horn")


class Car(Vehicle):
    def go(self):
        print("Car is Moving")

    def stop(self):
        print("Car is Stopped")

    def type(self):
        pass


class Van(Vehicle):
    def go(self):
        print("Van is Moving")

    def stop(self):
        print("Van is Stopped")


van = Van()

van.go()
van.horn()
van.stop()

car4 = Car()

car4.go()
car4.stop()
car4.horn()
car4.type()
