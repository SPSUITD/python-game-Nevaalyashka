import pygame

class Decorations():

    def __init__(self,screen):
        "Инициализация"

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('ref/decorations.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = 600.731
        self.rect.centery = 403.536


    def output(self):
        """Отрисовка декораций"""

        self.screen.blit(self.image, self.rect)

