import random

"""  
Hi Gemini,

I need your help to write me a function to build a text representation of a mine field. 
The function should take 2 integers arguments as inputs. The first integer argument is 
the number of rows and the second is the number of columns. There should be a third 
input to indicate the proportion of mines in the field.



In the string representation of the mine field empty spaces should be indicated with 
a period. Locations with a mine should be indicated with an *. The functions should 
return the generated string.
"""


def generate_minefield(rows, cols, mine_density):
    """
    Generates a text representation of a minefield.

    Args:
      rows: The number of rows in the minefield.
      cols: The number of columns in the minefield.
      mine_density: The proportion of mines in the field (between 0 and 1).

    Returns:
      A string representation of the minefield, where '.' represents an empty space
      and '*' represents a mine.
    """

    minefield = []
    num_mines = int(rows * cols * mine_density)

    # Create a list of all possible cell coordinates
    all_cells = [(row, col) for row in range(rows) for col in range(cols)]

    # Randomly select cells for mines
    mine_locations = random.sample(all_cells, num_mines)

    # Initialize the minefield with empty spaces
    for _ in range(rows):
        row = ["."] * cols
        minefield.append(row)

    # Place mines in the selected locations
    for row, col in mine_locations:
        minefield[row][col] = "*"

    # Convert the minefield to a string representation
    minefield_str = ""
    for row in minefield:
        minefield_str += "".join(row) + "\n"

    return minefield_str


# Example usage:
rows = 5
cols = 10
mine_density = 0.2  # 20% mine density

minefield_str = generate_minefield(rows, cols, mine_density)
print(minefield_str)
