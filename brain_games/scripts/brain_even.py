from brain_games.engine import play_game, MAX_QUESTION
from brain_games.games.even import generate_round


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'

    def game_logic():
        for _ in range(MAX_QUESTION):
            yield generate_round()

    play_game(game_logic, description)


if __name__ == "__main__":
    main()
