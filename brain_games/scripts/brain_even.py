from random import randint

from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def valide_inpute(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['yes', 'no']:
            return user_input
        print('Answer "yes" if the number is even, otherwise answer "no".')


def play_even_game():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    max_questions = 3

    while correct_answers < max_questions:
        number = randint(1, 100)
        print(f'Question: {number}')

        user_answer = valide_inpute('Your answer: ')

        correct_answer = 'yes' if is_even(number) else 'no'

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            return

    print(f'Congratulations, {user_name}!')


def main():
    play_even_game()
