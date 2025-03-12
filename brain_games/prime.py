import random
import prompt
import math


def is_prime():
    random_element = random.randint(1, 100)
    correct_answer = 'yes'
    if random_element < 2:
        correct_answer = 'no'
    else:
        for i in range(2, math.isqrt(random_element) + 1):
            if random_element % i == 0:
                correct_answer = 'no'
    return random_element, correct_answer


def prime_games():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Is the number prime?")

    counter = 0
    while counter != 3:
        correct_answer, random_element = is_prime()
        print()

        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{user_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
