my_str = "Let's learn about strings!"

# Change a string to all uppercase
print(my_str.upper())

# Count occurences of substring
count = my_str.count("s")
print("Number of 's' characters: {}".format(count))

# Find first index where substring is found
print(f"Index of character 'a' is {my_str.find('a')}")

# Check if all charaters in string is alphabetic
print(my_str.isalpha())

# Check if all charaters in string is numeric
print("123".isnumeric())

# Join strings in list together
print(" ".join(["Welcome", "to", "the", "lecture!"]))

# Replace a given substring within a string
print(my_str.replace("s", "#"))

# Split string into a list
print(my_str.split())

# Getting the length of a string
print(len(my_str))


# min and max functions on strings
print(max(my_str))
print(min(my_str))




# Looping over a string with for-loop
for letter in my_str:
    print(letter)


# Comparing strings
word = "chicken"
if word == "chicken":
    print(f"We will be eating {word} tonight!")


# Checking for substrings
if "learn" in my_str:
    print(f"Substring 'learn' exists in '{my_str}'")




my_str = "Let's slice some strings!"

# Index to a character in a string
print(my_str[1])
print(my_str[6] + my_str[7] + my_str[8] + my_str[9] + my_str[10])


# Strings  are immutable
my_str[25] = "?"


# Slicing a string
print(my_str[6:11])
print(my_str[17:24])

# Slice from beginning
print(my_str[:11])

# Slice up to the end
print(my_str[17:])

# Negative slicing
print(my_str[-19:-14])
print(my_str[-8:-1])


# Using the step parameter when slicing
print(my_str[0:16:2])
print(my_str[-2:-9:-1])
