"""
Define a base classe and create 2 subclasses, Dog & Cat, 
each with own behaviour.
"""
class Animal:
    def __init__(self, name:str) -> None: #Annotations included for documentation
        self.name = name

    def make_sound(self):
        return "Make a random sound"
    
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: Woof, woof!"
    
    def fetch(self):
        return f"{self.name} is fetching a ball!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow, meow!"
    
    def scratch_furniture(self):
        return f"{self.name} is scratching the furniture!"

# Create instances of Dog and Cat Classes
buddy = Dog("Buddy")
whiskers = Cat("Whiskers")

# Using the make_sound method from the base class Animal
print(buddy.make_sound())  # Output: Buddy barks: Woof, woof!
print(whiskers.make_sound())  # Output: Whiskers meows: Meow, meow!

# Using subclass-specific methods
print(buddy.fetch())
print(whiskers.scratch_furniture())

# Get instances of Dog Class
my_dogs = []
buddy = Dog("Buddy")
my_dogs.append(buddy)
rex = Dog("Rex")
my_dogs.append(rex)
amber = Dog("Amber")
my_dogs.append(amber)

total_dogs = len(my_dogs)

dogs_info = [dog.name for dog in my_dogs]
print(dogs_info)
"""
Multiple Inheritance Example
"""
class Vehicle:
    def __init__(self, brand) -> None:
        self.brand = brand

    def drive(self):
        return f"{self.brand} is driving"
    
class Electric:
    # def __init__(self) -> None: # Default constructor when no __init__ included
    #     pass

    def charge(self):
        return "Charging the electric vehicle"
    
class HybridCar(Vehicle, Electric):
    def __init__(self, brand, fuel_type) -> None:
        # Call the constructors of both parent classes
        Vehicle.__init__(self, brand)
        Electric.__init__(self)

        self.fuel_type = fuel_type

    def drive(self):
        return f"{self.brand} {self.fuel_type} is driving"
    
# Create an instance
hybrid_car = HybridCar("Toyota", "Hybrid")

# Use methods from Vehicle
print(hybrid_car.drive())   # Output: Toyota Hybrid is driving.

# Use methods from Electric
print(hybrid_car.charge())  # Output: Charging the electric vehicle.

"""=============================
Method Overriding example
"""
class Animal:
    def make_sound(self):
        return "Generic animal sound"

    def move(self):
        return "Animal is moving"

class Dog(Animal):
    def make_sound(self):
        return "Woof, woof!"

    def fetch(self):
        return "Dog is fetching the ball"

class Cat(Animal):
    def make_sound(self):
        return "Meow, meow!"
    
    def climb_tree(self):
        return "Cat is climbing the tree"

# Creating instances 
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Using methods from Animal class
print(generic_animal.make_sound())  # Output: Generic animal sound
print(generic_animal.move())        # Output: Animal is moving

# Using overridden make_sound methods
print(dog.make_sound())             # Output: Woof, woof!
print(cat.make_sound())             # Output: Meow, meow!

# Using additional methods in subclasses
print(dog.fetch())                  # Output: Dog is fetching the ball
print(cat.climb_tree())             # Output: Cat is climbing the tree

# Using additional methods in subclasses
print(dog.move())             # Output: Animal is moving
print(cat.move())             # Output: Animal is moving

"""
We can address the super(), isinstance() & issubclass() functions 
in the open class. This will include the __str__ as addressed with a learner.
"""