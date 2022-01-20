# import and initialize the pygame library
import pygame
import sys  # don't need these yet, but frequently do so it's in the template
import random
import DataBase as db


class Spider:
    def __init__(self, screen):
        self.screen = screen
        self.spider = pygame.transform.scale(pygame.image.load('img/background/spider.png'), (160, 80))
        self.spider_sound = pygame.mixer.Sound('sounds/spider.mp3')
    def spider_update(self):
        if db.call('spider_2') - 100 < db.call('spider_1'):
            db.save('spider_2',
                    random.randint(852, 1280) if db.call('spider_2') < -160 else db.call('spider_2') - 5)

        if db.call('spider_1') - 100 < db.call('spider_2'):
            db.save('spider_1',
                    random.randint(852, 1280) if db.call('spider_1') < -160 else db.call('spider_1') - 5)

        if 705 >= db.call('spider_1') >= 700:
            self.spider_sound.play()

        if 705 >= db.call('spider_1') >= 700:
            self.spider_sound.play()

        self.screen.blit(self.spider, (db.call('spider_1'), 450))
        self.screen.blit(self.spider, (db.call('spider_2'), 450))
