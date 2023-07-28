import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Darshan Gamer")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.SysFont(None, 25)

# Set up the images
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')
missile_img = pygame.image.load('missile.png')

# Set up the sounds
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)
missile_sound = pygame.mixer.Sound('missile_sound.wav')
explosion_sound = pygame.mixer.Sound('explosion_sound.wav')

# Set up the player
player_size = 50
player_x = (display_width - player_size) / 2
player_y = display_height - player_size
player_x_change = 0

# Set up the enemies
enemy_size = 50
enemy_x = random.randint(0, display_width - enemy_size)
enemy_y = 0
enemy_speed = 5

# Set up the missiles
missile_speed = 7
missile_state = "ready"

# Set up the score
score = 0


# Function to display the player
def player(x, y):
    game_display.blit(player_img, (x, y))


# Function to display the enemy
def enemy(x, y):
    game_display.blit(enemy_img, (x, y))


# Function to fire the missile
def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    game_display.blit(missile_img, (x + 20, y - 20))
    missile_sound.play()


# Function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    game_display.blit(score_text, (10, 10))


# Function to display the message on the screen
def message_display(text):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width / 2, display_height / 2)
    game_display.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)


# Function to check if the player has been hit
def check_hit(player_x, player_y, enemy_x, enemy_y):
    if player_x + player_size > enemy_x and player_x < enemy_x + enemy_size:
        if player_y < enemy_y + enemy_size:
            explosion_sound.play()
            return True
    return False


# Game loop
game_exit = False
while not game_exit:

    # Event loop
    for event in pygame.event.get():
        if event.type ==:
    