import codewars_test as test
from solution import final_grade

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(final_grade(100, 12), 100)
        test.assert_equals(final_grade(85, 5), 90)