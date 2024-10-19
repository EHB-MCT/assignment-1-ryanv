from player import Player
from enemy import Enemy
import pygame


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()

        # Create a list of enemies
        self.enemies = []
        self.create_enemies(3) #number of enemies

        # Flag for game over or collision
        self.game_over = False

    def create_enemies(self, number_of_enemies):
        # Get player size from player image rect
        player_size = (self.player.rect.width, self.player.rect.height)

        # Add enemies to the list
        for _ in range(number_of_enemies):
            enemy = Enemy(self.screen.get_width(), self.screen.get_height(), player_size)
            self.enemies.append(enemy)

    def update(self):
        # Update player position
        self.player.update()

        # Update enemy positions
        for enemy in self.enemies:
            enemy.update()

    def draw(self):
        # Fill screen with a black background
        self.screen.fill((0, 0, 0))

        # Draw player
        self.player.draw(self.screen)

        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(self.screen)
