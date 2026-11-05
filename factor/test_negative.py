from negative import find_negative

def test_find_negative():
    numbers = [6, 5, 4, -7, 8]
    assert find_negative(numbers) == -7

    numbers = [-1, 3, 6, 7, 9]
    assert find_negative(numbers) == -1

    # should return 0 when no negative number!
    numbers = [4, 5, 6, 7, 8]
    assert find_negative(numbers) == 0