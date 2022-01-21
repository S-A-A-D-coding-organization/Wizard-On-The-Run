"""
This script generates the code for the graphics.
"""

# imports
import pygame
import button
import Character
import DataBase as db
import time
import spider

"""
programed by: crypto-a(Ali Rahbar)
Date: January 17, 18
"""


class Game:  # when executed the games gui start working

    def __init__(self):  # loads and prepares all the data for the class

        pygame.init()
        res = (700, 550)
        self.screen = pygame.display.set_mode(res)
        self.logo = pygame.image.load('img/logo/logo.png')
        self.bg = pygame.image.load('img/background/ground.jpeg')
        pygame.display.set_caption("Wizard on The Run")

    def path_generator(self):  # it generates the path with the info from spider_generator and returns it to the display
        db.save('background', db.call('background') - 2)
        db.save('total_score', (db.call('background') * -1)//100)

    def play_music(self):
        bg_sound = pygame.mixer.Sound('sounds/background.mp3')  # play music
        bg_sound.play()

    def start_page(self):  # this shows the start page before starting the game
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(0.5)

        self.screen.blit(self.logo, (200, 180))
        pygame.display.flip()

        time.sleep(2)

        self.play_music()
        play_button = button.Button("Play", 300, 250, 50, 100, self.screen)

        while db.call('running'):  # runs the first scene
            pos = (play_button.is_over(pygame.mouse.get_pos()) == True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # the quit settings
                    db.save('running', False)
                elif event.type == pygame.MOUSEBUTTONDOWN and pos:  # if button is clicked
                    db.save('running', False)
                    break
            self.screen.blit(self.bg, (0, 0))

            play_button.draw((225, 255, 0)) if pos else play_button.draw((225, 255, 200))

            pygame.display.update()

        db.save('running', True)
        self.screen_update()

    def screen_update(self):  # refreshes the display every time
        three = button.Button('3', 340, 265, 20, 20, self.screen)
        two = button.Button('2', 340, 265, 20, 20, self.screen)
        one = button.Button('1', 340, 265, 20, 20, self.screen)
        self.screen.blit(self.bg, (0, 0))
        three.draw((0, 230, 0))
        pygame.display.update()
        time.sleep(1)

        self.screen.blit(self.bg, (0, 0))
        two.draw((0, 230, 0))
        pygame.display.update()
        time.sleep(1)

        self.screen.blit(self.bg, (0, 0))
        one.draw((0, 230, 0))
        pygame.display.update()
        time.sleep(1)

        db.game_prep()
        character = Character.Persona(self.screen, 700, 550)
        spiders = spider.Spider(self.screen)

        # screen loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # the quit settings
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        character.jump()

            self.path_generator()
            self.screen.blit(self.bg, (db.call('background') + db.call('ground_1'), 0))
            self.screen.blit(self.bg, (db.call('background') + db.call('ground_2'), 0))
            self.screen.blit(self.bg, (db.call('background') + db.call('ground_3'), 0))

            spiders.spider_update()
            character.movment()

            self.screen.blit(pygame.font.SysFont('comicsans', 20).render('score: ' + str(db.call('total_score')), True, (0, 0, 0)),
                             (600, 10))

            pygame.display.flip()

            # loop conditions
            db.save('ground_1', db.call('ground_1') + 3840) if (db.call('background') + db.call('ground_1') == -1280) else None
            db.save('ground_2', db.call('ground_2') + 3840) if (db.call('background') + db.call('ground_2') == -1280) else None
            db.save('ground_3', db.call('ground_3') + 3840) if (db.call('background') + db.call('ground_3') == -1280) else None

            if self.collision(db.call('spider_1'), db.call('pos')) or self.collision(db.call('spider_1'),
                                                                                  db.call('pos')):  # Delsin Gibbs
                break
            time.sleep(0.005)

        self.end_screen()

    def collision(self, spiderx, charectorY):  # checks for coalitions
        # checking for collision(HARD CODED)
        if spiderx >= -30 and spiderx <= 180 and charectorY >= 370 and charectorY <= 450:  # checking to see if the wizard hits the spider
            # The first part of his if statement is checking if the back of the spider is touching the back of the
            # wizard. It is -60 because the back of the wizard is at 100 and the length of the spider is 160 the
            # second part of this if statement is checking if the front of the wizard is touching the front of the
            # spider the last two parts are checking if the wizard is jumping over the spider or landing in the spider
            return True  # if the if statement above is true return true

        return False  # if not return false

    def end_screen(self):
        running = True
        redo = 0
        end_button = button.Button('Quit', 280, 250, 70, 70, self.screen)
        restart_button = button.Button('Re-try', 360, 250, 70, 70, self.screen)

        while running:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # the quit settings
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and end_button.is_over(pos):
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and restart_button.is_over(pos):
                    redo = 1
                    running = False

            if end_button.is_over(pos):
                end_button.draw((255, 200, 20))
            else:
                end_button.draw((255, 0, 0))

            if restart_button.is_over(pos):
                restart_button.draw((255, 200, 20))
            else:
                restart_button.draw((0, 0, 240))

            pygame.display.flip()

        if redo == 1:
            self.screen_update()
        else:
            pygame.quit()
