from player import Player
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()

    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)