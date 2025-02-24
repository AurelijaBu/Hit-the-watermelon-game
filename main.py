"""
Main game entry point.

This file:
- Displays the welcome screen (`welcome_script`).
- Initializes the `Tank` object.
- Starts the game (`tank.start_game()`).

The program execution begins by calling the `main()` function.
"""


from game_files.tank import Tank
from game_files.welcome_script import welcome_script


def main():
    welcome_script()
    tank = Tank()
    tank.start_game()


main()
