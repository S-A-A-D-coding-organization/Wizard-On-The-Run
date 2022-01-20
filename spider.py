# import and initialize the pygame library
import pygame
import sys  # don't need these yet, but frequently do so it's in the template
import random

class Spider:
    def __init__(self, screen, start):
        self.screen = screen
        self.spi = pygame.image.load('img/background/spider.png')
        self.spider = pygame.transform.scale(self.spi, (160,80))
        self.x = start
    def spider_update(self):
        if self.x < -160:
            x = random.randint(852, 1280)
            print(x)
            self.x = x
        self.x = self.x - 2

        self.screen.blit(self.spider, (self.x, 450))
