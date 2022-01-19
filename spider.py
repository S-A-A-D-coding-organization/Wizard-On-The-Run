# import and initialize the pygame library
import pygame
import sys  # don't need these yet, but frequently do so it's in the template
import random

class Spider:
    def __init__(self, screen):
        self.screen = screen
        self.spi = pygame.image.load('img/background/spider.png')
        self.spider = pygame.transform.scale(self.spi, (160,80))
        self.x = 1280
    def spider_update(self):
        self.x = self.x - 2
        self.screen.blit(self.spider, (self.x, 450))
