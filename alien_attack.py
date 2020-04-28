import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from stats import Stats
from button import Button
from scoreboard import ScoreBoard

def start_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )

    pygame.display.set_caption("Alien Attack")

    play_button = Button(settings, screen, "Play")

    stats = Stats(settings)
    sb = ScoreBoard(settings, screen, stats)

    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            update_elements(settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)


def update_elements(settings, screen, stats, sb, ship, aliens, bullets):
    ship.update()
    gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
    gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)


start_game()
