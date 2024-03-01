""" 
Below is how == Method OverLoading == is supposed to work.
This is however NOT SUPPORTED by Python since there are many alternatives.
"""
class MathOperations:
    def add(self, a, b):
        return a + b

    #Since Python does not support overloading, overwriting is applied here.
    def add(self, a, b, c):
        return a + b + c

# Create an instance of the MathOperations class
math_instance = MathOperations()

# Call the add method with different numbers of arguments
result_2_params = math_instance.add(2, 3)           # Calls the first add method
result_3_params = math_instance.add(2, 3, 4)        # Calls the second add method

print(result_2_params)  # Output: 5
print(result_3_params)  # Output: 9

# ========== 1st Alternative to the above - using default values
class MathOperations:
    def add(self, a, b, c = 0):
        return a + b + c

# Create an instance of the MathOperations class
math_instance = MathOperations()

# Call the add method with different numbers of arguments
result_2_params = math_instance.add(2, 3)      # Calls the first add method
result_3_params = math_instance.add(2, 3, 4)   # Calls the second add method

print(result_2_params)  # Output: 5
print(result_3_params)  # Output: 9

# ========== 2nd Alternative to the above - using *args
class MathOperations:
    def add(self, *args):
        if len(args) >= 2:
            numbers = [num for num in args]
            result = sum(numbers)
            return result
        else:
            raise ValueError("Invalid number of arguments")

# Create an instance of the MathOperations class
math_instance = MathOperations()

# Call the add method with different numbers of arguments
result_2_params = math_instance.add(2, 3)           # Calls the add_two method
result_3_params = math_instance.add(2, 3, 4)        # Calls the add_three method

print(result_2_params)  # Output: 5
print(result_3_params)  # Output: 9

"""
# ========= Learner question on how *args work ================
# Define ---
*args = unknown number of arguments   
name, age, grade

**kwargs = unknown number of keyword arguments
name = "John", age = 100, grade = "Galactic Genius"

# Declare ---
def my_function(*args, **kwargs):
    pass
    
# Call function
my_function()           # args and kwargs will be empty lists
my_function(1, 2)       # args will have 2 instances in the list
my_function(1, 2, num3 = 5, num4 = 6) #args and kwargs will each have 2 instances
"""

#===========================  BATS    ===========================
"""
Using super() function for double inheritance of subclasses
"""
class Animal:
    def __init__(self, species: str = "") -> None:
        self.species = species

    def make_sound(self):
        return f"The {self.species} makes a generic sound."

class Mammal(Animal):
    def __init__(self, fur_colour: str, species: str = "Mammal") -> None:
        super().__init__(species)  
        self.fur_colour = fur_colour
        
    def show_colour(self):
        return f"The {self.species} is a {self.fur_colour} colour."
    
    def give_birth(self):
        return f"The {self.species} gives birth to live young."

class Bird(Animal):
    def __init__(self, beak_type: str, species: str = "Bird") -> None:
        super().__init__(species)
        self.beak_type = beak_type
    
    def fly(self):
        return f"The {self.species} is flying with its {self.beak_type} beak."

class Amphibian(Animal):
    def __init__(self, skin_type: str, species: str = "Amphibian", ) -> None:
        super().__init__(species)

        self.skin_type = skin_type

    def jump(self):
        return f"The {self.species} jumps with it's {self.skin_type} skin."
    
class Bat(Mammal, Bird):
    def __init__(self, fur_colour: str, beak_type: str, species: str = "Bat") -> None:
        # Use super() to call constructors of parent classes
        Mammal.__init__(self, fur_colour, species)
        Bird.__init__(self, beak_type, species)

    def echolocate(self):
        return f"The {self.species} is using echolocation."

# ============ Main Code
# Create instances
mammal_instance = Mammal("golden", "Lion")
bird_instance = Bird("hooked", "Eagle")
amphibian_instance = Amphibian("smooth", "Frog")
bat_instance = Bat("brown", "sharp", "Bat")
# bat_instance = Bat("brown", "sharp") will also work because of Method Overloading

# Display information about animals
print(mammal_instance.make_sound())
print(mammal_instance.show_colour())
print(mammal_instance.give_birth())
print("===============")

print(bird_instance.make_sound())
print(bird_instance.fly())
print("===============")

print(amphibian_instance.make_sound())
print(amphibian_instance.jump())
print("===============")

print(bat_instance.make_sound())
print(bat_instance.echolocate())
print("===============")

"""=============================
Inheritance example for emotional support animals using an abstract method
==> The below is not a pure implementation of "Duck Typing" since subclasses
are at least inheriting the name of the animal from the parent class.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement the make_sound method")

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: Woof, woof!"

    def fetch(self):
        return f"{self.name} is fetching a ball."

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow, meow!"

    def climb_tree(self):
        return f"{self.name} is climbing the tree."

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} chirps: Chirp, chirp!"

    def fly(self):
        return f"{self.name} is flying."

class EmotionalSupportAnimal(Dog, Cat, Bird):   # Extraordinary Support Animals
    def __init__(self, name, support_task):
        # Call the constructors of all parent classes
        Dog.__init__(self, name)
        Cat.__init__(self, name)
        Bird.__init__(self, name)
        self.support_task = support_task

    def provide_support(self):
        return f"{self.name} provides emotional support by {self.support_task}."

# Creating instances
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")
esa_dog = EmotionalSupportAnimal("Rover", "being a loyal companion")

# Using methods from Dog
print(dog.make_sound())  # Output: Buddy barks: Woof, woof!
print(dog.fetch())       # Output: Buddy is fetching a ball.
print(f"{'-' * 30}")

# Using methods from Cat
print(cat.make_sound())    # Output: Whiskers meows: Meow, meow!
print(cat.climb_tree())    # Output: Whiskers is climbing the tree.
print(f"{'-' * 30}")

# Using methods from Bird
print(bird.make_sound())   # Output: Tweetie chirps: Chirp, chirp!
print(bird.fly())          # Output: Tweetie is flying.
print(f"{'-' * 30}")

# Using methods from EmotionalSupportAnimal
print(esa_dog.make_sound())     # Output: Rover barks: Woof, woof!
print(esa_dog.fetch())          # Output: Rover is fetching a ball.
print(esa_dog.climb_tree())     # Output: Rover is climbing the tree. (From Cat class)
print(esa_dog.provide_support())# Output: Rover provides emotional support by being a loyal companion.

