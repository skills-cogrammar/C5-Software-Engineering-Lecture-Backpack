my_str = "Let's learn some more about strings!"

# # Change a string to all uppercase
# print(my_str.upper())

# # Count occurences of substring
# count = my_str.count("s")
# print("Number of 's' characters: {}".format(count))

# # Find first index where substring is found
# print(f"Index of character 'a' is {my_str.find('a')}")

# # Check if all charaters in string is alphabetic
# print(my_str.isalpha()) # --> False

# Check if all charaters in string is numeric
# print("123".isnumeric())

# # Join strings in list together
string_list = ["Welcome", "to", "the", "lecture!"]
# joined = " ".join(string_list)

# # Use .strip() to remove all leading or trailing whitespace
# print(joined.strip())

my_str = "Let's learn some more about strings!"
# print(my_str)
# "".lstrip()
# "".rstrip()
# Replace a given substring within a string
# my_str = my_str.replace(" ", "-")

# # # Split string into a list
# print(my_str.split("-"))

# # Getting the length of a string
# print(len(my_str))

# Function len()
# Method .upper()

# min and max functions on strings
# az = "aRb"
# print(max(az))
# print(min(az))

# Looping over a string with for-loop
# for letter in my_str:
#     print(letter)


# # Comparing strings
# word = "chicken"
# if word == "chicken":
#     print(f"We will be eating {word} tonight!")

# # Checking for substrings
# if "learn" in my_str:
#     print(f"Substring 'learn' exists in '{my_str}'")




# Index to a character in a string
# print(my_str[1])
# print(my_str[6] + my_str[7] + my_str[8] + my_str[9] + my_str[10])

# string_list = ["Welcome", "to", "the", "lecture!"]
# string_list[-1] = "show!"

# print(string_list)
# Strings  are immutable
# my_str[25] = "?"


# Slicing a string

# print(my_str[0:7])
# print(my_str[17:24])

# Slice from beginning
print(my_str[:11])

# Slice up to the end
print(my_str[17:])

# Negative slicing
print(my_str[-19:-14])
print(my_str[-8:-1])

#                       [start, end, step]
# Using the step parameter when slicing
my_str = "Let's slice some strings!"
print(my_str[0:16:2])
print(my_str[-2:-9:-1])
