import pygame
import random

# Initialize pygame
pygame.init()

# Create Window
screen = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
screen.fill(WHITE)

# Player
player_x = 50
player_y = 50
player_change = 0

# Enemy
enemy_x = []
enemy_y = []
enemy_change = []

# Score
score_number = 0
score_font = pygame.font.Font(None, 30)

# Game Over
game_over_font = pygame.font.Font(None, 60)

def game_over_text():
    game_over_text = game_over_font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (200, 250))

def show_score(x, y):
    score = font.render("Score : " + str(score_number), True, WHITE)
    screen.blit(score, (x,y))

def player(x, y):
    pass

def enemy():
    pass

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False