from exercicies.easy import Easy


def test_sum_2_values():
    assert 2 == Easy().sum2Values(1, 1)
    assert 87 == Easy().sum2Values(2, 85)
    assert 5 != Easy().sum2Values(2, 2)


def test_manipulate_list():

    enter_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return_list = [0, 1, 4, 3, 8, 10, 12, 7, 16, 9,
                   20, 11, 24, 13, 28, 30, 32, 17, 36, 19, 40]

    assert return_list == Easy().manipulateList(enter_list)


def test_number_of_consonants():

    assert 6 == Easy().numberOfConsonants('DDDFFF')
    assert 0 == Easy().numberOfConsonants('AAAAAAA')
    assert 5 == Easy().numberOfConsonants('78FFSAORF##2')


def test_find_missing_number():

    assert 6 == Easy().findTheMissingNumber([3, 7, 1, 2, 8, 4, 5])
    assert 2 == Easy().findTheMissingNumber([3, 7, 1, 6, 8, 4, 5])


def test_have_sum_two_integers():

    assert True == Easy().haveSumByTwoIntegers([5, 7, 1, 2, 8, 4, 3], 10)
    assert False == Easy().haveSumByTwoIntegers([5, 7, 1, 2, 8, 4, 3], 19)
