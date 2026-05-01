class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"Lets Drive the {self.color} {self.model}")

    def stop(self):
        print(f"Stop the {self.color} {self.model} car")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
