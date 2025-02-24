"""
The Tank class represents the player's tank in the game, including:
- position
- direction
- shots fired in each direction
- target position
- game interactions (e.g., movement, shooting, stats).

The tank can move around the board, rotate in four directions, shoot towards a target, and track statistics.
"""


import random


class Tank:
    def __init__(self, x = 5, y = 5):
        """
        Initializes the Tank object with its starting position, direction, size of the board, and initializes
        game stats such as shots fired in different directions, successful shots, and crushed targets.

        :param x: The x-coordinate of the tank's initial position (default is 5)
        :param y: The y-coordinate of the tank's initial position (default is 5)
        """
        self.tank_x = x
        self.tank_y = y
        self.size = 10
        self.tank_direction = '▲'
        self.shots_fired_to_north = 0
        self.shots_fired_to_south = 0
        self.shots_fired_to_west = 0
        self.shots_fired_to_east = 0
        self.successful_shots = 0
        self.target_crushed = 0
        self.message = ''
        self.target_x = None
        self.target_y = None
        self.points = 100
        self.create_target()


    def create_board(self) -> None:
        """
        Creates and prints the game board, showing the tank, the target, and the menu for the game controls.
        It updates the board each time it is called.

        :return: None
        """
        for i in range(self.size):
            for j in range(self.size):
                if i == self.tank_y and j == self.tank_x:
                    print(f'\033[93m{self.tank_direction}\033[0m', end='  ')
                elif i == self.target_y and j == self.target_x:
                    print('\033[32m⊛\033[0m', end='  ')
                else:
                    print('.', end='  ')
            print()

        print()
        print(f'{self.message}')
        print()
        print('\033[1;34m*** MENU ***\033[0m')
        print('Key w : Tank moves forward')
        print('Key s : Tank moves backward')
        print('Key a : Tank will turn anti-clockwise')
        print('Key d : Tank will turn clockwise')
        print('Key * : Tank fires a shot')
        print('Key i : Show stats')
        print('Key q : Quit')


    def create_target(self) -> None:
        """
        Randomly generates a target's (x, y) coordinates on the board, ensuring that the target does not
        overlap with the tank's position. This target will be the object the player needs to hit or crush.

        :return: None
        """
        while True:
            self.target_x = random.randint(0, self.size - 1)
            self.target_y = random.randint(0, self.size - 1)
            if (self.target_x, self.target_y) != (self.tank_x, self.tank_y):
                break


    def start_game(self) -> None:
        """
        Starts the game loop, allowing the player to interact with the game. It continuously shows the board,
        processes user input for commands (e.g., moving the tank, shooting, showing stats), and controls
        the game's flow.

        :return: None
        """
        while True:
            if self.points <= 0:
                print('\033[31mOut of points!\033[0m')
                self.show_stats()
                break
            else:
                self.create_board()
                print()
                self.message = ''       # Reset message each turn
                print(f'Current points: {self.points}')
                command = input('\033[4mEnter any key from menu: \033[0m').strip().lower()
                print()

                if command == 'w':
                    self.move_forward()
                elif command == 's':
                    self.move_backward()
                elif command == 'a':
                    self.turn_left()
                elif command == 'd':
                    self.turn_right()
                elif command == '*':
                    self.shoot()
                elif command == 'i':
                    self.show_stats()
                elif command == 'q':
                    print('\033[31mExiting game...\033[0m')
                    break
                else:
                    self.message = '\033[31mInvalid command!\033[0m'


    def move_forward(self) -> None:
        """
        Moves the tank forward in its current direction, checking for board boundaries.
        If the tank reaches the board's edge, it gives a message and does not move further.

        :return: None
        """
        if self.tank_direction == '▲' and self.tank_y > 0:
            self.tank_y -= 1
        elif self.tank_direction == '▶' and self.tank_x < self.size - 1:
            self.tank_x += 1
        elif self.tank_direction == '▼' and self.tank_y < self.size - 1:
            self.tank_y += 1
        elif self.tank_direction == '◀' and self.tank_x > 0:
            self.tank_x -= 1
        else:
            self.message = '\033[31mBoard edge reached, turn around!\033[0m'

        self.check_if_target_crushed()
        self.points -= 10


    def check_if_target_crushed(self) -> None:
        """
        Checks if the tank's current position is the same as the target's position.
        If so, the tank crushes the target and a new target is generated.

        :return: None
        """
        if self.tank_x == self.target_x and self.tank_y == self.target_y:
            self.message = '\033[93mYou crushed the watermelon!\033[0m'
            self.target_crushed += 1
            self.create_target()
            self.points += 50


    def turn_left(self) -> None:
        """
        Rotates the tank 90 degrees anti-clockwise (left) and updates the tank's direction.

        :return: None
        """
        directions = {
            '▲': '◀',
            '◀': '▼',
            '▼': '▶',
            '▶': '▲'
        }
        self.tank_direction = directions[self.tank_direction]


    def turn_right(self) -> None:
        """
        Rotates the tank 90 degrees clockwise (right) and updates the tank's direction.

        :return: None
        """
        directions = {
            '▲': '▶',
            '▶': '▼',
            '▼': '◀',
            '◀': '▲'
        }
        self.tank_direction = directions[self.tank_direction]


    def move_backward(self) -> None:
        """
        Moves the tank backward by turning the tank 180 degrees (two right turns) and then moving forward.

        :return: None
        """
        self.turn_right()
        self.turn_right()
        self.move_forward()
        self.turn_right()
        self.turn_right()
        self.points -= 10


    def shoot(self) -> None:
        """
        Registers a shot fired in the current direction and checks if it hits the target.

        - Increments the shot count for the specific direction (North, South, East, or West).
        - If the shot aligns with the target in the same row/column and correct direction, it is considered a hit.
        - If the shot is successful, updates the success count and displays a message.
        - If the shot misses, displays a failure message.
        - Regardless of the result, generates a new target after each shot.

        :return: None
        """
        if self.tank_direction == '▲':
            self.shots_fired_to_north += 1
        elif self.tank_direction == '▼':
            self.shots_fired_to_south += 1
        elif self.tank_direction == '▶':
            self.shots_fired_to_east += 1
        else:
            self.shots_fired_to_west += 1

        if (
            (self.tank_direction == '▲' and self.tank_x == self.target_x and self.tank_y > self.target_y)
            or
            (self.tank_direction == '▼' and self.tank_x == self.target_x and self.tank_y < self.target_y)
            or
            (self.tank_direction == '▶' and self.tank_y == self.target_y and self.tank_x < self.target_x)
            or
            (self.tank_direction == '◀' and self.tank_y == self.target_y and self.tank_x > self.target_x)
        ):
            self.successful_shots += 1
            self.points += 20
            self.message = '\033[92mYou hit the watermelon!\033[0m'
        else:
            self.message = '\033[31mYou missed.\033[0m'
            self.points -= 15
        self.create_target()


    def show_stats(self) -> None:
        """
        Displays the player's statistics, including:
        - Number of shots fired in each direction (North, South, East, West).
        - Total successful shots.
        - Number of watermelons crushed.
        - Current tank coordinates.
        - Current tank facing direction.

        The function then prompts the user to either continue the game or quit.
        If the user presses "q", the game exits; otherwise, it returns to the game loop.

        :return: None
        """
        print()
        print('\033[1;34m*** STATISTICS ***\033[0m')
        print(f'Shots fired to north: {self.shots_fired_to_north}')
        print(f'Shots fired to south: {self.shots_fired_to_south }')
        print(f'Shots fired to east: {self.shots_fired_to_east }')
        print(f'Shots fired to west: {self.shots_fired_to_west}')
        print(f'Successful shots: {self.successful_shots}')
        print(f'Watermelons crushed: {self.target_crushed}')
        print(f'Current tank coordinates (x, y): ({self.tank_x + 1},{self.tank_y + 1})')

        directions_text = {
            '▲': 'North',
            '▼': 'South',
            '▶': 'East',
            '◀': 'West'
        }
        print(f'Current tank direction: {directions_text[self.tank_direction]}')
        print()

        while True:
            user_input = input('\033[4mPress Enter to continue, or "q" to quit:\033[0m ').strip().lower()
            if user_input == '':
                break
            elif user_input == 'q':
                print()
                print('\033[31mExiting game...\033[0m')
                exit()
            else:
                print()
                print('\033[31mInvalid option! Press Enter to continue or "q" to quit.\033[0m')
                print()
