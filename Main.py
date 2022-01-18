"""
This script always runs first.
It Starts the project and executes all the code to run the game.
"""


# imports
import Display
import DataBase as db
"""
programed by: crypto-a(Ali Rahbar)
Date: January 18
"""

def execute(): # when this function is executed, the game will start # ToDo
    Program = Display.Game()
    Program.start_page()
    Program.screen_update()



# Do not edit this part of the code
if __name__ == "__main__": # This script starts the Program
    execute()