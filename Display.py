"""
This script generates the code for the graphics.
"""

# imports
import pygame
import button
import Character
import Ground
import DataBase as db

bg = pygame.image.load('img/background/ground.jpeg')


class Game:  # when executed the games gui start working

    """
    programed by: crypto-a(Ali Rahbar)
    Date: January 17
    """

    def __init__(self):  # loads and prepares all the data for the class

        pygame.init()
        res = (700, 550)
        self.screen = pygame.display.set_mode(res)
        pygame.display.set_caption("Wizard on The Run")

        bg_sound = pygame.mixer.Sound('sounds/background.mp3')  # play music
        bg_sound.play()

    def start_page(self):  # this shows the start page before starting the game
        play_button = button.Button("Play", 300, 250, 50, 100, self.screen)
        run = True
        while run:  # runs the first scene
            pos = (play_button.is_over(pygame.mouse.get_pos()) == True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # the quit settings
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and pos:  # if button is clicked
                    run = False
                    break
            self.screen.blit(bg, (0, 0))

            if pos:
                play_button.draw((225, 255, 0))
            else:
                play_button.draw((225, 255, 200))

            pygame.display.update()


    def screen_update(self):  # refreshes the display every time
        # ToDo
        pass  # Delete this

    def colition(self):  # checks for coalitions
        # ToDo
        pass  # Delete this
