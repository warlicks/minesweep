import unittest
import numpy as np
from minesweep import extract_field_dimensions


class MyMinesweeperTests(unittest.TestCase):
    """Test if field dimensions are ints"""

    def test_parse_field_dimensions_are_integers(self):

        self.mine_map = open("mines.txt", "r")
        self.field_rows, self.field_cols = extract_field_dimensions(self.mine_map)
        self.assertIsInstance(self.field_rows, int, "No int in row value.")
        self.assertIsInstance(self.field_cols, int, "No int in column value.")
        self.mine_map.close()

    """Test if one of the values is a string and Raise Exception"""

    def test_parse_field_dimensions_strings_raise_exception(self):

        self.mine_map = open("tests_string.txt", "r")

        with self.assertRaises(ValueError):
            self.field_rows, self.field_cols = extract_field_dimensions(self.mine_map)

        self.mine_map.close()

    """Test that values are not none"""

    def test_parse_field_dimensions_values_not_none(self):

        self.mine_map = open("mines.txt", "r")
        self.field_rows, self.field_cols = extract_field_dimensions(self.mine_map)
        self.assertIsNotNone(self.field_rows, "No value in row value.")
        self.assertIsNotNone(self.field_cols, "No value in column value.")
        self.mine_map.close()

    """Test if one of the values are None and Raise Exception"""

    def test_parse_field_dimensions_none_raise_exception(self):

        self.mine_map = open("tests_none.txt", "r")

        with self.assertRaises(ValueError):
            self.field_rows, self.field_cols = extract_field_dimensions(self.mine_map)

        self.mine_map.close()

    """Test that values are within 1 - 101"""

    def test_parse_field_dimensions_range(self):

        self.mine_map = open("mines.txt", "r")
        self.field_rows, self.field_cols = extract_field_dimensions(self.mine_map)
        self.assertGreater(
            self.field_rows, -1, "Row value is not greater than 0."
        )  # Asserting that number test is > 0
        self.assertGreater(self.field_cols, -1, "Column value is not greater than 0.")

        self.assertLess(self.field_rows, 101, "Row value is not less than 101")
        self.assertLess(self.field_cols, 101, "Column value is not less than 101")
        self.mine_map.close()

    """Test that values are within 1 - 101 and Raise Exception"""

    def test_parse_field_dimensions_greater_101(
        self,
    ):  # allows for acceptence 101 in the code / program

        self.mine_map = open("tests_value_range_101.txt", "r")

        with self.assertRaises(ValueError):
            self.field_rows, self.field_cols = extract_field_dimensions(self.mine_map)

        self.mine_map.close()

    """Test that values are within -1 and Raise Exception"""

    def test_parse_field_dimensions_negative_value(
        self,
    ):  # allows for acceptence -1 in the code / program

        self.mine_map = open("tests_value_range_negative.txt", "r")

        with self.assertRaises(ValueError):
            self.field_rows, self.field_cols = extract_field_dimensions(self.mine_map)

        self.mine_map.close()


if __name__ == "__main__":
    unittest.main()
