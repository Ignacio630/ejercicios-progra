import pygame
from constantes import * 
from funciones_utiles import getSurfaceFromSprites

class Plataforma:

    def __init__(self,pos,size,type) -> None:
        self.surface = getSurfaceFromSprites(path="{0}plataformas.png".format(PATH_FONDO),columnas=12,filas=12,step=True,size=size)[type]
        self.surface.fill(R)
        self.rect = self.surface.get_rect(topleft = pos)

    def update(self,world_speed_x):
        self.rect.x += world_speed_x

    def draw(self,screen):
        screen.blit(self.surface,self.rect)