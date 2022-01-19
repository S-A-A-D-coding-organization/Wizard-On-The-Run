"""
Generates the code related to the character.
"""

# imports
import pygame
import DataBase as db
import threading
import time


class Persona:
    def __init__(self, screen, width, height): # loads and prepaires all the data for the class
        self.char = pygame.image.load("img/character/wizard.png")
        self.screen = screen
        self.width = width
        self.height = height
        self.pos = 370

    def jump(self):  # used for the jumping
        def run():
            for i in range (1, 201):
                if i <= 100:
                    self.pos = self.pos - 1
                elif i > 100:
                    self.pos = self.pos + 1
                time.sleep(0.005)

        t = threading.Thread(target=run)
        t.start()
    def movment(self):  # returns the movment info, uses data from self.jump()
        self.screen.blit(self.char,(100, self.pos))
