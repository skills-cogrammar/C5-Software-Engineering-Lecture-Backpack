# Single Responsibility
class UserAuthentication:
    def authenticate(self, username, password):
        # Code for user authentication
        pass

class UserDataManager:

    def __init__(self):
        self.users = []   

    def create_user(self, user_data):
        new_user = User(user_data[0], user_data[1])
        self.users.append(new_user)

    def update_user(self, user_id, new_data):
        # Code for updating user data
        pass   

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password



# Open-closed principle
# class Animal:

#     def __init__(self, type):
#         self.type == type
#         if type == "Lion":
#             self.sound = "Rawr"
#         elif type == "Dog":
#             self.sound = "Woof"

class Animal:

    def __init__(self, animal_type, sound):
        self.type = animal_type
        self.sound = sound

    def make_sound(self):
        pass


class Lion(Animal):
    def __init__(self):
        super().__init__("Lion", "Rawr")


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "Woof")
        
    

animal = Lion()

# Liskov substitution

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Lion(Animal):
    def make_sound(self):
        print("The Lion goes Rawr!")

class Dog(Animal):
    def make_sound(self):
        print("The dog goes woof")

class Cat(Animal):
    def make_sound(self):
        print("The cat goes meow")

def animal_make_sound(animal):
    animal.make_sound()

animals = [Animal(), Dog(), Lion(), Dog(), Lion(), Animal(), Cat()]
for animal in animals:
    animal_make_sound(animal)


# Interface segregation principle
from abc import ABC, abstractmethod

# Interface for workers who can work with documents
class DocumentWorker(ABC):
    @abstractmethod
    def work_with_documents(self):
        pass

# Interface for workers who can handle emails
class EmailWorker(ABC):
    @abstractmethod
    def work_with_emails(self):
        pass

# Interface for workers who can manage schedules
class ScheduleWorker(ABC):
    @abstractmethod
    def manage_schedule(self):
        pass

# Manager class implementing all three interfaces
class Manager(DocumentWorker, EmailWorker, ScheduleWorker):
    def work_with_documents(self):
        print("Manager is working with documents.")

    def work_with_emails(self):
        print("Manager is working with emails.")

    def manage_schedule(self):
        print("Manager is managing schedule.")

# Clerk class implementing only DocumentWorker and EmailWorker
class Clerk(DocumentWorker, EmailWorker):
    def work_with_documents(self):
        print("Clerk is working with documents.")

    def work_with_emails(self):
        print("Clerk is working with emails.")

# Assistant class implementing only EmailWorker and ScheduleWorker
class Assistant(EmailWorker, ScheduleWorker):
    def work_with_emails(self):
        print("Assistant is working with emails.")

    def manage_schedule(self):
        print("Assistant is managing schedule.")

# Client class utilizing different workers
class Client:
    def __init__(self, worker):
        self.worker = worker

    def perform_tasks(self):
        if isinstance(self.worker, DocumentWorker):
            self.worker.work_with_documents()
        if isinstance(self.worker, EmailWorker):
            self.worker.work_with_emails()
        if isinstance(self.worker, ScheduleWorker):
            self.worker.manage_schedule()

# Usage
manager = Manager()
clerk = Clerk()
assistant = Assistant()

client1 = Client(manager)
client1.perform_tasks()
print("-"*80)
client2 = Client(clerk)
client2.perform_tasks()
print("-"*80)
client3 = Client(assistant)
client3.perform_tasks()





