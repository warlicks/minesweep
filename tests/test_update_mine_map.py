import pytest
import numpy as np
from minesweep import update_mine_map

"""comparing storage (map) to expected storage (expected map) """


def check_adjacent_counts(storage, expected_storage):
    assert np.array_equal(
        storage, expected_storage
    ), f"Expected:\n{expected_storage}\nBut got:\n{storage}"


"""Test #1: mine placed in center of grid
    UL UC UR   1  1   1
    CL *  CR   1 -999 1
    LL LC LR   1  1   1"""


def test_middle():
    storage = np.zeros((3, 3), dtype=int)
    row, col = 1, 1  # Placing the mine at the center
    expected = np.array([[1, 1, 1], [1, -999, 1], [1, 1, 1]])
    updated_storage = update_mine_map(storage, row, col)
    check_adjacent_counts(updated_storage, expected)


"""Test #2: mine placed in corner of grid
    *  UC UR   -999 1 0
    CL C  CR     1  1 0
    LL LC LR     0  0 0"""


def test_corner():
    storage = np.zeros((3, 3), dtype=int)
    row, col = 0, 0  # Placing the mine at the corner
    expected = np.array([[-999, 1, 0], [1, 1, 0], [0, 0, 0]])
    updated_storage = update_mine_map(storage, row, col)
    check_adjacent_counts(updated_storage, expected)


"""Test #3: mine placed in right edge of grid
    UL UC UR   0 1 1
    CL C  *    0 1 -999
    LL LC LR   0 1 1"""


def test_right_edge():
    storage = np.zeros((3, 3), dtype=int)
    row, col = 1, 2
    expected = np.array([[0, 1, 1], [0, 1, -999], [0, 1, 1]])
    updated_storage = update_mine_map(storage, row, col)
    check_adjacent_counts(updated_storage, expected)


"""Test #4: mine placed in bottom edge of grid
    UL UC UR   0  0   0
    CL C  CR   1  1   1
    LL *  LR   1 -999 1"""


def test_bottom_edge():
    storage = np.zeros((3, 3), dtype=int)
    row, col = 2, 1
    expected = np.array([[0, 0, 0], [1, 1, 1], [1, -999, 1]])
    updated_storage = update_mine_map(storage, row, col)
    check_adjacent_counts(updated_storage, expected)


"""Test #5: mine placed in center of larger  grid

    0  0  0   0  0
    0  1  1   1  0
    0  1 -999 1  0
    0  1  1   1  0
    0  0  0   0  0"""


def test_middle_bigger_grid():
    storage = np.zeros((5, 5), dtype=int)
    row, col = 2, 2  # Placing the mine at the center of the 5x5 grid
    expected = np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, -999, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    updated_storage = update_mine_map(storage, row, col)
    check_adjacent_counts(updated_storage, expected)


"""Test #6: mine placed in grid with pre-existing mines
    0   0    0   0  0
    1   1    1   0  0
    1  -999  2   1  1
    1   1    2 -999 1
    0   0    1   1  1"""


def test_preexisting_mine():
    storage = np.array(
        [  # load mine with pre-existing mine at [2,1]
            [0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, -999, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    row, col = 3, 3  # Place new mine at [3,3]
    expected = np.array(
        [  # expected new grid with both mines
            [0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, -999, 2, 1, 1],
            [1, 1, 2, -999, 1],
            [0, 0, 1, 1, 1],
        ]
    )
    updated_storage = update_mine_map(storage, row, col)
    check_adjacent_counts(updated_storage, expected)
