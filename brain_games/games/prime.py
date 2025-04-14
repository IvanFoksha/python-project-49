from random import randint


def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = randint(1, 100)
    correct_answer = "yes" if prime_number(number) else "no"
    question = str(number)
    return question, correct_answer
