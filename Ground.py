"""
This scripts processes and generates the path for the Dino
"""

# imports
import pygame
import DataBase as db
import threading
import time
import spider

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
    def path_generator(self):  # it generates the path with the info from spider_generator and returns it to the display
        self.x = self.x - 2
        db.save('total_score', (self.x * -1)//100)
        return self.x
