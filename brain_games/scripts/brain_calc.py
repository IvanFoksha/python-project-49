from brain_games.engine import play_game, MAX_QUESTION
from brain_games.games.calc import generate_round


def main():
    description = 'What is the result of the expression?'

    def geme_logic():
        for index in range(MAX_QUESTION):
            yield generate_round(index)

    play_game(geme_logic, description)


if __name__ == "__main__":
    main()
