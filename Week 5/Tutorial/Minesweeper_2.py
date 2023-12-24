"""
Let's Generate a minesweeper grid!
"""

def initialize_grid(rows, cols):
    return [["-" for _ in range(cols)] for _ in range(rows)]

def display_board(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * (4 * len(row) -1))

# display_board(initialize_grid(5,5))

# rows = 5
# cols = 3

# our_grid = initialize_grid(rows, cols)
# for row in our_grid:
#     print(row)



# new_grid = [[" " for _ in range(cols)] for _ in range(rows)]

# print(new_grid)















"""
MineSweeper Code Along Challenge :)
"""


# Given a Minesweeper-like grid represented by a list of lists. 
# The grid contains two types of cells: "-" for free spots and "#" for mines. 
# Your task is to create a program that takes this grid as input 
# and returns a copy of the grid where each "-" is replaced with a 
# number representing the count of mines in the surrounding cells 
# (including diagonals).

# input_grid = [
#     ["-", "#", "-", "#", "#"],
#     ["#", "-", "-", "#", "#"],
#     ["-", "#", "-", "-", "-"],
#     ["-", "-", "-", "-", "#"],
#     ["#", "#", "-", "-", "-"]
# ]

# output_grid = minesweeper(input_grid)

# The resulting output_grid should be:
# [
#     [2, "#", 3, "#", "#"],
#     ["#", 3, 3, "#", "#"],
#     [3, "#", "#", 3, 3],
#     [2, 3, 3, 4, "#"],
#     ["#", "#", 3, 2, 2]
# ]

input_grid = [
    ["-", "#", "-", "#", "#"],
    ["#", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "-", "-", "#"],
    ["#", "#", "-", "-", "-"]
]

"""
(-1,-1)  (-1, 0) (-1, +1)
(0, -1)   (i,j)  (0, +1) 
(+1, -1) (+1, 0) (+1, +1)
"""


rows = len(input_grid)
cols = len(input_grid[0][0])

output_grid = [["" for _ in range(cols)] for _ in range(rows)]


for i in range(rows):
    for j in range(cols):
        if input_grid[i][j] == "#":
            output_grid[i][j] = "#"
        else:
            mine_counter = 0
            if i > 0:
                if j > 0 and input_grid[i-1][j-1] == "#":
                    mine_counter += 1
                if input_grid[i-1][j] == "#":
                    mine_counter += 1
                if j < cols-1 and input_grid[i-1][j+1] == "#":
                    mine_counter += 1
            if j > 0 and input_grid[i][j-1] == "#":
                mine_counter += 1
            if j < cols -1 and input_grid[i][j+1] == "#":
                mine_counter += 1
            if i < rows-1:    
                if j > 0 and input_grid[i+1][j-1] == "#":
                    mine_counter += 1
                if input_grid[i+1][j] == "#":
                    mine_counter += 1
                if j < cols-1 and input_grid[i+1][j+1] == "#":
                    mine_counter += 1 
            output_grid[i][j] = mine_counter  


for row in output_grid:
    print(row)