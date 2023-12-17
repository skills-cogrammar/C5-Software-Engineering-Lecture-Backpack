# Block comment: 
# i' can be thought of as the iterator (inline).
# Simple for loop that prints values from 0-10 


# # This is a block comment (I refer to the code following me :) )
# print("Read my block comment ^")

# Multi-Line comment
"""
Simple for loop that prints values from 0-10.
i' can be thought of as the iterator (inline).
"""

# # Inline comment:
# for i in range(10):
#     print(i)# 'i' can be thought of as the iterator (inline).
#     if i > 5:
#         print("The quick brown fox jumps over the lazy dog.", "The quick brown fox jumps over the lazy dog.", sep="\n")

# print("The quick brown fox jumps over the lazy dog.", 
#       "The quick brown fox jumps over the lazy dog.", 
#       sep="\n")




# print("A", "B", "C", sep="-")


# print(
# "A",
# "B",
# sep="\n")

# Enumerate Example
stock = ["tea", "milk", "sugar"]
# print(stock[0])

enumerated_stock = enumerate(stock)
visible_stock = list(enumerated_stock)

[(0, 'tea'), (1, 'milk'), (2, 'sugar')]


print(list(enumerate(stock)))

