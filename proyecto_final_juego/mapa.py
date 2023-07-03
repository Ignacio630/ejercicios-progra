import pygame 
from constantes import * 
from  jugador import Jugador
from enemigo import Enemy


class Mapa:
    def __init__(self,width,height,level_design) -> None:
        self.platforms_list = []
        self.level_design = level_design
        self.background = pygame.surface.Surface((width,height))
        self.background.fill(B)
        self.rect = self.background.get_rect()

    def draw_level(self):
        
        for column_index,column in enumerate(self.level_design):
            for row_index,item in enumerate(column):
                x = column_index * platform_size
                y = row_index * platform_size

                if item == "X":
                    pass
    def draw(self,screen):
        screen.blit(self.background,self.rect)

