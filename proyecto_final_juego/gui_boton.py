import pygame
from gui_widget import Widget
from funciones_utiles import *

class Botton(Widget):

    def __init__(self, screen, w, h, x, y,path,image_name,event,event_type) -> None:
        super().__init__(screen, w, h, x, y)
        self.main_rect = self.main_screen.get_rect(topleft=(x,y))
        self.path = path
        self.image_name = image_name
        self.event = event
        self.event_type = event_type
    
    def setup_button(self):
        self.subscreen = getSurface(path=self.path,frame=self.image_name,flag_flip=False,size=(self.w,self.h))
        self.subscreen_rect = self.subscreen.get_rect(topleft=(self.x,self.y))
        self.subscreen_rect_collide = pygame.Rect(self.subscreen_rect)

        # self.subscreen_rect_collide.x += self.main_rect.x
        # self.subscreen_rect_collide.y += self.main_rect.y

    def update(self,event_list):
        self.setup_button()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if self.subscreen_rect_collide.collidepoint(event.pos):
                    print(self.subscreen_rect)
                    self.event(self.event_type)

    def draw(self):
        super().draw()

        self.main_screen.blit(self.subscreen,self.subscreen_rect)
        if DEBUG:
            pygame.draw.rect(self.main_screen,(255,0,0),self.subscreen_rect_collide,1)