import pygame
from settings import *
from mapa import Mapa
from personaje import Player


pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()    
is_running = True
mapa = Mapa(level_map,screen)
p1 = Player((100,100),(100))


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    screen.fill(BLACK)  
    mapa.run()
    p1.update()
    p1.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
    