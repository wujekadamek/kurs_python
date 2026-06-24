import random

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None

    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldOfStudy = ["IT", "Math", "Robotics"]

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentsList.append(student)
            student.schoolName = self.name
            student.fieldOfStudy = random.choice(self.fieldOfStudy)

    def printSchoolInfo(self):
        print("School name:", self.name, "city:", self.city)
        print("Students:")
        for el in self.studentsList:
            el.printInfo()

student1 = Student("Karol", "Wojtyla", "21", "Wadowice")
student1.schoolName = "Przedszkole Publiczne nr 2137"
student1.country = "Watykan"
student1.printInfo()
print(student1.country)

student2 = Student("Adam", "Kowalski", 37, "Krakow")

school = School("Tech School", "Wadowice")
school.addStudent(student1)
school.addStudent(student2)
print()
school.printSchoolInfo()