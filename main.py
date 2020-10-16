import pygame
import random
import math

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Snowball Bash!')

################################################################################
# VARIABLES
################################################################################

# Constants
# Set up the drawing window
screen = pygame.display.set_mode((800, 600))

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

# Player Variables
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480

# Enemy Variables
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_num = 8

for i in range(enemy_num):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(1)
    enemy_y_change.append(1)

# Snowball Variables

# Ready - You can't see the snowball on the screen
# Fire - The snowball is currently moving

snowball_img = pygame.image.load('snowball.png')
snowball_x = 0
snowball_y = 480
snowball_x_change = 0
snowball_y_change = 10
snowball_state = "ready"

# Other variables
points = 0

################################################################################
# HELPER FUNCTIONS
################################################################################

# Player
def player(x, y):
    screen.blit(player_img, (x, y))

# Enemy
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

# Player Throw Snowball
def player_throw_snowball(x, y):
    global snowball_state
    snowball_state = "fire"
    screen.blit(snowball_img, (x + 10, y + 4))

## TODO: Enemy Throw Snowball 
# def enemy_throw_snowball(x, y):
#     global snowball_state
#     snowball_state = "fire"
#     screen.blit(snowball_img, (x + 10, y + 4))

## TODO: Snowball hits the player
# def is_colliding_with_player(player_x, player_y, snowball_x, snowball_y):
#     distance = math.sqrt(math.pow(player_x - snowball_x, 2) + (math.pow(player_y - snowball_y, 2)))
#     if distance < 27:
#         return True
#     else:
#         return False

# Snowball hits Enemy
def is_colliding_with_enemy(enemy_x, enemy_y, snowball_x, snowball_y):
    distance = math.sqrt(math.pow(enemy_x - snowball_x, 2) + (math.pow(enemy_y - snowball_y, 2)))
    if distance < 27:
        return True
    else:
        return False

def draw_text(text, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


################################################################################
# GAMEPLAY
################################################################################

# Game Loop
running = True
while running:

    # Fill screen with grey
    screen.fill(GREY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update the player
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5
    if keys[pygame.K_SPACE]:
        if snowball_state is "ready":
            # Get the current x cordinate of the spaceship
            snowball_x = player_x
            player_throw_snowball(snowball_x, snowball_y)

    # Enemy Movement
    for i in range(enemy_num):

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 2
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -2
            enemy_y[i] += enemy_y_change[i]

        # Run enemy function
        enemy(enemy_x[i], enemy_y[i], i)

        # If snowball hits enemy add 1 to point score
        if is_colliding_with_enemy(enemy_x[i], enemy_y[i], snowball_x, snowball_y):
            points += 1
            snowball_y = 480
            snowball_state = "ready"
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)

        # # TODO: If snowball hits player, flash game over screen
        # if is_colliding_with_player(player_x[i], player_y[i], snowball_x, snowball_y):
        #     snowball_y = 480
        #     snowball_state = "ready"
        #     player_x[i] = random.randint(0, 736)
        #     player_y[i] = random.randint(50, 150)

        #     # # Draw the Game Over text
        #     # draw_text(text='GAME OVER', color=BLACK, font_size=50, x=300, y=400)

    if snowball_y <= 0:
        snowball_y = 480
        snowball_state = "ready"

    if snowball_state is "fire":
        player_throw_snowball(snowball_x, snowball_y)
        snowball_y -= snowball_y_change

    # Draw the points
    draw_text(text=f'Points: {points}', color=BLACK, font_size=24, x=20, y=20)

    # Run player function
    player(player_x, player_y)

    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()