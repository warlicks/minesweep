from doctest import OutputChecker
from minesweep import mine_locations


def test_mine_location_identification():
    """Confirm that an empyt list is returned with no mines in a row."""
    field_row = "....."
    output = mine_locations(field_row)

    assert not output


def test_single_mine_locatoin():
    """Test that we can identify location of a single mine"""
    field_row = "*"
    output = mine_locations(field_row)
    assert output == [0]


def test_two_mine_locatoin():
    """test that we can correctly locate mines in a row of just mines"""
    field_row = "**"
    output = mine_locations(field_row)
    assert output == [0, 1]


def test_mix_mine_locations():
    """Test that we can find mine locations in row with mines and empty
    spaces
    """

    field_row = ".*.*..*"
    output = mine_locations(field_row)
    assert output == [1, 3, 6]
