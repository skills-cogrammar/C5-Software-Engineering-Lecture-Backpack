"""
my_list = [[1,2,3],[4,5,6],[7,8,9]]

for row in my_list:     #[[1,2,3],[4,5,6],[7,8,9]]
    print_line = f"jfdlkjsdlkj {row}"
    print(row)
    for col in row:     # [4,5,6]
        print(col)
"""
"""
# Example input
    [1,2,3]
    [12,23,34]
    [10,20,30]

# Example output: [23,45,67]
"""
# ====== Define function
def column_sums(grid):
    num_rows = len(grid)
    num_cols = len(grid[0]) if grid else 0

    sums = [0] * num_cols # [0,0,0]

    for row in grid:
        for col in range(num_cols):
            sums[col] += row[col]

    return sums

# Main Code
num_rows = int(input("Enter the number of rows: "))   
num_col = int(input("Enter the number of columns: "))   
# num_deep = int(input("Enter the number of deep: ")) 

# Use list comprehension to create the grid
user_grid = [[0 for col in range(num_col)] for row in range(num_rows)]

# Example of how to get to above
# list = [<Do this> for row in range(num_rows) <condition>]
# one_dim_list = [0 for row in range(num_rows)]
# two_dim_list = [[0 for col in range(num_rows)] for row in range(num_rows)]
# three_dim_list = [[[0 for deep in range(num_rows)] for col in range(num_rows)] for row in range(num_rows)]

print(f"==> Grid prep before values:")
for row in user_grid:
    print(row)

print(f"==> Provide values for the grid:")
for row in range(len(user_grid)):
    print(f"row number: {row + 1}")
    for col in range(len(user_grid[row])):
        print(f"col number: {col + 1}")
        user_grid[row][col] = int(input("Enter a value: "))

print(f"==> Grid prep after values:")
for row in user_grid:
    print(row)

column_sums_result = column_sums(user_grid)
print("Column sums:", column_sums_result)
