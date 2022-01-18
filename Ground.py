"""
This scripts processes and generates the path for the Dino
"""

# imports
import pygame
import DataBase as db

"""
programed by: crypto-a(Ali Rahbar)
Date: January 18
"""


class Path:
    def __init__(self, screen, bg, spider):  # prepare the path, import the picture, etc.
        self.screen = screen
        self.bg = bg
        self.spider = spider
        self.x = 0
    def spider_generator(self):  # it returns random spiders in diffrent positions and sizes
        # ToDo
        pass  # Delete this

    def path_generator(self):  # it generates the path with the info from spider_generator and returns it to the display
        self.x = self.x - 1
        #print(self.x)
        '''if self.x == -600:
            self.x = self.x + 600'''
        return self.x
