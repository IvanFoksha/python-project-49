from random import randint


def gcd_function(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return str(a + b)


def generate_round():
    a = randint(1, 100)
    b = randint(1, 100)
    correct_answer = gcd_function(a, b)
    question = f'{a} {b}'
    return question, correct_answer
