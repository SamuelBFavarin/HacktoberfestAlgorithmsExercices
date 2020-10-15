from exercicies.refactoring import Refactoring


def test_sum_2_values():
    assert 2 == Refactoring().sum2Values(1, 1)
    assert 87 == Refactoring().sum2Values(2, 85)
    assert 5 != Refactoring().sum2Values(2, 2)
