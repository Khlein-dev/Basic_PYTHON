import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Khlein GO! GO!')
icon = pygame.image.load('pics/khlein.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font('pics/stocky.ttf', 50)

# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

sky_surface = pygame.image.load('pics/sky.jpg').convert()
ground_surface = pygame.image.load('pics/ground.jpg').convert()
text_surface = test_font.render('Khlein GO! GO!', False, 'Blue')

doggy_surface = pygame.image.load('pics/doggy.png').convert_alpha()
doggy_surface = pygame.transform.scale(doggy_surface, (90, 90))
doggy_rect = doggy_surface.get_rect(midbottom = (600, 340))
# doggy_sit = 600

player_surface = pygame.image.load('pics/player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (120, 120))
player_rect = player_surface.get_rect(midbottom = (50, 340))

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
            
    # screen.blit(sky_surface,(0,0))
    screen.blit(pygame.transform.scale(sky_surface, (800, 400)), (0, 0))
    screen.blit(pygame.transform.scale(ground_surface, (800, 100)), (0, 300))
    screen.blit(text_surface,(200, 50))
    # doggy_sit -= 2
    # if doggy_sit < -100: doggy_sit = 800
    
    doggy_rect.x -=2
    if doggy_rect.right < 0:
         doggy_rect.left = 800
    screen.blit(doggy_surface, doggy_rect)
    
    player_rect.left += 1
    screen.blit(player_surface, player_rect)
    
    #Draw elements
    #Update everything
    pygame.display.update()
    clock.tick(60)
    



