import pygame
from sys import exit
from random import randint

def display_score():
   current_time =  int(pygame.time.get_ticks() / 1000) - start_time
   score_surface = test_font.render(f'{current_time}',False,"#000000")
   score_rect = score_surface.get_rect(center =(400,50))
   screen.blit(score_surface,score_rect)
   return current_time


# Might be wrong-----------------------

def obstacle_movement(obstacle_list):
    new_list = []
    for surface, rect in obstacle_list:
        rect.x -= 5
        screen.blit(surface, rect)  # draw correct image
        if rect.x > -50:
            new_list.append((surface, rect))
    return new_list

# ------------------------------------

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Retro Runner')
icon = pygame.image.load('pics/player.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font('pics/pixel.ttf', 30)
replay_font = pygame.font.Font('pics/pixel.ttf', 20)
game_active = False
start_time = 0
score = 0

# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

sky_surface = pygame.image.load('pics/sky.jpg').convert()
ground_surface = pygame.image.load('pics/ground.jpg').convert()
ground_surface = pygame.transform.scale(ground_surface, (800, 100))
ground_x = 0

# text_surface = test_font.render('SCORE', False, "#c0e8ec")
# text_rect =text_surface.get_rect(center = (400, 50))

doggy_surface = pygame.image.load('pics/doggy.png').convert_alpha()
doggy_surface = pygame.transform.scale(doggy_surface, (100, 100))     
# doggy_rect = doggy_surface.get_rect(midbottom = (600, 340))
# center = doggy_rect.center
# doggy_rect.inflate_ip(-85, -20)
# doggy_rect.center = center
# doggy_sit = 600

obstacle_rect_list = []

bird_surface = pygame.image.load('pics/bird.png').convert_alpha()
bird_surface = pygame.transform.scale(bird_surface, (80, 80))

player_surface = pygame.image.load('pics/player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (120, 120))           
player_rect = player_surface.get_rect(midbottom = (100, 340))
player_rect.inflate_ip(-30, -20)

player_gravity = 0



# GAME over Screen

character =  pygame.image.load('pics/player.png').convert_alpha()
character = pygame.transform.scale(character, (200, 200))
Name = test_font.render('RETRO RUNNER', False, "#000000")
Replay = replay_font.render("press 'space' to play", False, "#000000")

# TIMER--------->
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1300)

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:  
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if player_rect.collidepoint(event.pos) and player_rect.bottom >= 320:
                    player_gravity = -21
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 320:
                    player_gravity = -21
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
                start_time = int(pygame.time.get_ticks() / 1000)
                
       # Spawn obstacles
        if event.type == obstacle_timer:
            if randint(0,2):
                obstacle_rect_list.append((doggy_surface, doggy_surface.get_rect(midbottom=(randint(900, 1100), 340))))
            else:
                obstacle_rect_list.append((bird_surface, bird_surface.get_rect(midbottom=(randint(900, 1100), 200))))

            
        # if event.type == pygame.KEYUP:
        #      print("key up")
            
    # screen.blit(sky_surface,(0,0))
    if game_active:
        screen.blit(pygame.transform.scale(sky_surface, (800, 400)), (0, 0))
        
        ground_x -= 4 # speed
        if ground_x <= -ground_surface.get_width():
            ground_x = 0
        
        screen.blit(ground_surface, (ground_x, 300))
        screen.blit(ground_surface, (ground_x + ground_surface.get_width(), 300))
        
        # pygame.draw.rect(screen, (255, 0, 0), doggy_rect) 
        
        # Draw Line
        # pygame.draw.line(screen, 'gold', (0,0) , pygame.mouse.get_pos(), 6)
        
        # Draw Circle
        
        # pygame.draw.rect(screen, "#c0e8ec" , text_rect, 6, 20)
        # screen.blit(text_surface,text_rect)
        
        score = display_score()
        
        # doggy_sit -= 2
        # if doggy_sit < -100: doggy_sit = 800
        
        # doggy_rect.x -=4
        # if doggy_rect.right < 0:
        #     doggy_rect.left = 800
        # screen.blit(doggy_surface, doggy_rect)
        
        # player_rect.left += 1
        
        # ---------PLAYER---------
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 320: player_rect.bottom = 320
        screen.blit(player_surface, player_rect)
        
        
        # OBSTACLE MOVEMENT------------->
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        
        # --------COLLISION--------
        
        game_active = collisions(player_rect, obstacle_rect_list)
       
    else:
        screen.fill('orange')
        screen.blit(character, (300, 100))
        screen.blit(Name, (230, 50) )
        
        score_message = test_font.render(f'Your score is {score}', False, "#000000")
        
        if score == 0:
            screen.blit(Replay, (200, 300) )
        else:
            screen.blit(score_message, (180, 300))
        
        
        # if player_rect.colliderect(doggy_rect):
        #     print("collide")
        
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint((mouse_pos)):
        #     print(pygame.mouse.get_pressed())

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')
        
        
        #Draw elements
        #Update everything
    pygame.display.update()
    clock.tick(60)
    



