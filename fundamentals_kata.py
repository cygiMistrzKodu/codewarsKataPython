import codewars_test as test
from solution import grille


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(grille("abcdef", 5), "df")
        test.assert_equals(grille("", 5), "")
        test.assert_equals(grille("abcd", 1), "d")
        test.assert_equals(grille("0abc", 2), "b")
        test.assert_equals(grille("ab", 255), "ab")
        test.assert_equals(grille("ab", 256), "")
        test.assert_equals(grille("abcde", 32), "")
        test.assert_equals(grille("tcddoadepwweasresd", 77098), "codewars")
