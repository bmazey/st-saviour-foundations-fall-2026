from greatest import find_greatest

def test_find_greatest():
    numbers = [0, 1, 2, 3, 4, 5]
    assert find_greatest(numbers) == 5

    numbers = [7, 8, 4, 4, 1, 0]
    assert find_greatest(numbers) == 8