def fizzbuzz(number: int) -> str:
    if not (1 <= number <= 100):
        raise ValueError
    result = ''
    if number % 3 == 0:
        result += 'fizz'
    if number % 5 == 0:
        result += 'buzz'
    if result:
        return result
    return str(number)
