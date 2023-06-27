import pygame
from constantes import *
from jugador import Jugador

pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.init()
tiempo = pygame.time.Clock()
imagen_fondo = pygame.image.load("{0}fondo.png".format(PATH_FONDO))
tick_1s = pygame.USEREVENT + 0
esta_corriendo = True
player1 = Jugador("{0}character.png".format(PATH_RECURSOS),(100,0),(0,0))


while esta_corriendo:
    tiempo.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esta_corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)    
    
    #Update jugador, enemigo, mapa, etc
    player1.update()
    pantalla.blit(imagen_fondo,(0,0))
    player1.draw(pantalla)
    pygame.display.flip()
    
pygame.quit()