"""
Displays the welcome message for the game explaining the objective for the player before the game begins.
"""


def welcome_script() -> None:
    print("""
\033[34m
Welcome to the \033[1;93mHIT THE WATERMELON\033[0;34m game! 🎯🍉

In this game, your goal is to \033[1;4;34mdestroy the watermelon\033[0;34m — 
either by\033[1;3;34m crushing it\033[0;34m with your tank or by\033[1;3;34m shooting it from a distance.
\033[1;93m
Be aware!!! This game has point system:\033[0;34m
· You start with 100 points.
· Each move forward or backward costs 10 points.
· Each missed shot costs 15 points.
· Each successful shot gives you 20 points.
· Crushing a watermelon gives you 50 points.
\033[0;1;34m
Here’s the game board and the command menu:
\033[0m
""")
