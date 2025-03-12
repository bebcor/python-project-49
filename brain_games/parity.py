import random
import prompt


def even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0

    while counter != 3:
        random_number = random.randint(0, 10)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f"Question: {random_number}")
        user_answer = input("Your answer: ")

        if user_answer == "yes" and correct_answer = 'yes':
            print("Correct!")
            counter += 1

        elif user_answer == "no" and correct_answer = 'no':
            print("Correct!")
            counter += 1

        else:
            print(f"'{user_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            counter = 0
            break

    print(f"Congratulations, {name}!")
