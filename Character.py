"""
Generates the code related to the character.
"""

# imports
import pygame
import DataBase as db
import threading
import time


class Persona:  # this class is to render the wizard image and also is used for the jumping animation for the wizard
    def __init__(self, screen, width, height):  # loads and prepares all the data for the class this is for the
        # characters and the spider to appear onto the main code
        self.char = pygame.image.load("img/character/wizard.png")
        self.screen = screen
        self.width = width
        self.height = height

    def jump(self):  # used for the jumping
        def run():
            jump_sound = pygame.mixer.Sound('sounds/jump.mp3')  # play music
            jump_sound.play()
            for i in range(1, 301):
                if i < 150:
                    db.save('pos', db.call('pos') - 1)
                elif i > 150:
                    db.save('pos', db.call('pos') + 1.5)
                    if db.call('pos') > 370:
                        break
                time.sleep(0.003)

            db.save('Jump', False)

        if not db.call('Jump'):
            t = threading.Thread(target=run)
            t.start()
            db.save('Jump', True)

    def movment(self):  # returns the movment info, uses data from self.jump()
        self.screen.blit(self.char, (100, db.call('pos')))
