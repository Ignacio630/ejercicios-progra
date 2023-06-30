import pygame 
from constantes import * 
from  jugador import Jugador
from enemigo import Enemy
from plataformas import Plataforma


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
                    platform = Plataforma("{0}plataformas.png".format(PATH_FONDO),x=x,y=y,type=0)
                    print(platform)

    def draw(self,screen):
        screen.blit(self.background,self.rect)



mapa = Mapa(ANCHO_PANTALLA,ALTO_PANTALLA,level_map)

mapa.draw_level()