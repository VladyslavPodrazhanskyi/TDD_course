from FizzBuzz import fizzbuzz


def test_canAssertTrue():
    assert True


def test_canCallFizzBuzz():
    fizzbuzz(1)


#  utility function for tests
def check_fizz_buzz(value, expected_retval):
    ret_val = fizzbuzz(value)
    assert ret_val == expected_retval


def test_return1_with1_passedin():
    check_fizz_buzz(1, "1")


def test_return2_with2_passedin():
    check_fizz_buzz(2, "2")


def test_return_fizz_with3_passedin():
    check_fizz_buzz(3, "Fizz")


def test_return_buzz_with5_passedin():
    check_fizz_buzz(5, "Buzz")


def test_return_fizz_with6_passedin():
    check_fizz_buzz(6, "Fizz")


def test_return_buzz_with10_passedin():
    check_fizz_buzz(10, "Buzz")


def test_return_fizzbuzz_with15_passedin():
    check_fizz_buzz(15, "FizzBuzz")
