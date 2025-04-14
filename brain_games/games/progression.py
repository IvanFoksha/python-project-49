from brain_games.engine import PROGRESSION_LENGHT
from random import randint


def generate_progression(start, step, lenght):
    return [start + step * i for i in range(lenght)]


def hide_element(progression):
    hidden_index = randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, str(hidden_value)


def generate_round():
    start = randint(1, 50)
    step = randint(1, 10)
    lenght = PROGRESSION_LENGHT

    progression = generate_progression(start, step, lenght)
    question, correct_answer = hide_element(progression)

    return ' '.join(map(str, question)), correct_answer
