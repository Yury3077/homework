from homework4.task_5_optional import fizzbuzz


def test_that_func_return_5_values_of_fizzbuzz_game():
    assert list(fizzbuzz(5)) == ["1", "2", "Fizz", "4", "Buzz"]


def test_that_the_15_value_is_fizbuzz():
    assert list(fizzbuzz(15))[-1] == "FizzBuzz"
