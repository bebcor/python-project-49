import math
from brain_games.utils import generate_number


def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = generate_number(1, 100)
    return str(number), 'yes' if is_prime(number) else 'no'
