class Laptop:

    def __init__(self, brand, serial_number, screen_size):
        self.brand = brand
        self.serial_number = serial_number
        self.screen_size = screen_size

    def __str__(self):
        str_rep = f"Brand: {self.brand}\nSerial: {self.serial_number}\n"
        str_rep += f"Screen Size: {self.screen_size}\n"
        return str_rep
    
    def __repr__(self):
        return f"Laptop({self.brand},{self.serial_number},{self.screen_size})"

laptop = Laptop("Asus", "ASHDBHS", "17")
str_laptop = str(laptop)
print(str_laptop)



class MyNumber:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        return MyNumber(self.value + other.value)


num1 = MyNumber(25)
num2 = MyNumber(14)
num3 = num1 + num2
# num3 = num1.__add__(num2)
# print(num1)
# print(num2)
# print(num3)




class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
    
    def __add__(self, other):
        length = self.length + other.length
        width = self.width + other.width
        return Rectangle(length, width)
    
    def __sub__(self, other):
        length = self.length - other.length
        width = self.width - other.width
        return Rectangle(length, width)
    
# rect1 = Rectangle(11, 6)
# rect2 = Rectangle(7, 3)
# rect3 = rect1 - rect2
# # print(rect3.get_area())
    


class ContactList:

    def __init__(self):
        self.contact_list = []

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def __getitem__(self, key):
        return self.contact_list[key]
    
    def __len__(self):
        return len(self.contact_list)
    
    def __contains__(self, item):
        for contact in self.contact_list:
            if contact.name == item:
                return True
        return False

class Contact:

    def __init__(self, name):
        self.name = name 

# contact_list = ContactList()
# contact_list.add_contact(Contact("James"))
# contact_list.add_contact(Contact("Joe"))
# print(contact_list[1])
# if "James" in contact_list:
#     print("James is here.")





class Student:

    def __init__(self, fullname, student_number, grades) -> None:
        self.fullname = fullname
        self.student_number = student_number
        self.__grades = grades

    def get_average(self):
        return sum(self.__grades)/len(self.__grades)
    
    def __gt__(self, other):
        return self.get_average() > other.get_average()

    def __ge__(self, other):
        return self.get_average() >= other.get_average()

# student1 = Student("Jack", "Jackson", [88, 68, 78, 78])
# student2 = Student("John", "Johnson", [75, 78, 72, 88])

# # student1.__gt__(student2)
# print(student1.__grades) # Don't do!
# if student1 >= student2:
#     print(f"Student 1 has the greater average!")
# else:
#     print(f"Student 2 has the greater average!")






