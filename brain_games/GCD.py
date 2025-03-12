import random
import prompt


def GCD_games():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    counter = 0

    while counter != 3:
        random_number_one = random.randint(1, 10)
        random_number_two = random.randint(1, 10)
        print(f"Question: {random_number_one} {random_number_two}")

        dividers_number_one = set()
        dividers_number_two = set()

        for i in range(1, random_number_one + 1):
            if random_number_one % i == 0:
                dividers_number_one.add(i)

        for i in range(1, random_number_two + 1):
            if random_number_two % i == 0:
                dividers_number_two.add(i)

        intersection = dividers_number_one.intersection(dividers_number_two)
        correct_answer = max(intersection)
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{user_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
