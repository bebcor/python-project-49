#!/usr/bin/env python3
from brain_games.games.prime import generate_question
from brain_games.engine import play_game
from brain_games.consts import PRIME_RULE


def main():
    play_game(PRIME_RULE, generate_question)


if __name__ == "__main__":
    main()
