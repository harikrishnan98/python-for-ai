class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


e1 = Employee("Yuji", "Manager")
e2 = Employee("Sato", "Lead")
e3 = Employee("Geto", "Cook")

e1.get_info()

e1.is_valid_position("Cook")
Employee.is_valid_position("Cook")


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def init_obj(cls, name, gpa):  # Creating object
        return cls(name.upper(), gpa)

    @classmethod
    def get_count(cls):
        return f"Total number of students {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


Student.get_count()

student1 = Student("Harry", 3.2)
student2 = Student("Peter", 4.3)
student3 = Student("Miles", 4.7)

student4 = Student.init_obj("Morgan", 4.8)

student4.name

student1.get_count()
Student.get_count()
# When we call the @classmethod we can able to access or modify the class data
# Here class variable count
# Instead of using self, we will cls for class method

Student.get_average_gpa()
