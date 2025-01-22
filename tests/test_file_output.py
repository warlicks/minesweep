def test_string_match():
    """Full integration test that output matches the official outputs"""
    with open("official_output.txt") as f:
        expected_string = f.read()

    with open("minesweeper_output.txt") as f:
        my_string = f.read()

    assert expected_string == my_string
