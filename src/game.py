from player import Player
from enemy import Enemy
import random


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()

        # Create a list of enemies
        self.enemies = []
        self.create_enemies(3) #number of enemies

    def create_enemies(self, number_of_enemies):
        player_size = (self.player.rect.width, self.player.rect.height)

        for _ in range(number_of_enemies):
            enemy = Enemy(self.screen.get_width(), self.screen.get_height(), player_size)
            self.enemies.append(enemy)

    def update(self):
        self.player.update()

        for enemy in self.enemies:
            enemy.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)        for enemy in self.enemies:
            enemy.draw(self.screen)
