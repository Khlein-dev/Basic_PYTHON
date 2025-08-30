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
doggy_sit = 600

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
            
    # screen.blit(sky_surface,(0,0))
    screen.blit(pygame.transform.scale(sky_surface, (800, 400)), (0, 0))
    screen.blit(pygame.transform.scale(ground_surface, (800, 100)), (0, 300))
    screen.blit(text_surface,(200, 50))
    doggy_sit -= 2
    if doggy_sit < -100: doggy_sit = 800
        
        
    screen.blit(pygame.transform.scale(doggy_surface, (90, 90)), (doggy_sit, 250))
    
    #Draw elements
    #Update everything
    pygame.display.update()
    clock.tick(60)
    



