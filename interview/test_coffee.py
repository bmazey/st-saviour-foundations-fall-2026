from coffee import classify

def test_coffee():
    # verify cases for coffee classifier
    assert classify(2.50) == 'dunkin donuts'
    assert classify(5.0) == 'dunkin donuts'

    assert classify(5.2) == 'blank street'
    assert classify(10.8) == 'blank street'

    assert classify(11.0) == 'starbucks'
    assert classify(17.10) == 'starbucks'

    assert classify(17.50) == 'cafe paradiso'
    assert classify(19.00) == 'cafe paradiso'

    assert classify(0.0) == 'error'
    assert classify(-1.0) == 'error'
