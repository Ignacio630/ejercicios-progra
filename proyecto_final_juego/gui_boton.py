import pygame
from gui_widget import Widget
from funciones_utiles import *

class Button(Widget):

    def __init__(self, screen, w, h, x, y,path,image_name,event,event_type) -> None:
        super().__init__(screen, w, h, x, y)
        self.path = path
        self.image_name = image_name
        self.event = event
        self.event_type = event_type

    
    def setup_button(self):
        self.subscreen = getSurface(path=self.path,frame=self.image_name,flag_flip=False,size=(self.w,self.h))
        self.subscreen_rect = self.surface.get_rect(topleft=(self.x,self.y))

    
    def update(self):
        self.setup_button()