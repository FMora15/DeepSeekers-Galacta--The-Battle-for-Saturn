import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.shoot_sound = pygame.mixer.Sound("assets/sounds/move.wav")

    def update(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.shoot_sound.play()
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.shoot_sound.play()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
            self.shoot_sound.play()
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed
            self.shoot_sound.play()
