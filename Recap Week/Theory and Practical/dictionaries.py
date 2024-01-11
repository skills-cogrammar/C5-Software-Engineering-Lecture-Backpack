my_dict = {1 : 'One',
           2 : 'Two',
           3 : 'Three'}


my_dict_2 = {"Michelle" : "Parker",
             "Steven" : "Donald",
             "Cindy" : "Jackson"}

my_dict_3 = {1 : "Hello",
             True : False,
             "dict" : {"name" : "Peter",
                       'age' : 20,
                       'scores' : [50, 75, 66, 67, 71]},
             40.5 : "Float"}



# Create dictionaries using dict()

# new_dict = dict(name="Jack", surname="Reacher", age=14)
# print(new_dict)





# Accessing values


# print(test_dict['name'])
# print(test_dict['age'])
# print(test_dict['scores'])


# print(test_dict.get('name', "Nothing"))
# print(test_dict.get('ages', 0))
# print(test_dict.get('scores', []))





# Updating dictionary
# test_dict['name'] = "Susan"
# test_dict["age"] = 35
# print(test_dict)


# test_dict.update(age="30")
# print(test_dict)


# test_dict['surname'] = 'Clarke'

# test_dict.update(height=162)
# print(test_dict)





# Removing Items
# value = test_dict.pop('name')
# print(value)
# print(test_dict)

# test_dict.popitem()
# print(test_dict)

# test_dict.clear()
# print(test_dict)





# print(test_dict.values())
# for value in test_dict.values():
#     print(value)

# print(test_dict.keys())
# for key in test_dict.keys():
#     print(key)

# print(test_dict.items())
# for key, value in test_dict.items():
#     print(key, value, sep=" - ")




             
from copy import deepcopy
# Remember to use copy to create new dictionaries
test_dict = {"name" : "Peter",
             'age' : 20,
             'scores' : [50, 75, 66, 67, 71]}

copy_dict = deepcopy(test_dict)
copy_dict['scores'][1] = 200
print(copy_dict)
print(test_dict)





# Dictionary comprehension
# new_dict = {i:"" for i in range(5)}

# print(new_dict)


# names = ["John", "Margaret", "Sarah"]
# surnames = ["Smith", "Jones", "Williams"]

# users = {name:surname for name, surname in zip(names, surnames)}
# print(users)