import pygame

class Aim():
    def __init__(self, screen):
        """Инициализация"""

        self.screen = screen
        self.image = pygame.image.load('ref/aim.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect(bottomleft=(100, 600))

    def output(self):
        """Отрисовка прицела"""

        self.screen.blit(self.image, self.rect)

    def update_aim(self):
        """Следование за курсором"""

        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            self.rect.centerx = pos[0] - 2
            self.rect.centery = pos[1] - 1

