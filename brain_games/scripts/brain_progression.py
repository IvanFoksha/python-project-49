from brain_games.engine import play_game
from brain_games.games.progression import generate_round


def main():
    description = 'What number is missing in the progression?'

    def geme_logic():
        for _ in range(3):
            yield generate_round()

    play_game(geme_logic, description)


if __name__ == "__main__":
    main()
