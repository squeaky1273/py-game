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

# Background
background = pygame.image.load('background.png')

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# GREY = (246, 246, 246)

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
enemy_num = 10

for i in range(enemy_num):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

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

# Game Over
game_over_img = pygame.image.load('game_over.png')

################################################################################
# HELPER FUNCTIONS
################################################################################

# Player
def player(x, y):
    screen.blit(player_img, (x, y))

# Enemy
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

# TODO: Game Intro Screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_c]:
                    intro = False
                if keys[pygame.K_q]:
                    pygame.quit()
                    quit()
        
        screen.fill(WHITE)
        draw_text(text='Snowball Bash', color=BLACK, font_size=100, x=150, y=100)
        draw_text(text='The objective is to throw snowballs at the bullies.', color=BLACK, font_size=25, x=200, y=250)
        draw_text(text='The bullies will be trying to approach you. If they do, GAME OVER!', color=BLACK, font_size=25, x=125, y=300)
        draw_text(text='Get points by hitting them and keep them away.', color=BLACK, font_size=25, x=200, y=350)
        draw_text(text='Press C to play and Q to quit.', color=BLACK, font_size=25, x=275, y=450)
        pygame.display.update()

def game_over_text():
    screen.blit(game_over_img, (250, 175))
    draw_text(text='Press q to quit', color=BLACK, font_size=25, x=350, y=275)

# Player Throw Snowball
def player_throw_snowball(x, y):
    global snowball_state
    snowball_state = "fire"
    screen.blit(snowball_img, (x + 10, y + 4))

# # TODO: Enemy Throw Snowball 
# def enemy_throw_snowball(x, y):
#     global snowball_state
#     snowball_state = "fire"
#     screen.blit(snowball_img, (x + 10, y + 4))

# # TODO: Snowball hits the player
# def is_colliding_with_player(player_x, player_y, enemy_x, enemy_y):
#     distance = math.sqrt(math.pow(player_x - enemy_x, 2) + (math.pow(player_y - enemy_y, 2)))
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

# Pause Function
def paused():
    paused = True
    while paused:
        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_c]:
                    paused = False
                if keys[pygame.K_q]:
                    pygame.quit()
                    quit()
        
        screen.fill(WHITE)
        draw_text(text='Paused', color=BLACK, font_size=100, x=250, y=100)
        draw_text(text='Press C to continue or Q to quit', color=BLACK, font_size=25, x=250, y=250)
        pygame.display.update()

# Controls info page
def controls_info():
    controls_info = True
    while controls_info:
        for event in pygame.event.get():
            
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_c]:
                    controls = False
                if keys[pygame.K_q]:
                    pygame.quit()
                    quit()

        screen.fill(WHITE)
        draw_text(text='Controls', color=BLACK, font_size=100, x=250, y=75)
        draw_text(text='Press P to pause', color=BLACK, font_size=25, x=250, y=175)
        draw_text(text='Hold down the arrow keys to move', color=BLACK, font_size=25, x=250, y=225)
        draw_text(text='Press spacebar to shoot enemies', color=BLACK, font_size=25, x=250, y=250)
        draw_text(text='Press C to continue the game', color=BLACK, font_size=25, x=250, y=275)
        draw_text(text='Press Q to quit the game', color=BLACK, font_size=25, x=250, y=300)
        pygame.display.update()
        
################################################################################
# GAMEPLAY
################################################################################

# Game Loop
running = True
while running:
    # game_intro()

    # Fill screen with grey
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update the player
    if keys[pygame.K_LEFT]:
        player_x -= 4
    if keys[pygame.K_RIGHT]:
        player_x += 4
    # if keys[pygame.K_UP]:
    #     player_y -= 5
    # if keys[pygame.K_DOWN]:
    #     player_y += 5
    if keys[pygame.K_SPACE]:
        if snowball_state is "ready":
            # Get the current x cordinate of the spaceship
            snowball_x = player_x
            player_throw_snowball(snowball_x, snowball_y)

    if keys[pygame.K_p]:
        paused()
    
    # Get to controls screen
    if keys[pygame.K_i]:
        controls_info()

    # Quit Game
    if keys[pygame.K_q]:
        pygame.quit()
        quit()

    # Enemy Movement
    for i in range(enemy_num):
    
        # Game Over
        if enemy_y[i] > player_y:
            for j in range(enemy_num):
                enemy_y[j] = 7000
            game_over_text()
            if keys[pygame.K_q]:
                pygame.quit()
                quit()
            break

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
        # if is_colliding_with_player(player_x, player_y, enemy_x, enemy_y):
        #     player_x = random.randint(0, 736)
        #     player_y = random.randint(50, 250)

        #     # # Draw the Game Over text
        #     game_over_text()

    if snowball_y <= 0:
        snowball_y = 480
        snowball_state = "ready"

    if snowball_state is "fire":
        player_throw_snowball(snowball_x, snowball_y)
        snowball_y -= snowball_y_change

    # Draw the points
    draw_text(text=f'Points: {points}', color=BLACK, font_size=24, x=20, y=20)

    # Info
    draw_text(text='Press I for control info', color=BLACK, font_size=24, x=600, y=20)

    # Run player function
    player(player_x, player_y)

    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()