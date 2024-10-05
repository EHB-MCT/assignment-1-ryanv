import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load('assets/images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 5
    def draw(self, screen):
        screen.blit(self.image, self.rect)
