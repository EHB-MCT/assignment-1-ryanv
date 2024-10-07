# main.py

# Imports
import pygame
import sys
from pygame.locals import *
import random
import time
from datetime import datetime
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from game import run_game

# Initialise Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer game")
clock = pygame.time.Clock()


# Game loop
def main():
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()