import pygame
from constantes import *
from funciones_utiles import *

class Plataforma:
    
    def __init__(self,path,x,y,width,heigth,type) -> None:
        self.imagen_plataforma = getSurfaceFromSprites(path=path,columnas=13,filas=13,step=1,flag_flip=True,size=(width,heigth))[type]
        print(self.imagen_plataforma)
        self.rect_plataforma = self.imagen_plataforma.get_rect()
        self.rect_plataforma.x = x
        self.rect_plataforma.y = y

    def draw(self,screen):
        screen.blit(self.imagen_plataforma,self.rect_plataforma)
        if(DEBUG):
            pygame.draw.rect(screen,R,self.rect_plataforma,3)


plataforma = Plataforma(path="{0}plataformas.png".format(PATH_FONDO),x=10,y=10,width=10,heigth=10,type=0)
