class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(
            name, position
        )  # self - this company object - that have Employee class Object
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


c1 = Company("ZeroStack MNC")

c1.company_name

c1.add_employee("John Matt", "Software Engineer")
c1.add_employee("Mickey", "Team Lead")
c1.add_employee("Hari", "Director")

c1.list_employees()
c1.employees[0].position

for emp in c1.list_employees():
    print(emp)


c2 = Company("HackStack LTD")

c2.add_employee("Mathew", "Manager")
c2.add_employee("Wick", "CEO")

c2.list_employees()

for emp2 in c2.list_employees():
    print(emp2)
