import pygame
from constantes import *
from jugador import Jugador
from mapa import Mapa

pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

pygame.init()

tiempo = pygame.time.Clock()
esta_corriendo = True
#Instancias de objetos
player1 = Jugador("{0}stay_frames.png".format(PATH_JUGADOR),60,5,10,20,20,(1250,150))
mapa_1 = Mapa("{0}fondo.png".format(PATH_FONDO))


# bucle principal
while esta_corriendo:
    delta_ms = tiempo.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esta_corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)    
    
    #Update jugador, enemigo, mapa, etc
    pantalla.blit(mapa_1.draw(),(0,0))

    player1.input(keys)
    player1.update(delta_ms)
    player1.draw(pantalla)
    
    pygame.display.flip()
    
pygame.quit()