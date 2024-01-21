import os
# Common Character sets

"""
ASCII - American Standard Code for Information Interchange
Unicode - Universal Character encoding
UTF-8 - Unicode Transformation Format 8-bit
"""

"""
1. ASCII
- 128 characters that include english letters, numerals and symbols
- basic and common for english language but not for non-english characters
"""

"""
2. Unicode
- universal character encoding standard that represents most if not all characters
from known languages and scripts
"""

"""
3. UTF-8 
- Variable width character encoding that represents using 8-bit code units
- widely used and efficiently handles english and non-english characters
- (～￣▽￣)～  🐱‍👤👻
"""

# Why Encoding
"""
1. Multilingual Suport
2. Avoiding data corruption
3. Handling special characters - 🦾🎉
"""

"""
russian alphabet
(⟨б⟩, ⟨в⟩, ⟨г⟩, ⟨д⟩, ⟨ж⟩, ⟨з⟩, ⟨к⟩, ⟨л⟩, ⟨м⟩, ⟨н⟩, ⟨п⟩, ⟨р⟩, ⟨с⟩, ⟨т⟩, ⟨ф⟩, ⟨х⟩, ⟨ц⟩, ⟨ч⟩, ⟨ш⟩, ⟨щ⟩)

english alphabet
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.

serge's new language
🐱‍👤👻 - hello
🖐🎉 - pluto is a planet

Kanji
fill-in here (note)
"""


# Best Practices for file handling 
"""
1. Use with() context manager
2. Specify encoding - when working with files.
3. Handle Exceptions (try/catch)
4. Avoid hardcoding file paths (os library)
5. Use correct file access modes - r, w, a
"""

# 1. Use with() context manager
with open('random_names.txt', 'r+') as file:
    print(file.read())

# 2. Specify encoding - when working with files.
with open('random_names.txt', 'r+', encoding='utf-8') as file:
    print(file.read())

# 3. Handle Exceptions (try/catch)
try:
    with open('random_names.txt', 'r+', encoding='utf-8') as file:
        print(file.read())
except IOError as e:
    print(f"Error from file: {e}")

# 4. Avoid hardcoding file paths (os library)

# Approach 1 - use of variable
current_file_path = "list_of_cats.txt"

with open(current_file_path, 'r+') as file:
    print(file.read())

# Approach 2 - OS Library
    
current_dir = "/home/user"
current_file_path = os.path.join("your current directory", "random_names.txt")

with open(current_file_path, 'r+') as file:
    print(file.read())  

# Bonus 
current_file_path = "random_names.txt"
if os.path.exists(current_file_path):
    print("True the file does exist!")
    # with open(current_file_path, 'r+') as file:
    #     print(file.read())  
else:
    print("It does not exist")