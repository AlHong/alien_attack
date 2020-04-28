import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("images/alien_ship.bmp")
        self.rect = self.image.get_rect()

        # start each new alien near the screen's top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien at its location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """returns true if alien is on edge of screen"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True

    def update(self):
        """move alien right/left"""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x
