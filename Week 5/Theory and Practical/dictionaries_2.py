my_dict = {1 : 'One',
           2 : 'Two',
           3 : 'Three'}

my_dict_2 = {"Michelle" : "Parker",
             "Steven" : "Donald",
             "Cindy" : "Marsh"}

my_dict_3 = {1 : "Hello",
             True : False,
             "dict" : {"name" : "Peter",
                       'age' : 20,
                       'scores' : [50, 75, 66, 67, 71]},
             40.5 : "Float"}

print(my_dict_3['dict']['scores'].append())


# # Create dictionaries using dict()

new_dict = dict(name="Percy", surname="Jackson", age=14)

# print(new_dict)
# print(new_dict['name'])









# # Accessing values


# print(test_dict['name'])
# print(test_dict['age'])
# print(test_dict['scores'])


# print(test_dict.get('name'))
# print(test_dict.get('age'))
# print(test_dict.get('scores'))








# values = test_dict.values()
# print(values)
# for value in test_dict.values():
#     print(value)




# keys = test_dict.keys()
# print(keys)

# for key in test_dict.keys():
#     print(key)



name = "name"


# items = test_dict.items()
# print(items)

# for key, value in test_dict.items():
#     print(key, value, sep=" - ")











# # Updating dictionary
# test_dict['name'] = "Susan"
# test_dict["age"] = 35
# print(test_dict)

# test_dict.update({'age' : 30})
# print(test_dict)

# print(test_dict['surname'])

# test_dict['surname'] = 'Clarke'
# print(test_dict)

# user_height = 162

# test_dict.update(height=user_height)
# print(test_dict)













# # Removing Items
# removed_value = test_dict.pop('age')
# print(test_dict)
# print(f"Value that was removed - {removed_value}")

# test_dict.popitem()
# print(test_dict)

# test_dict.clear()
# print(test_dict)















# # Remember to use copy to create new dictionaries
# copy_dict = dict(test_dict)
# copy_dict['name'] = "Mark"
# print(test_dict)
# print(copy_dict)








test_dict = {'name' : "Peter",
             'age' : 20,
             'scores' : [50, 75, 66, 67, 71]}







# # Dictionary comprehension
# new_dict = {i:"" for i in range(5)}

# print(new_dict)


# names = ["John", "Margaret", "Sarah"]
# surnames = ["Smith", "Jones", "Williams", "James"]

# if len(names) == len(surnames):
#     users = {names[i]:surnames[i] for i in range(len(names))}

# # users = {}

# if len(names) == len(surnames):
#     for i in range(len(names)):
#         users.update({names[i]:surnames[i]})
# print(users)

# names_dict = {}
# for i in range(1, 3):
#     user_name = input("Please enter a name: ")
#     user_surname = input("Please enter a surname: ")
#     names_dict[user_name] = user_surname

# print(names_dict)
