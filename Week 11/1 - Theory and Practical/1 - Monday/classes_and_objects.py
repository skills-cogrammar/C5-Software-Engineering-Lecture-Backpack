# Basic class wiht class variable
class Person:
    name = "John"

# person1 = Person()
# print(person1.name)
# person1.name = "Jack"
# print(person1.name)



class Person:
    
    def __init__(self, name):
        self.name = name

# person1 = Person("Michelle")
# print(person1.name)
# person2 = Person("Sahra")
# print(person2.name)
# names = []
# people = [Person(name) for name in names]


class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}!")

person1 = Person("Steven")
person1.greet()
person1.name = "Carl"
person1.greet()

def person_do_greet(person):
    person.greet()

person_do_greet(person1)


class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.subjects = []
        self.grades = []

    def display_profile(self):
        profile = f"Student Name: {self.name} {self.surname}\n\n"
        profile += "Subject\t\t\tGrade\n"
        for subject, grade in zip(self.subjects, self.grades):
            profile += f"{subject}\t\t\t{grade}\n"
        profile += f"\nAverage: {self.get_average()}\n"
        print(profile)
        

    def get_average(self):
        return sum(self.grades)/len(self.grades)


# from random import randint
   
# student1 = Student("Jack", "Black")
# student2 = Student("Claire", "Steward")
# student3 = Student("Peter", "Johnson")

# students = [student1, student2, student3]

# # Adding subjects and grades
# subjects = ("English", "Physics", "History")
# for student in students:
#     student.subjects = [subject for subject in subjects]
#     student.grades = [randint(60,90) for _ in range(3)]

# for student in students:
#     student.display_profile()


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    

# rectangle1 = Rectangle(5, 9)
# print(f"Area of rectangle is {rectangle1.area()}")
# print(f"Perimeter of rectangle is {rectangle1.perimeter()}")

# rectangle2 = Rectangle(12, 15)
# print(f"Area of rectangle is {rectangle2.area()}")
# print(f"Perimeter of rectangle is {rectangle2.perimeter()}")

# rect1_area = rectangle1.area
# print(rect1_area())


new_rectangle = Rectangle 

my_rectangle = new_rectangle(5, 8)
print(my_rectangle.area())