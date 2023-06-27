import pygame
from constantes import *
from funciones_utiles import *


class Jugador:

    def __init__(self,posicion,nombre) -> None:
        self.imagen_jugador = pygame.image.load('{0}character.png'.format(PATH_JUGADOR))
        self.nombre_jugador = nombre
        self.posicion_jugador = self.imagen_jugador.get_rect(posicion)

        self.velocidad = 5
    



    def input(self):
        teclas = pygame.key.get_pressed()

