# Import necessary modules
import pygame                     # Pygame for game development
from sys import exit              # exit() for safely quitting the game
from random import randint        # randint() for random obstacle spawning

# Function to display the score (based on elapsed time)
def display_score():
    # Calculate elapsed time in seconds since game started
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    # Render the elapsed time as text
    score_surface = test_font.render(f'{current_time}', False, "#000000")
    # Position the score at top center
    score_rect = score_surface.get_rect(center=(390, 50))
    # Draw score on screen
    screen.blit(score_surface, score_rect)
    return current_time

# Function to calculate dynamic game speed
def get_speed(current_time):
    """
    Base speed = 4 pixels/frame.
    Increases by 0.1 every 5 seconds.
    Capped at max speed of 12.
    """
    speed = 4 + (current_time // 5) * 0.1
    return min(speed, 12)

# Function to move obstacles
def obstacle_movement(obstacle_list, speed):
    """
    Moves obstacles left by `speed` each frame.
    Removes obstacles once they leave the screen.
    """
    new_list = []
    for surface, rect in obstacle_list:
        rect.x -= speed              # Move obstacle left
        screen.blit(surface, rect)   # Draw obstacle
        if rect.x > -50:             # Keep only if still visible
            new_list.append((surface, rect))
    return new_list

# Function to check collisions
def collisions(player, obstacles):
    """
    Checks if player collides with any obstacle.
    Returns False if collision happens (game over),
    True otherwise.
    """
    if obstacles:
        for surface, obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):  # Collision check
                return False
    return True

# ------------------ GAME INITIALIZATION ------------------

pygame.init()  # Initialize pygame
screen = pygame.display.set_mode((800, 400))     # Create game window
pygame.display.set_caption('Retro Runner')       # Set window title
icon = pygame.image.load('pics/player.png')      # Load window icon
pygame.display.set_icon(icon)                    # Apply icon
clock = pygame.time.Clock()                      # Clock to control FPS
test_font = pygame.font.Font('pics/pixel.ttf', 30)  # Main font
replay_font = pygame.font.Font('pics/pixel.ttf', 20) # Replay font
game_active = False                              # Tracks game state
start_time = 0                                   # Start time reference
score = 0                                        # Player score

# ------------------ BACKGROUND IMAGES ------------------

# Load background (sky) and scale to window size
sky_surface = pygame.image.load('pics/bg1.png').convert()
sky_surface = pygame.transform.scale(sky_surface, (800, 400))

# Load ground and scale
ground_surface = pygame.image.load('pics/ground1.jpg').convert()
ground_surface = pygame.transform.scale(ground_surface, (800, 100))
ground_x = 0   # Ground x-position for scrolling

# Initialize sky scrolling
sky_x = 0

# ------------------ OBSTACLE IMAGES ------------------

# Doggy obstacle
doggy_surface = pygame.image.load('pics/doggy.png').convert_alpha()
doggy_surface = pygame.transform.scale(doggy_surface, (50, 50))

# Bird obstacle
bird_surface = pygame.image.load('pics/bird.png').convert_alpha()
bird_surface = pygame.transform.scale(bird_surface, (70, 70))

# List to store active obstacles
obstacle_rect_list = []

# ------------------ PLAYER ------------------

# Load and scale player
player_surface = pygame.image.load('pics/player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (60, 105))
# Set initial player position
player_rect = player_surface.get_rect(midbottom=(100, 340))

# Smaller rectangle for more accurate collisions
player_collision_rect = player_rect.inflate(-30, -20)

# Gravity variable (controls jump and fall)
player_gravity = 0

# ------------------ GAME OVER SCREEN ------------------

# Load character image for game over display
character = pygame.image.load('pics/player.png').convert_alpha()
character = pygame.transform.scale(character, (100, 165))
# Game title text
Name = test_font.render('RETRO RUNNER', False, "#000000")
# Replay instruction text
Replay = replay_font.render("press 'space' to play", False, "#000000")

# ------------------ OBSTACLE SPAWNING ------------------

# Custom timer event to spawn obstacles every 1300ms
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1300)

# ------------------ MAIN GAME LOOP ------------------

while True:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Quit button
            pygame.quit()
            exit()

        if game_active:
            # Jump on mouse click if player is on ground
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 320:
                    player_gravity = -21

            # Jump on SPACE if player is on ground
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 320:
                    player_gravity = -21

            # Spawn obstacle when timer event fires
            if event.type == obstacle_timer:
                if randint(0, 2):  # Randomly spawn doggy
                    obstacle_rect_list.append(
                        (doggy_surface, doggy_surface.get_rect(midbottom=(randint(900, 1100), 315)))
                    )
                else:  # Otherwise spawn bird
                    obstacle_rect_list.append(
                        (bird_surface, bird_surface.get_rect(midbottom=(randint(900, 1100), 200)))
                    )

        else:
            # Start game when SPACE pressed on game over screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)  # Reset start time
                obstacle_rect_list.clear()  # Clear obstacles
                player_rect.midbottom = (100, 340)  # Reset player position
                player_gravity = 0  # Reset gravity

    # ------------------ GAME RUNNING ------------------
    if game_active:
        # Get current speed based on elapsed time/score
        speed = get_speed(score)

        # Scroll sky (parallax effect, slower than ground)
        sky_x -= speed * 0.5
        if sky_x <= -sky_surface.get_width():  # Reset once fully off screen
            sky_x = 0

        # Draw two skies side by side to create seamless loop
        screen.blit(sky_surface, (sky_x, 0))
        screen.blit(sky_surface, (sky_x + sky_surface.get_width(), 0))

        # Scroll ground at current speed
        ground_x -= speed
        if ground_x <= -ground_surface.get_width():  # Reset once off screen
            ground_x = 0

        # Draw two grounds side by side
        screen.blit(ground_surface, (ground_x, 300))
        screen.blit(ground_surface, (ground_x + ground_surface.get_width(), 300))

        # Display score (time survived)
        score = display_score()

        # Apply gravity to player (falling effect)
        player_gravity += 1
        player_rect.y += player_gravity
        # Prevent player from falling below ground
        if player_rect.bottom >= 320:
            player_rect.bottom = 320
            player_gravity = 0  # Reset gravity on ground

        # Draw player
        screen.blit(player_surface, player_rect)

        # Update collision rectangle with player's position
        player_collision_rect = player_rect.inflate(-30, -20)

        # Move obstacles with current speed
        obstacle_rect_list = obstacle_movement(obstacle_rect_list, speed)

        # Check collisions; if True = keep running, if False = game over
        game_active = collisions(player_collision_rect, obstacle_rect_list)

    # ------------------ GAME OVER SCREEN ------------------
    else:
        screen.fill('orange')                   # Orange background
        screen.blit(character, (350, 100))      # Show character image
        screen.blit(Name, (230, 50))            # Show title text
        obstacle_rect_list.clear()              # Remove obstacles
        player_rect.midbottom = (100, 340)      # Reset player position
        player_gravity = 0                      # Reset gravity

        # Display score message
        score_message = test_font.render(f'Your score is {score}', False, "#000000")

        if score == 0:   # If never scored, show replay instruction
            screen.blit(Replay, (200, 300))
        else:            # Otherwise show final score
            screen.blit(score_message, (180, 300))

    # Update display
    pygame.display.update()
    # Cap framerate to 60 FPS
    clock.tick(60)
