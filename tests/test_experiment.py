from dateutil.parser import parse
from hypothesis import given
from hypothesis.strategies import datetimes, integers


@given(datetimes())
def test_round_trip(d):
    assert parse(str(d)) == d


class FizzBuzz:
    @classmethod
    def do_it(cls, i):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz " + str(i))
            return "FizzBuzz"
        elif i % 3 == 0:
            print("Fizz " + str(i))
            return "Fizz"
        elif i % 5 == 0:
            print("Buzz " + str(i))
            return "Buzz"
        else:
            print(i)
            return str(i)


@given(integers(min_value=1,max_value=30))
def test_all_fizzbuzz_possibilities_from_1_to_30(i):
    if i % 3  == 0 and i % 5  == 0:
        assert FizzBuzz.do_it(i) == "FizzBuzz"
    elif i % 3 == 0:
        assert FizzBuzz.do_it(i) == "Fizz"
    elif i % 5 == 0:
        assert FizzBuzz.do_it(i) == "Buzz"
    else:
        assert FizzBuzz.do_it(i) == str(i)


if __name__ == '__main__':
    test_all_fizzbuzz_possibilities_from_1_to_30
