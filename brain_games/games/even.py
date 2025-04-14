from random import randint


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return question, correct_answer
