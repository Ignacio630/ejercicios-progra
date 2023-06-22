import pygame 
from constantes import * 

class Mapa:
    def __init__(self,path,) -> None:
        self.background = pygame.image.load(path)
        self.background = pygame.transform.scale(self.background,(ANCHO_PANTALLA,ALTO_PANTALLA))

    def draw(self):
        return self.background