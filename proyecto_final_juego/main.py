import pygame
from constantes import *


pantalla_juego = (ANCHO_PANTALLA,ALTO_PANTALLA)
pygame.display.set_mode(pantalla_juego)
pygame.display.set_caption("Souls-like")

pygame.init()

clock = pygame.time.Clock()
esta_corriendo = True



while esta_corriendo:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esta_corriendo = False

    pygame.display.flip()

pygame.quit()