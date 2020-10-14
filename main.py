import pygame
import random

# Initialize pygame
pygame.init()

# Create Window
screen = pygame.display.set_mode((800, 600))

# Player
player_x = 50
player_y = 50
player_change = 0

# Enemy
enemy_x = []
enemy_y = []
enemy_change = []

# Score
score = 0

# Game Over


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False