""" ==================================
Single Responsibility:

If we have a person class that can have a pet, 
we won't add all the pet attributes to the person class. 
We will rather create a new class.
""" 
class Person:

    # Remember: In the same way that we applied annotations to functions
        # we can do the same for methods. Note -- -> None
    def __init__(self, name: str, surname: str, pet_name: str, pet_type: str) -> None:
        self.name = name
        self.surname = surname
        self.pet_name = pet_name
        self.pet_type = pet_type
    # Above class does not have a single responsibility
        
# Better implementation
class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.pet = None  # Initialize the pet attribute to None

    # Order of classes can be helpful. Note the undefined Pet annotation below
        # if Person class is above the Pet class: Switch classes to resolve
    def assign_pet(self, pet_instance: Pet) -> None:  
        self.pet = pet_instance

class Pet:
    """
    Represents a virtual pet.

    Attributes: 
    - pet_name (str): The name of the pet
    - pet_type (str): The type of breed of the pet
    """
    def __init__(self, pet_name: str, pet_type: str) -> None:
        """
        Initialize a Pet object with a name and type.

        Parameters:
        - pet_name (str): The name of the pet
        - pet_type (str): The type of breed of the pet
        
        Returns:    None
        """
        self.pet_name = pet_name
        self.pet_type = pet_type

    # def display_pet(self) -> str:
    #     return f"{self.pet_name} the {self.pet_type}"

    # alternative to above which we will deal with later
    # print(f"Pet: {person_1.pet}") in main code will work if we have __str__
        
    # def __str__(self):
    #     return f"{self.pet_name} the {self.pet_type}"
    
""" It is important to realise that method names with leading and trailing __
are special methods and they are part of Python's data model. The init in 
__init__ cannot be changed to something else."""

# Creating instances of the classes
person_1 = Person("John", "Here-again")
pet_1 = Pet("Buddy", "Dog")

# Connecting the pet to the person
person_1.assign_pet(pet_1)

# Accessing attributes of the instances
print(f"Person: {person_1.name} {person_1.surname}")
print(f"Pet: {person_1.pet.pet_name} the {person_1.pet.pet_type}")

print(f"Pet: {person_1.pet}")    # This object in itself is not readable without __str__
# For now we have to code a method that can display this for us.
# print(f"Pet: {person_1.pet.display_pet()}")
