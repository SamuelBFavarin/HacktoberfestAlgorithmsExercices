from exercicies.medium import Medium


def test_sum_2_values():
    assert 2 == Medium().sum2Values(1, 1)
    assert 87 == Medium().sum2Values(2, 85)
    assert 5 != Medium().sum2Values(2, 2)
