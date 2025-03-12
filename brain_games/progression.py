import random
import prompt


def calc_the_progression():
    random_first_element = random.randint(0, 100)
    random_step = random.randint(1, 100)
    random_missing_element = random.randint(0, 9)
    progression_numbers = []

    current_value = random_first_element
    for i in range(10):
        progression_numbers.append(current_value)
        current_value += random_step

    correct_answer = progression_numbers[random_missing_element]
    progression_numbers[random_missing_element] = ".."

    progression_str = " ".join(map(str, progression_numbers))
    return progression_str, correct_answer


def progression_games():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    counter = 0
    while counter != 3:
        progression_str, correct_answer = calc_the_progression()
        print(f"Question: {progression_str}")

        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
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
