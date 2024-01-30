# from functions import print_name

# print_name("James")

def print_line(length=80, symbol="-"):
    print(symbol*length)

print_line(length=20, symbol="~")


def random_calculation(num1, num2, num3):
    try:
        result = (num1 ** num2) + num3
        return result
    except:
        return None

# try:
#     random_calculation("3", "4", "5")
# except:
#     print("Invalid values")

# print(random_calculation(10,3,6))

# def print_lines():
#     for i in range(10):
#         print_line(30, "@")


# print(print_line())

# if 10 > 5:
#     print()


def add_values(values):
    if len(values) == 1:
        return values[0]
    else:
        return values[0] + add_values(values[1:])
    
print(add_values([1,2,3,4,5]))
