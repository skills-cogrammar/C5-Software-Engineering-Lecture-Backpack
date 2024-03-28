# Special methods init, str, repr
class MyLaptop:
    def __init__(self, brand1, serial_number1, screen_size1) -> None:
        self.brand2 = brand1
        self.serial_number2 = serial_number1
        self.screen_size2 = screen_size1

    def __str__(self):      # User representation
        str_rep = f"Brand: {self.brand2}\nSerial: {self.serial_number2}\n"
        str_rep += f"Screen Size: {self.screen_size2}\n"
        return str_rep
    
    def __repr__(self):     # Developer representation
        pass

# How to use
my_laptop = MyLaptop("Asus", "ASH123", "17")
print(my_laptop)              # Use __str__ special method - Auto Call

str_laptop = str(my_laptop)     # Use str casting
print(str_laptop)

# ===========================================

# MyNumber class with special methods __init__, __str__, and __add__
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # Custom string representation for print function
        return str(self.value)
    
    def __add__(self, other):
        # Custom addition operation
        print("==> __add__ method")
        return MyNumber(self.value + other.value)

# Creating instances of MyNumber and performing addition
num1 = MyNumber(25)
num2 = MyNumber(14)
num3 = num1 + num2  # Uses the __add__ method
print(num1)
print(num2)
print(num3)
           
numbers = [25, 14]
numbers.append(num1)
numbers.append(num2)

my_count = len(numbers)

# ===========================================

# ContactList class with special methods __init__, __str__, and __len__
class ContactList:
    def __init__(self, value):
        self.contact_list = []

    def __str__(self):
        # Custom string representation for print function
        return str(self.value)
    
    def __len__(self):
        return len(self.contact_list)
    
contact_list = ContactList()
contacts_count = len(contact_list)
