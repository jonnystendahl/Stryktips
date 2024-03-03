import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple FPS Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the player
player_image = pygame.image.load('player.png')  # You need to provide a player image file
player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
player_speed = 5

# Set up the clock
clock = pygame.time.Clock()

# Function to handle player movement and collisions
def move_player(keys):
    global player_rect
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Boundary checking
    player_rect.x = max(0, min(WIDTH - player_rect.width, player_rect.x))
    player_rect.y = max(0, min(HEIGHT - player_rect.height, player_rect.y))

# Function to check collisions between player and window boundaries
def check_collision():
    if player_rect.left < 0:
        player_rect.left = 0
    elif player_rect.right > WIDTH:
        player_rect.right = WIDTH
    if player_rect.top < 0:
        player_rect.top = 0
    elif player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    move_player(keys)
    check_collision()

    # Fill the screen with background color
    screen.fill(WHITE)

    # Draw the player
    screen.blit(player_image, player_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
