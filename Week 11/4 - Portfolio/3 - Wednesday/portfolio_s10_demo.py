# Animal interact option
class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat

    def display_info(self):
        return f"{self.name} ({self.species}) lives in {self.habitat} habitat."

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

class Penguin(Animal):
    def make_sound(self):
        return "Honk!"

# Virtual Zoo
lion = Lion(name = "Leo", species = "African Lion", habitat = "Savannah")
elephant = Elephant(name = "Ellie", species = "African Elephant", habitat = "Jungle")
penguin = Penguin(name = "Penny", species = "Emperor Penguin", habitat = "Antarctica")

# User Interface
def interact_with_animal(animal):
    print(animal.display_info())
    print(f"The {animal.species} says: {animal.make_sound()}\n")

print("Welcome to the Virtual Zoo!\n")

while True:
    print("Choose an animal to interact with:")
    print("1. Lion")
    print("2. Elephant")
    print("3. Penguin")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        interact_with_animal(lion)
    elif choice == "2":
        interact_with_animal(elephant)
    elif choice == "3":
        interact_with_animal(penguin)
    elif choice == "4":
        print("Thank you for visiting the Virtual Zoo. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.\n")
