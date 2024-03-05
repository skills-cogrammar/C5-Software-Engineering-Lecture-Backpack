"""
Create a function that takes a grid of # and -, 
where each hash (#) represents a # mine and each dash (-) represents a mine-free spot.

Return a grid, where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally).

Example of an input:
[ 
['-', '-', '-', '#', '#'],
['-', '#', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '#', '#', '-', '-'],
['-', '-', '-', '-', '-'] ]

Example of the expected output:
[ 
['1', '1', '2', '#', '#'],
['1', '#', '3', '3', '2'],
['2', '4', '#', '2', '0'],
['1', '#', '#', '2', '0'],
['1', '2', '2', '1', '0'] ]

""" 

# HINTS: 
# - When checking adjacent positions to a specific position in the grid,
#   the following grid might assist you in determining adjacent indexes:
#           -------------------------------------------------
#   R - 1   |       NW      |       N       |       NE      |
#           -------------------------------------------------
#     R     |       W       |       *       |       E       |
#           -------------------------------------------------
#   R + 1   |       SW      |       S       |       SE      |
#           -------------------------------------------------
#                 C - 1             C             C + 1
#
# - Also ensure that when checking adjacent positions in the grid that you take 
#   into account that on the edges of the grid, you may go out of bounds.
# - Lastly, you could make use of the enumerate function in Python to keep track 
#   of the index points and values without having to create a count variable and
#   explicitly iterate the count variable to keep track of the current row or 
#   column index.

# =============== IMPORT LIBRARIES =================

import copy
import random

# =============== DECLARE FUNCTIONS ================

