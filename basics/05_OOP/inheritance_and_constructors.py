class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor!")

    def printPersonData(self):
        print("Person.printPersonData: ", self.name, self.surname, self.city)

person1 = Person("Ola", "Kowalska", "Warszawa")
person1.printPersonData()

class Employee(Person):
    def __init__(self, name, surname, city, companyName, salary):
        Person.__init__(self, name, surname, city)
        self.companyName = companyName
        self.salary = salary

        print("Employee constructor!")

    def printEmployeeData(self):
        print("Employee.printEmployeeData: ", self.name, self.surname, self.companyName, self.salary)

employee1 = Employee("Kasia", "Nowak", "Krakow", "Google", 10000)
employee1.printPersonData()
employee1.printEmployeeData()

class Manager(Employee):
    def __init__(self, name, surname, city, companyName, salary, department):
        Employee.__init__(self, name, surname, city, companyName, salary)
        self.department = department
        print("Manager constructor!")

    def hireEmployee(self):
        print("Hire employee")

    def printManagerData(self):
        print("Manager data:", self.name, self.surname, self.city, self.department)

print()
manager1 = Manager("Ania", "X", "Waw", "Tech Ltd", 15000, "IT")
manager1.printPersonData()
manager1.printEmployeeData()
manager1.printManagerData()
manager1.hireEmployee()