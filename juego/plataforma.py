import pygame
from settings import *


class Plataforma(pygame.sprite.Sprite):
    def __init__(self,pos,size) -> None:
        super().__init__()
        self.image = pygame.surface.Surface((size,size))
        self.image.fill(R)
        self.rect = self.image.get_rect(topleft = pos)







