# games_library/__init__.py
# Import the run_snake_game function from the snake module
from .snake import run_snake_game
# Import the run_pong_game function from the new pong module
from .pong import run_pong_game

# Define a function that can be called to list all available games
def list_games():
    """Lists the available games in this library."""
    print("Available Games:")
    print("- run_snake_game()")
    print("- run_pong_game()")

# A main function to start a game, useful for a command-line interface
def play_game(game_name):
    """
    Starts the specified game.
    Example: play_game('snake')
    """
    if game_name.lower() == 'snake':
        print("Starting the Snake game...")
        run_snake_game()
    elif game_name.lower() == 'pong':
        print("Starting the Pong game...")
        run_pong_game()
    else:
        print(f"Game '{game_name}' not found.")
        list_games()