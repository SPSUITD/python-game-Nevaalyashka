import time
from threading import Timer
import pygame
import sys

import control
from squirrels import Enemy
from stats import Stats

spawnenemies_count = 1
timer_count_spawn = 1
timer_period_spawn = 1
end_game = 30000

END_TIMER = pygame.USEREVENT + 1
HERO_ANIM_TIMER = pygame.USEREVENT + 2

def events(screen, aim, enemies, stats, hero):
    """Обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_enemy = Enemy(screen)
                enemies.add(new_enemy)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                hero.shoot = True
                hero.anim()
                pygame.time.set_timer(HERO_ANIM_TIMER, 280)
                if len(enemies) != 0:
                    for enemy in enemies:
                        enemy.check_hit(pygame.mouse.get_pos(), stats)
        elif event.type == END_TIMER:
            stats.timer -= 1
            stats.image_stats()
        elif event.type == HERO_ANIM_TIMER:
            hero.anim()
        else:
            aim.update_aim()



def update(bg_color,screen, bg, aim, hero, enemies, stats, deco):
    screen.fill(bg_color)
    screen.blit(bg, bg.get_rect())
    stats.output()

    if (pygame.time.get_ticks() > (control.timer_period_spawn * 2000) and (pygame.time.get_ticks()<end_game)):
        spawn_enemies(screen, enemies)
        control.timer_period_spawn += 1

    for enemy in enemies.sprites():
        enemy.draw_enemy()

    deco.output()
    aim.output()
    hero.output()

    pygame.display.flip()

def update_enemies(bg_color, screen, bg, aim, hero, enemies, stats):
    enemies.update(bg_color, screen, bg, aim, hero, enemies, stats)

def spawn_enemies(screen, enemies):
    for i in range(control.spawnenemies_count):
        new_enemy = Enemy(screen)
        enemies.add(new_enemy)
    if (pygame.time.get_ticks() > (control.timer_count_spawn * 6000)):
        control.spawnenemies_count += 1
        control.timer_count_spawn += 1
