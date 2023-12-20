"""
Let's Generate a minesweeper grid!
"""

def initialize_grid(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

# numbers = ["Liano" for _ in range(5)]
# print(numbers)

def display_board(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))

# Example usage
rows = 3
cols = 3

minesweeper_grid = initialize_grid(rows, cols)
display_board(minesweeper_grid)



"""
MineSweeper Code Along Challenge :)
"""


# Given a Minesweeper-like grid represented by a list of lists. 
# The grid contains two types of cells: "-" for free spots and "#" for mines. 
# Your task is to create a function that takes this grid as input 
# and returns a copy of the grid where each "-" is replaced with a 
# number representing the count of mines in the surrounding cells 
# (including diagonals).



# output_grid = minesweeper(input_grid)

# The resulting output_grid should be:
# [
#     [2, "#", 3, "#", "#"],
#     ["#", 5, 5, "#", "#"],
#     [3, "#", "#", 5, 3],
#     [2, 3, 3, 4, "#"],
#     ["#", "#", 3, 2, 2]
# ]



"""

iterate through each cell in grid *

Identify cells occupied mines *
    add this mine to the new grid(same index) *

Identify Mine-free cells(elements) *
    identify if surrounding cells are occupied by mines & * 
        count those occupied by mines *

add this count to the relevant position in the new grid

"""
input_grid = [
    ["-", "#", "-", "#", "#"], # [0][0] 
    ["#", "-", "-", "#", "#"], # [x+1][2]
    ["-", "#", "-", "-", "-"],
    ["-", "-", "-", "-", "#"],
    ["#", "#", "-", "-", "-"]
]

rows = len(input_grid)
cols = len(input_grid[0])

output_grid = [['' for _ in range(cols)] for _ in range(rows)]
# print(output_grid)

for i in range(rows):  
    for j in range(cols):
        # If current cell = "#" send to output grid.
        if input_grid[i][j] == '#':
            output_grid[i][j] = '#'
        else:
            # Count mines surrounfing this spot (incl diagonals)
            mine_counter = 0
            for x in range(max(0, i - 1), min(rows, i+2)):
                for y in range(max(0, j -1), min(cols, j+2)):
                    if input_grid[x][y] == '#':
                        mine_counter += 1

            # send to output grid.       
            output_grid[i][j] = mine_counter

# print(output_grid)

# for i in range(len(output_grid)):
#     print(output_grid[i])
        

for i in range(1, 9+2):
    print(i)