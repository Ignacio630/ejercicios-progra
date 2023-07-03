import pygame
from constantes import * 


class Plataforma:

    def __init__(self,pos_x,pos_y,width,height) -> None:
        self.surface = pygame.surface.Surface()