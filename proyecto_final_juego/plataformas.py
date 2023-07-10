import pygame
from constantes import * 
from funciones_utiles import *

class Plataforma:

    def __init__(self,pos,size,path,flag,frames) -> None:
        self.surface = getSurfaceFromSeparateSprite(path=path,frames=frames,flag_flip=flag,size=(size,size))[0]
        self.rect = self.surface.get_rect(topleft = pos)

    def update(self,world_speed_x):
        self.rect.x += world_speed_x

    def draw(self,screen):
        screen.blit(self.surface,self.rect)