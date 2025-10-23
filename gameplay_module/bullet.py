import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.shoot_sound = pygame.mixer.Sound("assets/sounds/shot.wav")

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
