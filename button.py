"""
This program defines the button in the screen
"""
"""
    programed by: crypto-a(Ali Rahbar)
    Date: January 17
"""

import pygame


class Button:
    def __init__(self, text, X, Y, height, width, screen):  # init the new button
        self.text = text
        self.X = X
        self.Y = Y
        self.height = height
        self.width = width
        self.screen = screen

    def draw(self, color):  # draws the button every time. returns a button on the display
        pygame.draw.rect(self.screen, color, pygame.Rect(self.X, self.Y, self.width, self.height))
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text, (self.X + (self.width / 2 - text.get_width() / 2),
                                self.Y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):  # checks if the mouse is on the button or not. returns True or False
        if self.X < pos[0] < self.X + self.width:
            if self.Y < pos[1] < self.Y + self.height:
                return True

        return False
