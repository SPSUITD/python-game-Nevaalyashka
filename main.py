import time
import sys
import pygame
import control
from hero import Hamster
from aim import Aim
from decorations import Decorations
from stats import Stats
from pygame.sprite import Group

def run():
    pygame.init()

    screen = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption("Хомяк против белок")

    bg = pygame.image.load('ref/level 1.png')
    bg_color = (0, 0, 0)

    eg = pygame.image.load('ref/endgame.png')
    eg_rect = eg.get_rect()
    eg_rect.centerx = screen.get_rect().centerx
    eg_rect.centery = screen.get_rect().centery

    pygame.mouse.set_visible(False)

    sound = pygame.mixer.Sound('ref/Onion Capers.mp3')
    sound.play()

    statistics = open('Highscore.txt', 'r+')

    hero = Hamster(screen)
    aim = Aim(screen)
    enemies = Group()
    stats = Stats(screen)
    deco = Decorations(screen)

    stats.highscore = int(statistics.read())

    while True:

        control.events(screen, aim, enemies, stats, hero)

        control.update_enemies(bg_color, screen, bg, aim, hero, enemies, stats)
        control.update(bg_color, screen, bg, aim, hero, enemies, stats, deco)

        if pygame.time.get_ticks() > control.end_game:
            screen.blit(eg, eg_rect)
            if stats.score >= stats.highscore and stats.score != 0:
                stats.image_new_highscore()
                statistics.truncate(0)
                statistics.seek(0)
                statistics.write(str(stats.score))
            pygame.display.flip()
            time.sleep(5)
            statistics.close()
            sys.exit()


run()