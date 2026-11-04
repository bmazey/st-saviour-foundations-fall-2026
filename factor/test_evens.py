from evens import evens_only

def test_evens_only():
    numbers = [4, 6, 7, 9, 12]
    result = evens_only(numbers)

    assert result[0] == 4
    assert result[1] == 6
    assert result[2] == 12