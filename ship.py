import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load("images/player_ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # ship movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx