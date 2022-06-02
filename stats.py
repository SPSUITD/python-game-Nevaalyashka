import pygame

class Stats():
    "Отслеживание статистики и вывод"

    def __init__(self, screen):
        "Инициализация"


        self.count_enemies = 0
        self.score = 0
        self.highscore = 0
        self.timer = 30

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 52)
        self.image_stats()

        END_TIMER = pygame.USEREVENT + 1
        pygame.time.set_timer(END_TIMER, 1000)

    def change_stats(self):
        """Статистика, изменяющаяся во время игры"""

        if pygame.time.get_ticks() < 6000:
            self.score += 25
        elif 6000 <= pygame.time.get_ticks() < 12000:
            self.score += 50
        elif 12000 <= pygame.time.get_ticks() < 18000:
            self.score += 75
        elif 18000 <= pygame.time.get_ticks() < 24000:
            self.score += 100
        elif 24000 <= pygame.time.get_ticks() <= 30000:
            self.score += 125
        if self.score > self.highscore:
            self.highscore = self.score

    def image_stats(self):
        """Преобразование статистики в графическое изображение"""

        self.score_img = self.font.render("Score: " + str(self.score), True, self.text_color, None)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 40
        self.score_rect.top = 20

        self.timer_img = self.font.render(str(self.timer), True, self.text_color, None)
        self.timer_rect = self.timer_img.get_rect()
        self.timer_rect.centerx = self.screen_rect.centerx
        self.timer_rect.top = 20

        self.highscore_img = self.font.render("Highscore: " + str(self.highscore), True, self.text_color, None)
        self.highscore_rect = self.highscore_img.get_rect()
        self.highscore_rect.right = self.screen_rect.right - 40
        self.highscore_rect.top = 20

    def image_new_highscore(self):
        """Оповещение о новом рекорде"""

        self.highscore_msg_img = self.font.render("New Highscore: " + str(self.highscore), True, self.text_color, None)
        self.highscore_msg_rect = self.highscore_msg_img.get_rect()
        self.highscore_msg_rect.centerx = self.screen_rect.centerx
        self.highscore_msg_rect.top = 200

        self.screen.blit(self.highscore_msg_img, self.highscore_msg_rect)

    def output(self):
        """Отрисовка статистики"""

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.highscore_img, self.highscore_rect)
        self.screen.blit(self.timer_img, self.timer_rect)