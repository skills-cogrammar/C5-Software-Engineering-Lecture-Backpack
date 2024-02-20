"""
How to deal with dates
"""
from datetime import datetime
# Testing for a valid date
def is_valid_date(date_str):
    try: 
        # Parse the date string using the specified format
        # If the format is valid then datetime will work else a ValueError 
        # will be raised.
        date_format = datetime.strptime(date_str, '%d %b %Y')
        print("--- Is Valid Date ---")
        print(f"date_str: >{date_str}< - date_format: >{date_format}< ")
        return True
    except ValueError:
        return False
    
# Example Usage
date_to_check = "29 Feb 2024"
if is_valid_date(date_to_check):
    print(f">{date_to_check}< is a valid date")
else:
    print(f">{date_to_check}< is NOT a valid date")

# =====================
# Build today's date from datetime.now
current_date = datetime.now().strftime('%d %b %Y') # (%d-%m-%Y) -> 29-02-2024

# Example Usage
input_date = "20 Feb 2024"
if input_date == current_date:
    print(f"-- Dates are the same --")
else:
    print(f"-- Dates are not the same --")

print(f"input_date: >{input_date}< - current_date: >{current_date}< \n")

# =====================
# Using individual date portions
display_date = str(datetime.now().day) + " " + datetime.now().strftime("%b") + \
                " " + str(datetime.now().year)

input_date = "20 Feb 2024"
if input_date == display_date:
    print(f"-- Dates are the same --")
else:
    print(f"-- Dates are not the same --")

print(f"input_date: >{input_date}< - display_date: >{display_date}< \n")

# =============================================
# Get today's date
from datetime import date

today_date = date.today()

input_date = "20 Feb 2024"
if input_date == today_date:
    print("-- Dates are the same --")
else:
    print("-- Dates are not equal --")

# The import date does not provide the format we are looking for.
print(f"input_date: >{input_date}< - display_date: >{today_date}<")
