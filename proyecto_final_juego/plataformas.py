import pygame
from constantes import *
from funciones_utiles import *

class Plataforma:
    
    def __init__(self,path,x,y,type,size) -> None:
        self.imagen_plataforma = getSurfaceFromSprites(path,13,13,1,True)[type]
        self.rect_plataforma = self.imagen_plataforma.get_rect()
        self.rect_plataforma.x = x
        self.rect_plataforma.y = y

    def draw(self,screen):
        screen.blit(self.imagen_plataforma,self.rect_plataforma)
        if(DEBUG):
            pygame.draw.rect(screen,R,self.rect_plataforma,3)