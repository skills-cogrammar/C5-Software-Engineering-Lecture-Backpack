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


# Create dictionaries using dict()

new_dict = dict(name="Percy", surname="Jackson", age=14)

print(new_dict)


# Accessing values

test_dict = {"name" : "Peter",
             'age' : 20,
             'scores' : [50, 75, 66, 67, 71]}

print(test_dict['name'])
print(test_dict['age'])
print(test_dict['scores'])


print(test_dict.get('name'))
print(test_dict.get('age'))
print(test_dict.get('scores'))


for value in test_dict.values():
    print(value)


for key in test_dict.keys():
    print(key)


for key, value in test_dict.items():
    print(key, value, sep=" - ")


# Updating dictionary
test_dict['name'] = "Susan"
test_dict["age"] = 35

test_dict.update({'age' : 30})
print(test_dict)


test_dict['surname'] = 'Clarke'

test_dict.update(height=162)
print(test_dict)


# Removing Items
test_dict.pop('surname')
print(test_dict)

test_dict.popitem()
print(test_dict)

test_dict.clear()
print(test_dict)




# Remember to use copy to create new dictionaries
copy_dict = test_dict
copy_dict['name'] = "Mark"
print(test_dict)



# Dictionary comprehension
new_dict = {i:"" for i in range(5)}

print(new_dict)


names = ["John", "Margaret", "Sarah"]
surnames = ["Smith", "Jones", "Williams"]

users = {names[i]:surnames[i] for i in range(len(names))}
print(users)