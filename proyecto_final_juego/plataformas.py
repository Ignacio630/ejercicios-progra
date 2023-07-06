import pygame
from constantes import * 


class Plataforma:

    def __init__(self,pos,size) -> None:
        self.surface = pygame.surface.Surface((size,size))
        self.surface.fill(R)
        self.rect = self.surface.get_rect(topleft = pos)


    def update(self,world_speed_x):
        self.rect.x += world_speed_x

    def draw(self,screen):
        screen.blit(self.surface,self.rect)