# Use the hardcode grid initially and then switch to the grid generation
def generate_random_mine_grid(rows, cols, mine_probability):
    """
    Generate a random mine grid.

    Parameters:
    - rows: Number of rows in the grid.
    - cols: Number of columns in the grid.
    - mine_probability: Probability of a cell containing a mine (0.0 to 1.0).

    Returns:
    - A randomly generated mine grid as a nested list.
    """

    mine_grid_nlist = [['-' for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if random.random() < mine_probability:
                mine_grid_nlist[row][col] = '#'

    return mine_grid_nlist


def mine_count_func(mine_grid_nlist):
    """
    Calculate the number of mines for each '-' position in the grid

    Parameters:
    - mine_grid_nlist: The mine grid as a nested list

    Returns:
    - A new grid with mine counts as a nest list
    """

    # count_grid_nlist = mine_grid_nlist.copy()
    count_grid_nlist = copy.deepcopy(mine_grid_nlist)

    for row, row_values in enumerate(count_grid_nlist):
        for col, item in enumerate(row_values):       
        # Above was improved from:
        # for col, item in enumerate(count_grid_nlist[row]):

            mine_count_int = 0

            if item == '-': # Improved from: if count_grid_nlist[row][col] == '-':
            # If current position value is '-' then count mines
            # All if statements below also test for out-of-range mine searching. 
            # For-loops above will make sure that the current row and col 
            # will not be out of index range.
            # When we test position (row - 1) or (col - 1) for a mine, 
            # we stay in range by making sure that these positions are >= 0.
            # When we test position (row + 1) or (col + 1) for a mine, 
            # we stay in range by making sure that these positions 
            # are < number of rows and < number of columns in our grid.
                
                # ==> NW position: [row - 1][col - 1]
                if (row - 1) >= 0 and (col - 1) >= 0 and \
                    count_grid_nlist[row - 1][col - 1] == '#' :

                    mine_count_int += 1

                # ==> N position: [row - 1][col]
                if (row - 1) >= 0 and count_grid_nlist[row - 1][col] == '#':
                    mine_count_int += 1

                # ==> NE position: [row - 1][col + 1]
                # len(count_grid_nlist[row]) or len(row_values) counts 
                # number of columns and is 1 more than the maximum index.
                if (row - 1) >= 0 and (col + 1) < len(row_values) and \
                    count_grid_nlist[row - 1][col + 1] == '#':

                    mine_count_int += 1

                # ==> W position: [row][col - 1]
                if (col - 1) >= 0 and count_grid_nlist[row][col - 1] == '#':
                    mine_count_int += 1

                # ==> E position: [row][col + 1]
                if (col + 1) < len(row_values) and \
                    count_grid_nlist[row][col + 1] == '#':

                    mine_count_int += 1

                # ==> SW position: [row + 1][col - 1]
                # len(count_grid_nlist) counts number of rows and is 1 more than 
                # the maximum index.
                if (row + 1) < len(count_grid_nlist) and (col - 1) >= 0 and \
                    count_grid_nlist[row + 1][col - 1] == '#':

                    mine_count_int += 1

                # ==> S position: [row + 1][col]
                if (row + 1) < len(count_grid_nlist) and \
                    count_grid_nlist[row + 1][col] == '#':

                    mine_count_int += 1

                # ==> SE position: [row + 1][col + 1]
                if (row + 1) < len(count_grid_nlist) \
                    and (col + 1) < len(row_values) \
                        and count_grid_nlist[row + 1][col + 1] == '#':
                    
                    mine_count_int += 1             
                
                """
                The below code removes the max_row and max_col test and allow
                the code to produce an Index-out-of-range error and then just 
                ignore that surrounding position when this happens since an 
                out-of-range position cannot contain a mine.

                # NW position: [row - 1][col - 1]
                try:
                    if (row - 1) >= 0 and (col - 1) >= 0 and \
                    count_grid_nlist[row - 1][col - 1] == '#' :
                        mine_count_int += 1
                except IndexError:
                    pass

                # N position: [row - 1][col]
                try:
                    if (row - 1) >= 0 and count_grid_nlist[row - 1][col] == '#':
                        mine_count_int += 1
                except IndexError:
                    pass

                # NE position: [row - 1][col + 1]
                try:
                    if (row - 1) >= 0 and count_grid_nlist[row - 1][col + 1] == '#':
                        mine_count_int += 1
                except IndexError:
                    pass

                # W position: [row][col - 1]
                try:
                    if (col - 1) >= 0 and count_grid_nlist[row][col - 1] == '#':
                        mine_count_int += 1
                except IndexError:
                    pass

                # E position: [row][col + 1]
                try:
                    if count_grid_nlist[row][col + 1] == '#':
                        mine_count_int += 1
                except IndexError:
                    pass

                # SW position: [row + 1][col - 1]
                try:
                    if (col - 1) >= 0 and count_grid_nlist[row + 1][col - 1] == '#':
                        mine_count_int += 1
                except IndexError:
                    pass

                # S position: [row + 1][col]
                try:
                    if count_grid_nlist[row + 1][col] == '#':
                        mine_count_int += 1
                except IndexError:
                    pass

                # SE position: [row + 1][col + 1]
                try:
                    if count_grid_nlist[row + 1][col + 1] == '#':
                        mine_count_int += 1
                except IndexError:
                    pass
            
                """

                # Change '-' value of the current position to the 
                # number of mines around it. Store as string.
                count_grid_nlist[row][col] = str(mine_count_int)

    return count_grid_nlist

# =============== START MAIN LOGIC HERE =============

# Create a grid as input

"""
# Below grid is a hardcode grid option that was replaced with the
# generate_random_mine_grid() grid generating function

mine_grid_nlist = [ 
['-', '-', '-', '#', '#'],
['-', '#', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '#', '#', '-', '-'],
['-', '-', '-', '-', '-'] ]

"""

# Generate a random mine grid with mine probability (density)
mine_rows = 10   # Upgrade to input statements, let the user choose.
mine_cols = 10
mine_density = 0.35

# Function call generates our input grid
mine_grid_nlist = generate_random_mine_grid(mine_rows, mine_cols, mine_density)

count_grid_nlist = mine_count_func(mine_grid_nlist)

# print the output grid on the screen. We will print each row.
print(f"\n{'*' * 10} This is the minesweeper game. Count the mines! {'*' * 10}\n")
print("=======  STARTING MINE GRID  =======\n")

for i in range(len(mine_grid_nlist)) :
    print(mine_grid_nlist [i])

input("\n==> Press enter when you are ready to see the result! > ")
# =============================================================

# print the output grid on the screen. We will print each row.
print("\n=======  MINE COUNT GRID  =======\n")

for i in range (len(count_grid_nlist)) :
    print(count_grid_nlist[i])

print()
# =================  END PROGRAM LOGIC HERE  ====================


