import codewars_test as test
from solution import find_difference


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_difference([3, 2, 5], [1, 4, 4]), 14,
                           "{0} should equal 14".format(find_difference([3, 2, 5], [1, 4, 4])))
        test.assert_equals(find_difference([9, 7, 2], [5, 2, 2]), 106,
                           "{0} should equal 106".format(find_difference([9, 7, 2], [5, 2, 2])))
