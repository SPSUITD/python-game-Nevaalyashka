import pygame

class Hamster():
    def __init__(self,screen):
        """Инициализация"""

        self.shoot = False

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('ref/hamster.png')
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(bottomleft=(100,600))


    def output(self):
        """Отрисовка героя"""

        self.screen.blit(self.image, self.rect)

    def anim(self):
        """Анимция при стрельбе"""

        if self.shoot:
            self.image = pygame.image.load('ref/shootHamster.png')
            self.rect = self.image.get_rect()
            self.rect = self.image.get_rect(bottomleft=(100, 600))
            self.shoot = False
        else:
            self.image = pygame.image.load('ref/hamster.png')
            self.rect = self.image.get_rect()
            self.rect = self.image.get_rect(bottomleft=(100, 600))
            self.output()