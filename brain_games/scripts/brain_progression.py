#!/usr/bin/env python3
from brain_games.games.progression import generate_question
from brain_games.engine import play_game
from brain_games.consts import PROGRESSION_RULE


def main():
    play_game(PROGRESSION_RULE, generate_question)


if __name__ == "__main__":
    main()
