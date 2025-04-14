from brain_games.engine import play_game
from brain_games.games.gcd import generate_round


def main():
    description = 'Find the greatest common divisor of given numbers.'

    def game_logic():
        for _ in range(3):
            yield generate_round()

    play_game(game_logic, description)


if __name__ == "__main__":
    main()
