# Creating strings
single = 'Hello World!'
double = "This is a string!"
triple = """This is a 
multi-line string!"""
# print(triple)



# Indexing
# print(test_str[0])
# print(test_str[2])
# print(test_str[-1])
# print(test_str[-4])


# Slicing strings
# print(test_str[::2])
# print(test_str)
# print(test_str[:5])
# hello = test_str[:5]
# print(hello)
# print(test_str[4:])

# Negative slicing
# print(test_str[-3:-1])
# print(test_str[-6:])
# print(test_str[:-2])


# Strings are immutable
# test_str[3] = "*"


# test_str = test_str.replace("l", "*")
# print(test_str)


# Some useful string methods

# print(test_str)
# print(test_str.capitalize())
# print(test_str.upper())
# print(test_str.replace("ll", "********"))
# print(test_str.strip("*"))
# print(test_str.split(","))

# print(" ".join(["This", "is", "how", "you", "join!"]))

test_str = "hello, world!"
# Get character index
# print(test_str.find("o"))
# print(test_str.index("e"))


# String checks

# print(test_str.isnumeric())
# print(test_str.isalpha())
# print(test_str.islower())


# Comparison Operators
# print("hello" == "hello")
# print("hello" != "Hello")
# print("q" < "b") # ASCII
# print('l' > 'g') # ASCII


test_str = "hello world!"
# Looping over strings
for i in range(1, len(test_str)):
    print(test_str[i])

# for letter in test_str:
#     print(letter)




range()
len()
enumerate()
