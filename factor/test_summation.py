from summation import summation

def test_summation():
    numbers = [0, 1, 2, 3]
    assert summation(numbers) == 6

    numbers = [-1, 2, 3, 4]
    assert summation(numbers) == 8