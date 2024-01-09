# class Lion:

#     def __init__(self):
#         self.sound = "Roar!"

#     def make_sound(self):
#         print(self.sound)






# class Lion:

#     def __init__(self, name):
#         self.name = name
#         self.sound = "Roar!"

#     def make_sound(self):
#         print(self.name, "goes", self.sound)

# names = ["Sunny", "Dave", "Spot", "Jack"]
# lions = []
# for name in names:
#     lion = Lion(name)
#     lions.append(lion)

# for lion in lions:
#     lion.make_sound()






class Animal():

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Make animal sound.")


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.sound = "meow"

    def make_sound(self):
        print("The cute little kitty goes", self.sound)


class Lion(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.sound = "roar"

    def make_sound(self):
        print("The ferocious lion goes", self.sound)


cat = Cat("Astro")
lion = Lion("Sunny")
animals = [cat, lion]

for animal in animals:
    if isinstance(animal, Animal):
        print(animal.name)