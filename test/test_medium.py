import sys
from typing import Match

sys.path.append("..")
from exercicies import medium
from exercicies.medium import Medium


# create the test here
def test_name_of_function():
    assert True == False

def test_mergeSort():
    input = [6, 24, -22, -41, -21, 41, 3, 4, -11, -
             31, 18, -42, 7, 31, 19, -4, 12, 9, 37, 28]
    return_output = [-42, -41, -31, -22, -21, -11, -4,
                     3, 4, 6, 7, 9, 12, 18, 19, 24, 28, 31, 37, 41]
    assert return_output == Medium().mergeSort(input)

# description: Create a function to return next permutation of given string. i.e, rearrange string into the lexicographically next greater permutation of given string.
#              If such arrangement is not possible, return its lowest possible order
# enter parameter: string = "58523"
# return: "58532"
def test_nextPermutation(self, string):
    assert "13245" == Medium().nextPermutation("12543")
    assert "014679" == Medium().nextPermutation("976410")
    assert "73951230359" == Medium().nextPermutation("73951209533")


# description: Create a function that returns weather given string matchs given pattern
#              in pattern, * represents it can be replaced by zero or more characters and ? represents it can be replaced by exactly one character
# enter parameter: string = "abbbbcbbc" | pattern = "ab*?b*c"
# return: true
def test_matchPattern(self, string, pattern):
    assert True == Medium().matchPattern("ab", "?*")
    assert False == Medium().matchPattern("aab", "c*a*b")
    assert True == Medium().matchPattern(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "*a")

