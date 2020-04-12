import random
import pygame
from Settings import SCREEN_HEIGHT, SCREEN_WIDTH, GAME_MODE
from Supporting_Functions import determine_enemy_speed_range

class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        enemy_lower_speed_range, enemy_upper_speed_range = determine_enemy_speed_range(SCREEN_WIDTH)
        self.speed = random.uniform(enemy_lower_speed_range, enemy_upper_speed_range)
        if GAME_MODE == 'easy': self.speed = self.speed * 1
        if GAME_MODE == 'medium': self.speed = self.speed * 2
        if GAME_MODE == 'hard': self.speed = self.speed * 3

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
