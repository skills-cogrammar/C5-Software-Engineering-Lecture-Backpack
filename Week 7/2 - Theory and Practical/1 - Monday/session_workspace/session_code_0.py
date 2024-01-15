# hello everyone
# absolute path - C:\Users\smugh\Desktop\HypeDev Lecture Backpack\Week 7\session_workspace\session_code.py
# relative path - "session_code"

# Open() - load in file as an object
# Access Modes - 'r' ; 'w' ; 'a' ; '+'

# traditional method
"""
file_object = open("randomOtherFolder\cats.txt", "r")
# process file logic
file_object.close()
"""

# context manager
"""
with open("cats.txt", "r") as file_object:
  #  process your logic
"""
