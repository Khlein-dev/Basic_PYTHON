import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Khlein GO! GO!')
icon = pygame.image.load('pics/khlein.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

sky_surface = pygame.image.load('pics/sky.jpg')
ground_surface = pygame.image.load('pics/ground.jpg')

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
            
    # screen.blit(sky_surface,(0,0))
    screen.blit(pygame.transform.scale(sky_surface, (800, 400)), (0, 0))
    screen.blit(pygame.transform.scale(ground_surface, (800, 100)), (0, 300))
    
    #Draw elements
    #Update everything
    pygame.display.update()
    clock.tick(60)
    



