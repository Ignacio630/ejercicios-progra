import pygame
from settings import *


class Plataforma:
    def __init__(self,pos,size) -> None:
        self.pos = pos
        self.size = size
        self.imagen = pygame.surface.Surface((size,size))
        self.imagen.fill(R)
        self.rect = self.imagen.get_rect(topleft = pos)
    
    def draw(self,screen):
        screen.blit(self.imagen ,self.rect)






