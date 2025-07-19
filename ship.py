import pygame
from settings import Settings


class Ship:
    def __init__(self, screen):
        ship_image = pygame.image.load('./images/spaceship.png')
        # self.ship_image = pygame.transform.scale(ship_image, (40,200))
        self.ship_image = pygame.transform.scale_by(ship_image, .07)
        self.settings = Settings()
        self.screen = screen

        self.ship_rect = self.ship_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


        self.ship_rect.midbottom = self.screen_rect.midbottom
        self.ship_rect.y -= 10

        #auxiliary variables
        self.x = float(self.ship_rect.x)
        self.y = float(self.ship_rect.y)


    def update(self):
        if self.moving_right == True:
            self.x += self.settings.ship_speed
        if self.moving_left == True:
            self.x -= self.settings.ship_speed

        self.ship_rect.x = self.x

        if self.moving_up == True:
            self.y -= self.settings.ship_speed
        if self.moving_down == True:
            self.y += self.settings.ship_speed

        self.ship_rect.y = self.y
        
        
        self.blitme()
        
    def blitme(self):    
        self.screen.blit(self.ship_image, self.ship_rect)