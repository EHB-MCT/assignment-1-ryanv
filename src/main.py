# main.py

# Imports
import pygame
import sys
from pygame.locals import *
import random
import time
from datetime import datetime
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from game import Game  # Import the Game class

# Initialise Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()

# Game loop
def main():
    # Instantiate the Game class
    game = Game(screen)

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            # Stop game loop when quitting pygame
            if event.type == pygame.QUIT:
                running = False
            # Handle player movement events
            game.player.handle_event(event)

        # Update the game state
        game.update()

        # Draw the game elements
        game.draw()

        # Refresh the display
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
