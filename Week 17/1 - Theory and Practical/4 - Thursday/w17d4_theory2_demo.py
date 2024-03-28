""" ==================================
local variables and class attributes
"""
class MyClass:
    def __init__(self, name):
        print(f"self => >{self}<")          # the instance in memory
        """ 
        self represents a box in memory that will contain smaller boxes of
        attributes and functions (methods).
		The label on the box will be the variable name that we declare as 
        a MyClass object. We must therefor open the bigger box before we can 
        access the attributes and methods.
        """
        print(f"name => {name}")            # the input name value
        
        # print(f"self.name => {self.name}")  # the instance name value
        self.name = name
        print(f"self.name => {self.name}")


    def greet_and_update(self, new_name):
        local_variable = "I'm a local variable"
        print(f"Hello, {self.name}!")       # the instance name value
        print(local_variable)
        
        # Updating the instance variable with the new_name parameter
        self.name = new_name        # John is overwritten with Alice.

# Creating an instance of MyClass
my_instance = MyClass("John")       # Passed to name class input
"""
# my_instance = "John"  
For my_instance = "John" # This will declare my_instance as a Str object since 
this is the default for the value format "John". So to overwrite the default we
need to add the replacement class name MyClass.
"""
# Calling the greet_and_update method
my_instance.greet_and_update("Alice")     #Passed to new_name class input

# Accessing the updated name
print(f"Updated name: {my_instance.name}")

""" ==================================
Access Modifiers
"""
# ================ 1. Public Attribute
"""
Accessible from outside the class or module.
Part of the public interface.
"""
class MyClass:
    def __init__(self):
        self.public_variable = "Accessible Everywhere"

# Creating an object of MyClass
my_object = MyClass()

# Accessing the public variable from outside the class
print(my_object.public_variable)

# ================ 2. Protected Attribute
"""
No name mangling is applied.
Conventional indication that the variable is for internal use.
Still accessible from outside the class.
"""
class MyClass:
    def __init__(self):
        self._protected_variable = "Limited Access"

# Creating an object of MyClass
my_object = MyClass()

# Accessing the protected variable from outside the class
print(my_object._protected_variable)

# ================ 3. Private Attribute
"""
Name mangling is applied.
Accessible with a mangled name from outside the class.
Not a strict access control mechanism, more of a convention.
"""
class MyClass:
    def __init__(self):
        self.__private_variable = "Secret"

# Accessing the private variable from outside the class
my_object = MyClass()

# print(my_object.__private_variable)             # Note this code gives error
print(my_object._MyClass__private_variable)       # Name mangling must be applied

""" ==================================
Getter Methods:

Getter methods, are used to retrieve the values of private or protected attributes.
They provide read-only access to the internal state of an object.
The naming convention for a getter method is typically get_attribute(), ie. get_value
"""
class MyClass:
    def __init__(self):
        self._value = 42

    def get_value(self):
        return self._value

# Creating an object of MyClass
my_object = MyClass()

# Using the getter method to access the value
print(my_object.get_value())  # Output: 42

"""
Setter Methods:

Setter methods, are used to modify the values of private or protected attributes.
They provide a way to control the modification of internal state and 
enforce validation rules. The naming convention for a setter method is 
typically set_attribute().
"""
class MyClass:
    def __init__(self):
        self._value = 42

    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# Creating an object of MyClass
my_object = MyClass()

# Using the setter method to modify the value
my_object.set_value(50)

"""
Setter & Getter combination to run.
"""
class MyClass:
    def __init__(self):
        self._value = 42

    # Getter Method:
    def get_value(self):
        return self._value
    
    # Setter Method:
    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# Creating an object of MyClass
my_object = MyClass()

# Using the getter method to access the value
print(my_object.get_value())

# Using the setter method to modify the value
my_object.set_value(50)

# Using the getter method to access the modified value
print(my_object.get_value())

# === Changing private attribute value with setter method
class MyClass:
    def __init__(self):
        self.__private_variable = "Secret"

    def set_private(self, new_private):
        if new_private > 0:
            self.__private_variable = new_private

# Accessing the private variable from outside the class
my_object = MyClass()

# print(my_object.__private_variable)           # Note this code gives error
print(my_object._MyClass__private_variable)      # Name mangling must be applied

# The below will not change the private variable but create a new attribute
# my_object.__private_variable = "No more secret"  
 
# Using the setter method to modify the value
my_object.set_private("No more secret")

""" ==================================
A class called Person with a custom dunder method __call__. 
The __call__ method allows instances of the class to be called 
as if they were functions.
"""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}!"

    def __call__(self, other_person):
        return f"{self.name} says: Hi, {other_person.name}!"

# Creating instances of Person
alice = Person("Alice")
bob = Person("Bob")

# Using the greet method
print(alice.greet())  # Output: Hello, my name is Alice!
print(bob.greet())    # Output: Hello, my name is Bob!

# Using the __call__ method, allowing instances to be called like functions
print(alice(bob))  # Output: Alice says: Hi, Bob!
print(bob(alice))  # Output: Bob says: Hi, Alice!

print(alice.__call__(bob))
