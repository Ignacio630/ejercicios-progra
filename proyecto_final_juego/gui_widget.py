import pygame
from funciones_utiles import *

class Widget:

    def __init__(self,screen,w,h,x,y) -> None:
        self.main_screen = screen
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        

    def draw(self):
        self.main_screen.blit(self.subscreen,self.subscreen_rect)