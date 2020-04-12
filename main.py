import random
import time
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT,
    K_ESCAPE)

from Colors import Colors
from Enemy import Enemy
from Player import Player
from Settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BACKGROUND_COLOR, GAME_MODE
from Supporting_Functions import round_down

pygame.init()
running = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# CUSTOM EVENT FOR ADDING ENEMIES
ADD_ENEMY = pygame.USEREVENT + 1
if GAME_MODE == 'easy': pygame.time.set_timer(ADD_ENEMY, 150)
if GAME_MODE == 'medium': pygame.time.set_timer(ADD_ENEMY, 110)
if GAME_MODE == 'hard': pygame.time.set_timer(ADD_ENEMY, 75)

# CUSTOM EVENT FOR UPDATING TIMER
UPDATE_TIMER = pygame.USEREVENT + 2
pygame.time.set_timer(UPDATE_TIMER, 100)

# Initiate player and enemies
player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Timer for game
start_time = time.time()
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)
current_time_string = '0'

while running:
    # Check events for any inputs and stuff
    for event in pygame.event.get():
        # Quit Event
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        # Add Enemy Event. Happens every .15 seconds
        elif event.type == ADD_ENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        # Update timer event. Happens every 100ms
        elif event.type == UPDATE_TIMER:
            current_time = time.time() - start_time
            # Round to 3 digits
            current_time_string = str(round_down(current_time, 1))
            # Render the timer in the top left corner

    # Text for timer
    text = font.render(current_time_string, True, Colors.green, SCREEN_BACKGROUND_COLOR)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH - (SCREEN_WIDTH * .95), SCREEN_HEIGHT - (SCREEN_HEIGHT * .95))

    # Capture player movement and move them
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Move the enemies across the screen. May update with UI eventually
    enemies.update()

    screen.fill(SCREEN_BACKGROUND_COLOR)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    # Blit the timer
    screen.blit(text, textRect)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
