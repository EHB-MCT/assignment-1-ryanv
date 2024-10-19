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

        # Movement speed (constant speed)
        self.speed_x = random.choice([-3, 3])  # Random speed in x direction
        self.speed_y = random.choice([-3, 3])  # Random speed in y direction

        self.screen_width = screen_width
        self.screen_height = screen_height

    # Update the position of the enemy
    def update(self):
        # Move the enemy
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    # Draw the enemy on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)