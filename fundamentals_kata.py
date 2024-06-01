import codewars_test as test
from solution import is_palindrome


@test.describe("Fixed Tests")
def fixed_tests():
    @test.describe('sample tests')
    def sample_tests():
        test.assert_equals(is_palindrome('a'), True)
        test.assert_equals(is_palindrome('aba'), True)
        test.assert_equals(is_palindrome('Abba'), True)
        test.assert_equals(is_palindrome('malam'), True)
        test.assert_equals(is_palindrome('walter'), False)
        test.assert_equals(is_palindrome('kodok'), True)
        test.assert_equals(is_palindrome('Kasue'), False)
