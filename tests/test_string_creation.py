import pytest
import numpy as np
from minesweep import prepare_string_output


@pytest.fixture
def input_array():
    a = np.array([[1, 1, 1], [1, -400, 1], [1, 1, 1]])
    return a


@pytest.fixture
def expected_string1():
    return "Field #1:\n111\n1*1\n111\n"


@pytest.fixture
def expected_string2():
    return "\nField #2:\n111\n1*1\n111\n"


@pytest.fixture
def array_wo_mines():
    """Create an array without mines.

    Technically this is an invalid option. You couldn't this combination of
    counts without a mine at the center of the 3x3 array, but it's helpful to
    test that the np.where statement to convert the negative number to the * works
    """
    a = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    return a


@pytest.fixture
def expected_str_wo_mines():
    return "Field #1:\n111\n111\n111\n"


@pytest.fixture
def expected_str_wo_mines2():
    return "\nField #4:\n111\n111\n111\n"


def test_field_one(input_array, expected_string1):
    output = prepare_string_output(1, input_array)

    assert output == expected_string1


def test_field_two(input_array, expected_string2):
    output = prepare_string_output(2, input_array)

    assert output == expected_string2


def test_field_without_mines(array_wo_mines, expected_str_wo_mines):
    output = prepare_string_output(1, array_wo_mines)

    assert output == expected_str_wo_mines


def test_field_without_mines2(array_wo_mines, expected_str_wo_mines2):
    output = prepare_string_output(4, array_wo_mines)

    assert output == expected_str_wo_mines2
