# Dealing with keyboard interrupts

try: 
    while True:
        # Your main program code
        pass

except KeyboardInterrupt as interrupt_msg:
     print("Keyboard Interrupt was caught. Ignoring...")

# ===============================

# =================== Syntax Errors
     
if True print("This is true!")
"""
if True:
    print("This is a true statement")
"""

# -----------------
while True:
print("Endless print")
"""
while True:
    print("Endless loop")
"""

# -----------------
my_dict = {1: "one"
           2: "two"
           3: "three"}
"""
my_dict = {1: "one",
           2: "two",
           3: "three"}
"""
# -----------------

# =================== Runtime Errors
add_num = "5" + 1
# TypeError: can only concatenate str (not "int") to str

# -----------------
add_num =  1 + "5"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# -----------------
split_str = "Hello World".split_string(" ")
# AttributeError: 'str' object has no attribute 'split_string'
"""
split_str = "Hello World".split(" ")
print(split_str)
"""
# -----------------
file = open("Randomfile.txt", "r")
# FileNotFoundError: [Errno 2] No such file or directory: 'Randomfile.txt'

# =================== Logical Errors
sum_squares = 0

for num in range(10):   # [0,1,2,3,4,5,6,7,8,9] [0,1,4,9,16,25,36,49,64,81]
    squared_num = num**2

# Indentattion error
sum_squares += squared_num

print(sum_squares) 

# Outcome: 81 but should be 285

# -----------------
num = 5

# The for loop declares and controls the variable num
for num in [0,1,2,3,4,5,6,7,8,9]:   #range(10)
    num += num

print(num)  
# Result is 18 since the last num += num was not overwritten
# by the new loop iteration.
