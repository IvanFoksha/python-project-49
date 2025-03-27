from random import randint, choice

from brain_games.cli import welcome_user


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        raise ValueError(f'Неизвестный оператор: {operator}')


def play_calc_game():
    user_name = welcome_user()
    print('What is the result of the expression?')

    correct_answers = 0
    max_questions = 3

    while correct_answers < max_questions:
        a = randint(1, 100)
        b = randint(1, 100)
        operator = choice(['+', '-', '*'])

        correct_answer = calculate(a, b, operator)

        print(f'Question: {a} {operator} {b}')
        user_answer = input('Your answer: ').strip().lower()

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')


def main():
    play_calc_game()
