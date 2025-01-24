import numpy as np


def update_mine_map(storage: np.ndarray, row: int, column: int) -> np.ndarray:
    """Updates the mine field map when a new mine is found.

    This function updates the mine field map by incrementing the adjacent cells
    of the given mine cell. The adjacent cells that are not mines will have their
    values incremented by 1. The mine cell itself is set to -999.

    Args:
        storage (np.ndarray): A 2D numpy array representing the mine field grid.
        row (int): The row index where the new mine is placed.
        column (int): The column index where the new mine is placed.

    Returns:
        np.ndarray: The updated mine field grid with the new mine placed, and adjacent cells' mine counts updated.
    """

    # Handle updates to the upper row.
    if row - 1 >= 0 and column - 1 >= 0 and storage[(row - 1), (column - 1)] != -999:
        storage[(row - 1), (column - 1)] += 1
    if row - 1 >= 0 and storage[(row - 1), column] != -999:
        storage[(row - 1), column] += 1
    if row - 1 >= 0 and column + 1 < storage.shape[1] and storage[(row - 1), (column + 1)] != -999:
        storage[(row - 1), (column + 1)] += 1

    # Handle updates to the current row.
    if column - 1 >= 0 and storage[row, column - 1] != -999:
        storage[row, column - 1] += 1
    if column + 1 < storage.shape[1] and storage[row, column + 1] != -999:
        storage[row, column + 1] += 1

    # Indicate mine position with a negative number
    storage[row, column] = -999

    # Handle updates to the row below.
    if row + 1 < storage.shape[0] and column - 1 >= 0 and storage[row + 1, column - 1] != -999:
        storage[row + 1, column - 1] += 1
    if row + 1 < storage.shape[0] and storage[row + 1, column] != -999:
        storage[row + 1, column] += 1
    if row + 1 < storage.shape[0] and column + 1 < storage.shape[1] and storage[row + 1, column + 1] != -999:
        storage[row + 1, column + 1] += 1

    return storage

def mine_locations(current_data: str) -> list:
    """Find the position of mines in a row of the mine field

    For this project our row of mines is represented by a string. In the string mines are
    represented by "*". Positions without a mine are denoted by a period ".". The function
    checks the string for mines and records the position in the string where each mine
    is located.

    Args:
        current_data (str): A string representing a row in a mine field. Mines should be
          represented as a "*". Empty positions without a mine are represented with a ".".

    Returns:
        list: The list contains the position in the string where a mine is located. If no
          mines are found the list is empty.
    """
    return [i for i in range(len(current_data)) if current_data.startswith("*", i)]


def extract_field_dimensions(input_file: "TextIOWrapper") -> tuple:
    """Extract the dimensions of a mine field

    The dimensions of the mine field are indicated by a row with 2 numbers indicating
    the number of rows and number of columns. The first is the number of rows and the
    second is the number of columns. Two values are separated are by a space.

    Args:
        input_file (TextIOWrapper): The file with the mine field files.

    Returns:
        tuple: The row and column values of the mine field.
    """
    field_dim = input_file.readline().strip("\n")
    field_rows = int(field_dim.split(" ")[0])
    field_cols = int(field_dim.split(" ")[1])

    return field_rows, field_cols


def prepare_string_output(field_index: int, field_counter: np.ndarray) -> str:
    """Prepares the mine field map to be written output.

    A little bit of work needs to happen to take the numpy array and turn it into the
    expected format. Mine location values are converted from negative to an "*". Next
    extraneous characters are stripped out.

    Expected format for a given field should follow the example below:

    Field 1:
    *100
    2210
    1*10
    1110

    Args:
        field_index (int): An index of the current mine field being parsed.
        field_counter (np.ndarray): The values in the array indicate the number of mines
          adjacent to a given position. The location of the mines are indicated by
          negative values.

    Returns:
        str: A string representing the mine field. See details above for the expected
          structure.
    """
    if field_index == 1:
        output = f"Field #{field_index}:\n"
    else:
        output = f"\nField #{field_index}:\n"

    field_counter = field_counter.astype(int)
    # replace mine locations with * and convert to string
    array_string = (
        np.array2string(
            np.where(field_counter < 0, "*", field_counter),
            max_line_width=1000,
            threshold=np.inf,
            separator="",
        )
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .replace("\n ", "\n")  # Strip whites after line return
    )

    return output + array_string + "\n"


# Note to self: readline method is an iterator. Each time I call it it goes to the next line

if __name__ == "__main__":
    # Open the file.
    # TODO: Put this all within a context manager?
    mine_map = open("mines.txt", "r")
    field_index = 1
    # Find the dimensions of the current mine field.
    field_rows, field_cols = extract_field_dimensions(mine_map)

    while field_rows != 0:
        # Create an array to hold the mine field map/counts.
        field_counter = np.zeros((field_rows, field_cols))
        print(f"The current mine field is {field_rows} rows by {field_cols} columns")

        for i in range(field_rows):
            current_data = mine_map.readline().strip("\n")
            mines = mine_locations(current_data)
            if not mines:
                continue
            else:
                for mine in mines:
                    field_counter = update_mine_map(field_counter, i, mine)
        output_string = prepare_string_output(field_index, field_counter)

        # Write the field map out after each field incase program fails.
        with open("./minesweeper_output.txt", mode="a") as f:
            f.write(output_string)

        field_index += 1
        field_rows, field_cols = extract_field_dimensions(mine_map)

    mine_map.close()
