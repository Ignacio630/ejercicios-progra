import pygame
from settings import *
from mapa import Mapa
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock
is_running = True
mapa = Mapa(level_map,screen)

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    screen.fill(BLACK)
    mapa.run()
    pygame.display.flip()

pygame.quit()
    