from random import randint

from brain_games.cli import welcome_user


def generate_progression(start, step, lenght):
    return [start + step * i for i in range(lenght)]


def hide_element(progression):
    hidden_index = randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, str(hidden_value)


def play_progression_game():
    user_name = welcome_user()
    print('What number is missing in the progression?')

    correct_answers = 0
    max_questions = 3

    while correct_answers < max_questions:
        start = randint(1, 50)
        step = randint(1, 10)
        lenght = 10

        progression = generate_progression(start, step, lenght)

        question, correct_answer = hide_element(progression)

        print(f"Question: {' '.join(map(str, question))}")
        user_answer = input('Your answer: ').strip()

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
    play_progression_game()
