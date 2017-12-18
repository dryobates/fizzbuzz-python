from abc import ABC


def fizzbuzz(number: int) -> str:
    fizzbuzz = FizzBuzz()
    return fizzbuzz.evaluate(number)


class FizzBuzz(object):

    def __init__(self):
        self.__fizz_rules = DivisibleAndContainsRules(3)  # type: Rules
        self.__buzz_rules = DivisibleAndContainsRules(5)  # type: Rules

    def evaluate(self, asked_number: int) -> str:
        self.__validate_is_in_range(asked_number)
        result = ''
        if self.__fizz_rules.matches(asked_number):
            result += 'fizz'
        if self.__buzz_rules.matches(asked_number):
            result += 'buzz'
        if result:
            return result
        return str(asked_number)

    def __validate_is_in_range(self, asked_number: int) -> None:
        if not (1 <= asked_number <= 100):
            raise ValueError


class Rules(ABC):

    def matches(self, number: int) -> bool:
        raise NotImplementedError  # pragma: nocover


class DivisibleAndContainsRules(Rules):

    def __init__(self, number: int) -> None:
        self.__number = number

    def matches(self, asked_number: int) -> bool:
        number = Number(asked_number)
        return (
            number.is_divisible_by(self.__number)
            or number.contains(self.__number)
        )


class Number(int):

    def is_divisible_by(self, divisor: int) -> bool:
        return (self % divisor == 0)

    def contains(self, digit: int) -> bool:
        return (str(digit) in str(self))
