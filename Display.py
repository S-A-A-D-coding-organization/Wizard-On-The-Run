"""
This script generates the code for the graphics.
"""

# imports
import pygame
import button
import Character
import Ground
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
        self.logo = pygame.image.load('img/logo/logo.png')
        self.bg = pygame.image.load('img/background/ground.jpeg')
        self.spider = 0
        self.screen = pygame.display.set_mode(res)
        self.ground = Ground.Path(self.screen, self.bg, self.spider)
        pygame.display.set_caption("Wizard on The Run")

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
        self.screen.blit(self.bg, (0, 0))
        pygame.display.update()
        time.sleep(3)

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

            pos = self.ground.path_generator()
            self.screen.blit(self.bg, (pos + db.call('ground_1'), 0))
            self.screen.blit(self.bg, (pos + db.call('ground_2'), 0))
            self.screen.blit(self.bg, (pos + db.call('ground_3'), 0))

            spiders.spider_update()
            character.movment()

            self.screen.blit(pygame.font.SysFont('comicsans', 20).render(str(db.call('total_score')), True, (0, 0, 0)),
                             (630, 10))

            pygame.display.flip()

            # loop conditions
            db.save('ground_1', db.call('ground_1') + 3840) if (pos + db.call('ground_1') == -1280) else None
            db.save('ground_2', db.call('ground_2') + 3840) if (pos + db.call('ground_2') == -1280) else None
            db.save('ground_3', db.call('ground_3') + 3840) if (pos + db.call('ground_3') == -1280) else None

            if self.collision(db.call('spider_1'), db.call('pos')) or self.collision(db.call('spider_1'),
                                                                                  db.call('pos')):  # Delsin Gibbs
                break
            time.sleep(0.005)

        self.end_screen()

    def collision(self, spiderx, charectorY):  # checks for coalitions
        # checking for collision(HARD CODED)
        if spiderx >= -60 and spiderx <= 210 and charectorY >= 370 and charectorY <= 450:  # checking to see if the wizard hits the spider
            # The first part of his if staement is checking if the back of the spider is tounching the back of the wizard. It is -60 becuase the back of the wizard is at 100 and the length of the spider is 160
            # the second part of this if statement is checking if the front of the wizard is touching the front of the spider
            # the last two parts are checking if the wizard is jumping over the spider or landing in the spider
            return True  # if the if statement above is true return true

        return False  # if not return false

    def end_screen(self):
        pygame.quit()
