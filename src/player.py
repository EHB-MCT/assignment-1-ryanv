import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load('assets/images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 5

        # Movement attributes (boolean) declaration
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    # Movement controls event listeners
    def handle_event(self, event):
        # Set movement attributes to True when key pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.moving_left = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.moving_right = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.moving_up = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.moving_down = True

        # Set movement attributes back to False when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.moving_left = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.moving_right = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.moving_up = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.moving_down = False

    # Update player position if any movement attribute is set to True
    def update(self):
        if self.moving_left:
            self.rect.x -= self.speed
        if self.moving_right:
            self.rect.x += self.speed
        if self.moving_up:
            self.rect.y -= self.speed
        if self.moving_down:
            self.rect.y += self.speed

    # Draw player on screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
