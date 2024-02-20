"""
Use the super() function with single inheritance
"""

class Animal:
    def __init__(self, species: str, name: str) -> None:
        self.species = species
        self.name = name

    def make_sound(self):
        return "Generic Animal Sound"
    
    def get_species_description(self):
        return f"{self.name} is a {self.species}"
    
    def __str__(self):
        return f"{self.species} {self.name}"
    
class Dog(Animal):
    def __init__(self, breed, name) -> None:
        super().__init__("Dog", name)
        self.breed = breed

    def make_sound(self):
        return "Woof"
    
    def get_description(self):
        return super().get_species_description() + f" and a {self.breed} breed"
    
    def __str__(self):
        return f"{self.name} is a {self.breed} {self.species} "
    
class Cat(Animal):
    def __init__(self, colour, name) -> None:
        super().__init__("Cat", name)
        self.colour = colour

    def make_sound(self):
        return "Meow!"
    
    def get_description(self):
        return super().get_species_description() + f" with {self.colour} colour"
    
    def __str__(self):
        return f"{self.name} is a {self.colour} {self.species} "

# - Main Code
# Let's create instances    
dog_instance = Dog("Great Dane", "Scooby Doo")
cat_instance = Cat("Black & White", "Tom")

# Using methods
print(dog_instance.make_sound())
print(cat_instance.make_sound())
print(f"{'=' * 30}")

print(dog_instance.get_description())
print(cat_instance.get_description())
print(f"{'=' * 30}")

print(dog_instance)

# Let's get instances of Dog Class => Note for email task
my_dogs = []

# Here we might want a function that adds dog instances
# buddy = Dog("Lab", "Buddy")
# my_dogs.append(buddy)

# rex = Dog("All Stations", "Rex")
# my_dogs.append(rex)

# amber = Dog("Basenji", "Amber")
# my_dogs.append(amber)

# We need a function to add Dog instances
dog_instance = Dog("Lab", "Buddy")
my_dogs.append(dog_instance)

dog_instance = Dog("All Stations", "Rex")
my_dogs.append(dog_instance)

dog_instance = Dog("Basenji", "Amber")
my_dogs.append(dog_instance)

total_dogs = len(my_dogs)
print(total_dogs)

dogs_info = [[dog.name, dog.breed] for dog in my_dogs]
print(dogs_info)
print(f"{'=' * 30}")


"""
How we can use isinstance and issubclass in coding logic
"""
class Shape:
    def __init__(self, colour) -> None:
        self.colour = colour

    def area(self):
        raise NotImplementedError("Subclasses must implement this area method")

class Circle(Shape):
    def __init__(self, colour, radius) -> None:
        super().__init__(colour)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
class Rectangle(Shape):
    def __init__(self, colour, width, height) -> None:
        super().__init__(colour)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

#Declare Functions
def calculate_total_area(shapes):
    total_area = 0

    for shape in shapes:
        # Check for the current object as an instance of the Shape class
        if isinstance(shape, Shape):
            total_area += shape.area()
        else:
            print("Skipping invalid shape")

    return total_area

# Main Code
# Create instances
circle_instance = Circle("Red", 5)
rectangle_instance = Rectangle("Blue", 4, 6)
triangle_instance = "Invalid shape"

# Calculate the total_area
shapes_list = [circle_instance, rectangle_instance, triangle_instance]

sum_of_area = calculate_total_area(shapes_list)
print(f"Total Area of shapes: {sum_of_area}")


"""=============================
Inheritance example for emotional support animals - As promised 
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Placeholder for the make_sound method

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

class EmotionalSupportAnimal(Dog, Cat, Bird):
    def __init__(self, name, support_task):
        # Call the constructors of both parent classes
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
  