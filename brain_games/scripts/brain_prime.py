from random import randint

from brain_games.cli import welcome_user


def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def play_game_prime_number():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0
    max_questions = 3

    while correct_answers < max_questions:
        number = randint(1, 100)

        correct_answer = "yes" if prime_number(number) else "no"

        print(f'Question: {number}')
        user_answer = input('Your answer: ').strip().lower()

        if user_answer == correct_answer:
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
    play_game_prime_number()
