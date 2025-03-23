from brain_games import cli
from brain_games.consts import NUMBER_OF_ROUNDS
import prompt


def play_game(game_rules, generate_question):
    name = cli.welcome_user()
    print(game_rules)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = generate_question()
        user_answer = prompt.string(f"Question: {question}\nYour answer: ")

        if user_answer != correct_answer:
            error_msg = (
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(error_msg)
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
