import pygame
import random

class Enemy:
    def __init__(self, screen_width, screen_height, player_size):
        # Load the enemy image and resize it
        self.image = pygame.image.load('assets/images/dynamics/enemy.png')
        self.image = pygame.transform.scale(self.image, player_size)  # Same size as player
        # Random initial position
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)

    # Draw the enemy on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)