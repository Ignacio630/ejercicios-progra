import pygame
from constantes import *
from jugador import Jugador
from mapa import Mapa
from plataformas import Plataforma
pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

pygame.init()

tiempo = pygame.time.Clock()
esta_corriendo = True
lista_plataformas = []

#Instancias de objetos
player1 = Jugador(path="{0}stay_frames.png".format(PATH_JUGADOR),frame_rate=60,speed_walk=5,speed_run=10,jump_power=40,jump_height=30,gravity=10)
mapa_1 = Mapa("{0}fondo.png".format(PATH_FONDO))

lista_plataformas.append(Plataforma("{0}plataformas.png".format(PATH_FONDO),400,260,0,TAMANIO_PLATAFORMA))
lista_plataformas.append(Plataforma("{0}plataformas.png".format(PATH_FONDO),460,260,0,TAMANIO_PLATAFORMA))

# bucle principal
while esta_corriendo:
    delta_ms = tiempo.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esta_corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)    
    player1.inputs(keys)    
    
    #Update jugador, enemigo, mapa, etc
    pantalla.blit(mapa_1.draw(),(0,0))

    for plataforma in lista_plataformas:
        plataforma.draw(pantalla)

    player1.update(delta_ms)
    player1.draw(pantalla)
    pygame.display.flip()
    
pygame.quit()