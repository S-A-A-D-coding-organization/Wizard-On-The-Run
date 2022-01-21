"""
This script always runs first.
It Starts the project and executes all the code to run the game.
"""


# imports
import Display

"""
programed by: crypto-a(Ali Rahbar)
Date: January 18 
"""

def execute(): # when this function is executed, the game will start
    try:
        Program = Display.Game()
        Program.start_page()
    except:
        pass

# Do not edit this part of the code
if __name__ == "__main__": # This script starts the Program
    execute()
