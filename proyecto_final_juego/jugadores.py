import pygame
from constatenes import *

def getFrameSprite(path,columns,rows,step=1):
    lista = []
    surface_image = pygame.image.load(path)
    f_width = int(surface_image.get_width()/columns)
    f_height = int(surface_image.get_height()/rows)

    for column in range(columns):
        for row in range(rows):
            x = column * f_width
            y = row * f_height
            surface_f = surface_image.subsurface(x,y,f_width,f_height)
            lista.append(surface_f)


    return lista

class Personaje:

    def __init__(self,path,size,postion) -> None:
        self.posicion_inicial = postion
        self.frame = 0
        self.animation = getFrameSprite(path,9,6,1)
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.life = 100
        self.score = 0
        self.move_x = 0
        self.move_y = 0


    def input(self,x=0,y=0):
        self.move_x = x
        self.move_y = y
        

    def update(self):
        if (self.frame < len(self.animation)-1):
            self.frame += 1
        else:
            self.frame = 0
        
        self.rect.x += self.move_x
        self.rect.y -= self.move_y
        

    def draw(self,pantalla):
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        pantalla.blit(self.image,self.rect)