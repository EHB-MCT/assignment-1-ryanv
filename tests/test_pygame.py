# Imports
import pygame

# Initialise pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Test")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()