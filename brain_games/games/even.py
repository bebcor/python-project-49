from brain_games.utils import generate_number


def is_even(number: int):
    return number % 2 == 0


def generate_question():
    number = generate_number(1, 100)
    return str(number), "yes" if is_even(number) else "no"
