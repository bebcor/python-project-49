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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    counter = 0
    while counter != 3:
        random_element, correct_answer = is_prime() 
        print(f"Question: {random_element}") 

        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{user_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
