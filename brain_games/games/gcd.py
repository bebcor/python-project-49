import math
from brain_games.utils import generate_number


def generate_question():
    num1 = generate_number(1, 100)
    num2 = generate_number(1, 100)
    gcd_value = math.gcd(num1, num2)
    return f"{num1} {num2}", str(gcd_value)
