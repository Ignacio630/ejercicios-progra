import pygame
from funciones_utiles import *

class Widget:

    def __init__(self,screen,w,h,x,y) -> None:
        self.main_screen = screen
        self.widht = w
        self.height = h
        self.pos_x = x
        self.pos_y = y
        

    def draw(self):
        self.main_screen.blit(self.subscreen,self.subscreen_rect)