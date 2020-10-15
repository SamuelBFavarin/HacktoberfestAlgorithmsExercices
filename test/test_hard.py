from exercicies.hard import Hard


def test_sum_2_values():
    assert 2 == Hard().sum2Values(1, 1)
    assert 87 == Hard().sum2Values(2, 85)
    assert 5 != Hard().sum2Values(2, 2)
