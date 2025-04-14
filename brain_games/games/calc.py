from random import randint


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        raise ValueError(f'Неизвестный оператор: {operator}')


def generate_round(index):
    operations = ['+', '-', '*']
    operator = operations[index]
    a = randint(1, 100)
    b = randint(1, 100)

    if operator == '-':
        a, b = max(a, b), min(a, b)

    correct_answer = str(calculate(a, b, operator))
    question = f'{a} {operator} {b}'
    return question, correct_answer
