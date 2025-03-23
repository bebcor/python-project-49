from brain_games.utils import generate_number


def generate_question():
    start = generate_number(1, 50)
    step = generate_number(2, 10)
    length = 10
    hidden_pos = generate_number(0, length - 1)

    progression = [str(start + step * i) for i in range(length)]
    correct_answer = progression[hidden_pos]
    progression[hidden_pos] = ".."

    return " ".join(progression), correct_answer
