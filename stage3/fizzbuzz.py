from abc import ABC, abstractmethod
from typing import List  # noqa


def fizzbuzz(number: int) -> str:
    fizzbuzz = FizzBuzz()
    return fizzbuzz.evaluate(number)


class FizzBuzz(object):

    def __init__(self):
        self.__rules = [
            DivisibleAndContainsRules(3, 'fizz'),
            DivisibleAndContainsRules(5, 'buzz'),
            DivisibleRules(7, 'wizz'),
        ]  # type: List[Rules]

    def evaluate(self, asked_number: int) -> str:
        self.__validate_is_in_range(asked_number)
        result = ''.join(rules.word for rules in self.__rules if rules.matches(asked_number))
        if result:
            return result
        return str(asked_number)

    def __validate_is_in_range(self, asked_number: int) -> None:
        if not (1 <= asked_number <= 100):
            raise ValueError


class Rules(ABC):

    def __init__(self, number: int, word: str) -> None:
        self._number = number
        self.__word = word

    @abstractmethod
    def matches(self, number: int) -> bool:
        raise NotImplementedError  # pragma: nocover

    @property
    def word(self) -> str:
        return self.__word


class DivisibleAndContainsRules(Rules):

    def matches(self, asked_number: int) -> bool:
        number = Number(asked_number)
        return (
            number.is_divisible_by(self._number)
            or number.contains(self._number)
        )


class DivisibleRules(Rules):

    def matches(self, asked_number: int) -> bool:
        number = Number(asked_number)
        return number.is_divisible_by(self._number)


class Number(int):

    def is_divisible_by(self, divisor: int) -> bool:
        return (self % divisor == 0)

    def contains(self, digit: int) -> bool:
        return (str(digit) in str(self))
