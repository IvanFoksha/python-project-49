from brain_games.cli import welcome_user


MAX_QUESTION = 3
PROGRESSION_LENGHT = 10


def play_game(game_logic, description):
    # Вынесена общая логика игры
    user_name = welcome_user()
    print(description)

    correct_answers = 0

    for question, correct_answer in game_logic():
        print(f'Question: {question}')
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
