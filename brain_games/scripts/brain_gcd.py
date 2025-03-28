from random import randint

from brain_games.cli import welcome_user


def gcd_function(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def play_gcd_game():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0
    max_questions = 3

    while correct_answers < max_questions:
        a = randint(1, 100)
        b = randint(1, 100)

        correct_answer = gcd_function(a, b)

        print(f'Question: {a} {b}')
        user_answer = input('Your answer: ').strip()

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
    play_gcd_game()
