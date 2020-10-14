import pygame
import random

# Initialize pygame
pygame.init()
pygame.display.set_caption('LOL!')

# Create Window
screen = pygame.display.set_mode((800, 600))

# Color(s)
WHITE = (255, 255, 255)

# Player
player_x = 50
player_y = 50
player_change = 0

# Enemy
enemy_x = []
enemy_y = []
enemy_change = []
enemy_num = 5

# Score
score_number = 0
score_font = pygame.font.SysFont(None, 30)

text_x = 10
test_y = 10

def throw_snowball(x, y):
    global snowball_state
    snowball_state = "fire"
    screen.blit(snowballImg, (x + 16, y + 10))

def is_colliding(enemy_x, enemy_y, snowball_x, snowball_y):
    distance = math.sqrt(math.pow(enemy_x - snowball_x, 2) + (math.pow(enemy_y - snowball_y, 2)))
    if distance < 27:
        return True
    else:
        return False

# GAME OVER
game_over_font = pygame.font.SysFont(None, 60)

# Game over text
def game_over_text():
    game_over_text = game_over_font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (200, 250))

# Final Score
def show_score(text, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    score_text = font.render(text, True, color)
    screen.blit(score_text, (x, y))

# CHARACTERS
# Player
def player(x, y):
    screen.blit(img, (x, y))

# Enemy
def enemy():
    screen.blit(img[i], (x, y))

# GAMEPLAY
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update the player
    if keys[pygame.K_LEFT]:
        player_change = -5
    if keys[pygame.K_RIGHT]:
        player_chnage = 5
    if keys[pygame.K_UP]:
        player_change = -5
    if keys[pygame.K_DOWN]:
        player_change = 5
        
    # Fill screen with white
    screen.fill(WHITE)

    player(player_x, player_y)
    show_score(text_x, test_y)

    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()