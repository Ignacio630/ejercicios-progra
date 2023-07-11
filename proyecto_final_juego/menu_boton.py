import pygame
from constantes import *
from funciones_utiles import *

class Boton:
    def __init__(self,path,size,frame,master_screen,pos) -> None:
        self.screen = master_screen
        self.surface_button = getSurface(path=path,frame=frame,flag_flip=False,size=size)
        self.rect_button = self.surface_button.get_rect(topleft = pos)
        
    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.surface_button,self.rect_button)