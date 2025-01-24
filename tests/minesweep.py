import numpy as np


def update_mine_map(storage: np.ndarray, row: int, column: int) -> np.ndarray:
    """Updates the mine field map to when new mines are found.

    When a mine is found in a row, the counters for all the adjacent positions need to
    be updated. This way we know how many mines are adjacent to any given empty position.
    For example 3 indicates that there are mines in 3 locations adjacent to the current
    position.

    There can be a maximum of 8 positions adjacent to a given mine. See the diagram below
    for an illustration of this fact.

    UL UC UR   1 1 1
    CL *  CR   1 * 1
    LL LC LR   1 1 1

    Args:
        storage (np.ndarray): A numpy array representing a "map" of the mine field. The
          array has the same dimensions as the mine field. The values in the array are
          a count of adjacent positions with a mine.
          row (int): The row position of a mine
          column (int): The column position of the mine.

    Returns:
        np.array: The values in the array indicate the number of mines adjacent to a
          given position. The location of the mines are indicated by negative values.
    """

    # Handle updates to the upper row.
    if row - 1 >= 0 and column - 1 >= 0:
        storage[(row - 1), (column - 1)] += 1
    if row - 1 >= 0:
        storage[(row - 1), column] += 1
    if row - 1 >= 0 and column + 1 < storage.shape[1]:
        storage[(row - 1), (column + 1)] += 1

    # Handle Updates to the current row.
    if column - 1 >= 0:
        storage[row, column - 1] += 1
    if column + 1 < storage.shape[1]:
        storage[row, column + 1] += 1

    # Indicate mine position with a negative number. Even if adjacent mines impact the count
    # we can still identify which spots have mines
    storage[row, column] = -999

    # Handle updates to the row below.
    if row + 1 < storage.shape[0] and column - 1 >= 0:
        storage[row + 1, column - 1] += 1
    if row + 1 < storage.shape[0]:
        storage[row + 1, column] += 1
    if row + 1 < storage.shape[0] and column + 1 < storage.shape[1]:
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
