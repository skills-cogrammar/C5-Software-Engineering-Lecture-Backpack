
# animals.append("Parrot")
# animals.insert(1, "Parrot")



# animals = ["Dog", "Cat", "Gecko", "Goldfish", "Ball Python"]

# new_animals = animals.copy()
# new_animals.append("Chameleon")
# print(new_animals)
# print(animals)






# squares = []
# for x in range(10):
#     squares.append(x**2)

# squares = [x**2 for x in range(10)]
# print(squares)


even_nums = []
# print(list(range(50)))
# for i in range(50):
#     if i%2 == 0:
#         even_nums.append(i)

# even_nums = [i for i in range(50) if i%2 == 0]
# print(even_nums)

# print(list(zip(names, surnames, "abcdefg", [1,2,3,4,5])))


names = ["David", "Peter", "Michelle", "Kayla", "Anita"]
surnames = ["Jackson", "Graham", "Cook", "Carty"]

new_list = []
for name, surname in zip(names, surnames):
    new_list.append((name, surname))
print(new_list)

names_surnames = [(name, surname) for name, surname in zip(names, surnames)]
# print(names_surnames)

# name, surname, age = ("David", "Jackson", 25)
# print(name, surname, age)

# my_print = print
# my_print("Hello world!")