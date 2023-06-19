import pygame
from constatenes import *
from jugadores import Personaje

pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
pygame.init()
tiempo = pygame.time.Clock()
imagen_fondo = pygame.image.load("{0}fondo.png".format(PATH_RECURSOS))
tick_1s = pygame.USEREVENT + 0
esta_corriendo = True
player1 = Personaje("{0}character.png".format(PATH_RECURSOS),(100,100),(0,0))


while esta_corriendo:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esta_corriendo = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)    
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                player1.input(0,5)
            if event.type == pygame.K_DOWN:
                player1.input(0,-5)
            if event.type == pygame.K_LEFT:
                player1.input(-5,0)
            if event.type == pygame.K_RIGHT:
                player1.input(5,0)
    tiempo.tick(FPS)
    
    #Update jugador, enemigo, mapa, etc
    pygame.display.flip()
    pantalla.blit(imagen_fondo,imagen_fondo.get_rect())
    
    player1.update()
    player1.draw(pantalla)
pygame.quit()