from unittest import TestCase

from fizzbuzz import fizzbuzz


class FizzBuzzTest(TestCase):

    def test_raises_value_error_if_number_less_than_1(self):
        with self.assertRaises(ValueError):
            fizzbuzz(0)

    def test_raises_value_error_if_number_is_negative(self):
        with self.assertRaises(ValueError):
            fizzbuzz(-2)

    def test_raises_value_error_if_number_greater_than_100(self):
        with self.assertRaises(ValueError):
            fizzbuzz(101)

    def test_returns_number_if_not_fizz_nor_buzz(self):
        cases = [
            (1, '1'),
            (2, '2'),
            (4, '4'),
        ]
        for number, expected in cases:
            with self.subTest(number=number):
                result = fizzbuzz(number)
                self.assertEqual(expected, result)

    def test_returns_fizz_when_number_divisible_by_3(self):
        numbers = [3, 6]
        for number in numbers:
            with self.subTest(number=number):
                result = fizzbuzz(number)
                self.assertEqual('fizz', result)

    def test_returns_buzz_when_number_divisible_by_5(self):
        numbers = [5, 10]
        for number in numbers:
            with self.subTest(number=number):
                result = fizzbuzz(number)
                self.assertEqual('buzz', result)

    def test_returns_fizzbuzz_when_number_divisible_by_3_and_5(self):
        numbers = [15, 30]
        for number in numbers:
            with self.subTest(number=number):
                result = fizzbuzz(number)
                self.assertEqual('fizzbuzz', result)

    def test_returns_1_when_number_is_1(self):
        number = 1
        result = fizzbuzz(number)
        self.assertEqual('1', result)

    def test_returns_buzz_when_number_is_100(self):
        number = 100
        result = fizzbuzz(number)
        self.assertEqual('buzz', result)

    def test_returns_fizz_when_number_contains_3(self):
        numbers = [31, 43]
        for number in numbers:
            with self.subTest(number=number):
                result = fizzbuzz(number)
                self.assertEqual('fizz', result)

    def test_returns_buzz_when_number_contains_5(self):
        numbers = [25, 52]
        for number in numbers:
            with self.subTest(number=number):
                result = fizzbuzz(number)
                self.assertEqual('buzz', result)

    def test_returns_fizzbuzz_when_number_contains_3_and_contains_5(self):
        numbers = [35, 53]
        for number in numbers:
            with self.subTest(number=number):
                result = fizzbuzz(number)
                self.assertEqual('fizzbuzz', result)

    def test_returns_fizzbuzz_when_number_contains_3_and_is_divisible_by_5(self):
        number = 35
        result = fizzbuzz(number)
        self.assertEqual('fizzbuzz', result)

    def test_returns_fizzbuzz_when_number_is_divisible_by_3_and_contains_5(self):
        number = 51
        result = fizzbuzz(number)
        self.assertEqual('fizzbuzz', result)
