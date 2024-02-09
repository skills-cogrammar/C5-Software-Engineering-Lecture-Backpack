# dict_list = [{} for _ in range(10)]
# dict_list[0]["name"] = "Armand"
# print(dict_list)


# def add_nums(num1, num2):
#     return num1 + num2

# def subtract_nums(num1, num2):
#     return num1 - num2

# add_nums(2, 5)

# new_add_nums = add_nums
# print(new_add_nums(3, 5))

# def calculate(num1, num2, operation):
#     return operation(num1, num2)

# print(calculate(3, 6, add_nums))
# print(calculate(10, 6, subtract_nums))

# # -- Example 2
# def my_decorator(func):     # func is paramater that receives the function name
#     def wrapper():          # wrapper can be any name
#         print("It is time to celebrate.")
#         func()
#         print("Here comes the sparkles.")
#     return wrapper

# @my_decorator       # Same as say_hello_with_sparkles = my_decorator(say_hello)
# def say_hello():
#     print("Hello!")

# @my_decorator       # Same as say_cheers_while_smiling = my_decorator(say_cheers)
# def say_cheers():
#     print("Cheers!")

# # Using the decorated function
# say_hello()
# """
# You can also remove @my_decorator above function and the say_hello() and
# replace with below by placing it after the function
# """
# say_hello_with_sparkles = my_decorator(say_hello)
# say_hello_with_sparkles()
# print()

square = lambda x : x**2

numbers = [1,2,3,4,5]
squared = list(map(lambda x : x*2, numbers))
# squared = [_ for _ in map(square, numbers)]
# print(squared)


"""Function Decorators"""
def positives_only(func):
    def wrapper(values):
        values = [i for i in values if i >= 0]
        return func(values)
    return wrapper

@positives_only
def average(numbers):
    return sum(numbers)/len(numbers)

# print(average([-1,-5,-2,-6,1,5,3,2]))


dict_list = [{"name": "", "surname" : ""} for _ in range(10)]
dict_list.append({})
for dict in dict_list:
    if "name" in dict:
        dict["name"] = "Armand"
        dict.update(name="Armand")
print(dict_list)

# for i, dict in enumerate(dict_list):
#     print(i, dict["name"], dict["surname"])

my_dict = {"name": "James", "surname" : "Parker"}

for i, (key, value) in enumerate(my_dict.items()):
    print(i ,key, value)