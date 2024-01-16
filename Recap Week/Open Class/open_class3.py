"""

What does invalid literal for int with base 10 mean 
when user chooses something other than 1, 2 , 3 , 4. 
How do I defend against this?

"""

user_input = input("Enter value:")

# if numeric:
#    cast/convert to int/float
# else:
#     print error
#     prompt again

# update = int(user_input)
# print(update)



"""
Second question[2, 4,5] i want to join these but 
getting error expected str instance, int found.
I used "\n".join(item_quantity)'
"""

item_quantity = [2, 4, 5]
# Iterate over item_quan:
#   for every item:
#       add a str intance of this item to new list

joined = "\n".join(item_quantity)

print(joined)