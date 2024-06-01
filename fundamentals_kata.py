import codewars_test as test

try:
    from solution import zeroFuel as zero_fuel
except ImportError:
    from solution import zero_fuel


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(zero_fuel(50, 25, 2), True)
        test.assert_equals(zero_fuel(100, 50, 1), False)
