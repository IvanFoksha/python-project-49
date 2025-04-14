from brain_games.games.calc import play_calc_game
from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    if play_calc_game():
        print(f'Congratulations, {user_name}!')

if __name__ == "__main__":
    main()
