from brain_games.utils import generate_number
import random


def calculate(num1: int, num2: int, operation: str):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2


def generate_question():
    num1 = generate_number(1, 100)
    num2 = generate_number(1, 100)
    operation = random.choice("+-*")
    question = f"{num1} {operation} {num2}"
    correct_answer = str(calculate(num1, num2, operation))
    return question, correct_answer
