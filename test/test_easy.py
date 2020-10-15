from exercicies.easy import Easy


def test_sum_2_values():
    assert 2 == Easy().sum2Values(1, 1)
    assert 87 == Easy().sum2Values(2, 85)
    assert 5 != Easy().sum2Values(2, 2)
