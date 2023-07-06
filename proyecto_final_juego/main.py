import pygame
from constantes import *
from jugador import Jugador
from mapa import Mapa
from enemigo import Enemy
from plataformas import Plataforma

pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

pygame.init()

tiempo = pygame.time.Clock()
esta_corriendo = True
lista_plataformas = []

#Instancias de objetos
# player1 = Jugador(path=PATH_JUGADOR,speed_walk=5,speed_run=10,jump_power=30,jump_height=300,gravity=10,size=(100,175))
enemy = Enemy(size=40,pos=(500,500),move_x=10,gravity=10)
mapa_1 = Mapa(level_map,pantalla)


# bucle principal
while esta_corriendo:
    delta_ms = tiempo.tick(FPS)
    keys = pygame.key.get_pressed() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            esta_corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)   
  
 
    #Update jugador, enemigo, mapa, etc
    
    mapa_1.draw(delta_ms)

    pygame.display.flip()
    
pygame.quit()