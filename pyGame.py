import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Khlein GO! GO!')
icon = pygame.image.load('khlein.png')
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
    #Draw elements
    #Update everything
    pygame.display.update()



