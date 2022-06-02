import random
import control

import pygame

class Enemy(pygame.sprite.Sprite):

    it = 1
    ministep = 1

    way_ch_x = []
    way_ch_y = []
    way_ch_r = []

    way_1_x = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450]
    way_1_y = [600, 575, 545, 525, 525, 525, 525, 545, 575, 600]
    way_1_r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    way_2_x = [1250, 1230, 1160, 1030, 1030, 1080, 1060, 1080, 1090, 1095, 1090, 1050, 1050, 980, 970, 960, 940, 850, 900, 975, 1000, 1070, 1110, 1120, 1130, 1155, 1170, 1190, 1260]
    way_2_y = [580, 570, 590, 550, 520, 500, 480, 470, 460, 430, 340, 310, 290, 290, 280, 270, 275, 225, 165, 175, 165, 175, 160, 160, 165, 175, 120, 110, 110]
    way_2_r = [0, 0, 180, 36, 0, 0, 0, 67, 0, 0, 0, 0, 74, 0, 0, 0, 0, 270, 270, 0, 0, 0, 0, 0, 75, 0, 0, 0, 0]

    way_3_x = [1070, 900, 865, 860, 850, 855, 855, 855, 860, 840, 805, 810, 805, 805, 800, 775, 650]
    way_3_y = [405, 415, 400, 395, 340, 310, 250, 170, 150, 180, 150, 230, 290, 330, 390, 405, 385]
    way_3_r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, screen):
        """Инициализация"""

        super(Enemy, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('ref/squirrel.png')
        self.rect = self.image.get_rect()

        self.way_number = random.randint(1, 3)
        self.choose_way(self.way_number)
        self.speed = 5

        self.choose_image()


    def draw_enemy(self):
        """Отрисовка белки"""

        self.screen.blit(self.image, self.rect)

    def update(self, bg_color, screen, bg, aim, hero, enemies, stats):
        """Движение белки"""

        if self.it < len(self.way_ch_x):
            if self.ministep < (self.speed + 1):
                self.rect.centerx = self.way_ch_x[self.it - 1] + self.ministep * (self.way_ch_x[self.it] - self.way_ch_x[self.it - 1]) / self.speed
                self.rect.bottom = self.way_ch_y[self.it - 1] + self.ministep * (self.way_ch_y[self.it] - self.way_ch_y[self.it - 1]) / self.speed
            else:
                if self.way_ch_r[self.it] == 180:
                    self.image = pygame.transform.flip(self.image, flip_x = False, flip_y = True)
                self.image = pygame.transform.rotate(self.image, (self.way_ch_r[self.it]))
                self.it += 1
                self.ministep = 1
            self.ministep += 1
        else:
            self.kill()

    def choose_way(self, way_number):
        """Присвоение маршрута по номеру"""

        if way_number == 1:
            self.way_ch_x = self.way_1_x
            self.way_ch_y = self.way_1_y
            self.way_ch_r = self.way_1_r
        elif way_number == 2:
            self.way_ch_x = self.way_2_x
            self.way_ch_y = self.way_2_y
            self.way_ch_r = self.way_2_r
        elif way_number == 3:
            self.way_ch_x = self.way_3_x
            self.way_ch_y = self.way_3_y
            self.way_ch_r = self.way_3_r
        elif way_number == 4:
            self.way_ch_x = self.way_4_x
            self.way_ch_y = self.way_4_y
            self.way_ch_r = self.way_4_r
        elif way_number == 5:
            self.way_ch_x = self.way_5_x
            self.way_ch_y = self.way_5_y
            self.way_ch_r = self.way_5_r

    def choose_image(self):
        """Присвоение картинки"""

        if self.way_number == 1:
            self.image = pygame.image.load('ref/frontSquirrel.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.way_ch_x[0]
            self.rect.centery = self.way_ch_y[0]
            self.image = pygame.transform.rotate(self.image, self.way_ch_r[0])
        elif self.way_number == 2:
            self.image = pygame.image.load('ref/squirrel.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.way_ch_x[0]
            self.rect.centery = self.way_ch_y[0]
            self.image = pygame.transform.rotate(self.image, self.way_ch_r[0])
        elif self.way_number == 3:
            self.image = pygame.image.load('ref/smallSquirrel.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.way_ch_x[0]
            self.rect.centery = self.way_ch_y[0]
            self.image = pygame.transform.rotate(self.image, self.way_ch_r[0])

    def check_hit(self, pos, stats):
        """Проверка попадания"""

        if self.rect.collidepoint(pos):
            stats.change_stats()
            stats.image_stats()
            self.kill()

        # #def update(self, bg_color, screen, bg, aim, hero, enemies):
        #     # screen.blit(enemy.image, enemy.rect)
        #     for i in range(len(self.way_ch_x)):
        #         if i != 0:
        #             for z in range(self.speed + 1):
        #                 control.events(screen, aim, enemies)
        #                 self.rect.centerx = self.way_ch_x[i - 1] + z * (
        #                             self.way_ch_x[i] - self.way_ch_x[i - 1]) / self.speed
        #                 self.rect.centery = self.way_ch_y[i - 1] + z * (
        #                             self.way_ch_y[i] - self.way_ch_y[i - 1]) / self.speed
        #                 # enemy.image = pygame.transform.rotate(enemy.image, enemy.way_1_r[i])
        #                 # control.update(bg_color, screen, bg, aim, hero, enemies)
        #     self.kill()
