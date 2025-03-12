import random
import prompt


def get_dividers(number):
    return {i for i in range(1, number + 1) if number % i == 0}


def find_gcd(number1, number2):
    dividers1 = get_dividers(number1)
    dividers2 = get_dividers(number2)
    common_dividers = dividers1.intersection(dividers2)
    return max(common_dividers)


def ask_question(number1, number2):
    print(f"Question: {number1} {number2}")
    return int(input("Your answer: "))


def GCD_games():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    counter = 0

    while counter < 3:
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        correct_answer = find_gcd(number1, number2)
        user_answer = ask_question(number1, number2)

        if user_answer == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(
                f"'{user_answer}' is a wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
