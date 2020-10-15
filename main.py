import pygame
import random
import math

# Initialize Pygame
pygame.init()
pygame.display.set_caption('LOL!')

################################################################################
# VARIABLES
################################################################################

# Constants
# Set up the drawing window
screen = pygame.display.set_mode((800, 600))

# CHARACTER_WIDTH = 40
# CHARACTER_HEIGHT = 40

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player Variables
player_img = pygame.image.load('player.png') # make sure to create diiferent sprite
player_x = 370
player_y = 480

# # Enemy Variables
# enemy_img = []
# enemy_x = []
# enemy_y = []
# enemy_num = 5

# for i in range(enemy_num):
#     enemy_x.append(random.randint(0, 736))
#     enemy_y.append(random.randint(50, 150))
#     enemy_x_change.append(4)
#     enemy_y_change.append(40)

# # Snowball

# # Ready - You can't see the snowball on the screen
# # Fire - The snowball is currently moving

# snowball_x = 0
# snowball_y = 480
# snowball_x_change = 0
# snowball_y_change = 10
# snowball_state = "ready"

# # Target Variables
# target_x = 10
# target_y = 10

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

# def is_colliding(enemy_x, enemy_y, snowball_x, snowball_y):
#     distance = math.sqrt(math.pow(enemy_x - snowball_x, 2) + (math.pow(enemy_y - snowball_y, 2)))
#     if distance < 27:
#         return True
#     else:
#         return False

def draw_text(text, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# # Game over text
# def game_over_text():
#     game_over_text = game_over_font.render("Game Over", True, WHITE)
#     screen.blit(game_over_text, (200, 250))


################################################################################
# GAMEPLAY
################################################################################

# Game Loop
running = True
while running:
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

    # TODO: Update the enemy's y position based on its velocity

    # TODO: If enemy went off the screen, reset it

    # # If player collides with target, reset it & increment points
    # if is_colliding(player_x, player_y, target_x, target_y, CHARACTER_WIDTH, CHARACTER_HEIGHT):
    #     points += 1
    #     target_y = 0
    #     target_x = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)

    # TODO: If player collides with enemy, flash game over screen

    # Fill screen with white
    screen.fill(WHITE)

    # TODO: Draw the enemy

    # Draw the points
    draw_text(text=f'Points: {points}', color=BLACK, font_size=24, x=20, y=20)

    # Run player function
    player(player_x, player_y)

    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()