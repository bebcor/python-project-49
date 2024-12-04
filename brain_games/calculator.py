import random
import prompt


def calculator_games():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    counter = 0

    while counter != 3:
        random_number_one = random.randint(0, 10)
        random_number_two = random.randint(0, 10)
        random_arithmetic_operation = random.choice("+-*")
        print(f"Question: {random_number_one} {random_arithmetic_operation} {random_number_two}")

        if random_arithmetic_operation == "+":
            correct_answer = random_number_one + random_number_two
        elif random_arithmetic_operation == "-":
            correct_answer = random_number_one - random_number_two
        elif random_arithmetic_operation == "*":
            correct_answer = random_number_one * random_number_two

        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            counter += 1

        else:
            print(f"'{user_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            counter = 0

    print(f"Congratulations, {name}!")
