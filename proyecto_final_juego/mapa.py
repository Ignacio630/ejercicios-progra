import pygame 
from constantes import * 
from  jugador import Jugador
from enemigo import Enemy
from plataformas import Plataforma

class Mapa:
    def __init__(self,level_design,screen) -> None:
        self.platforms_list = []
        self.player = ''
        self.screen = screen
        self.setup_map(level_design)

    
    def setup_map(self,level_map):
        for row_index,item in enumerate(level_map):
            for column_index,column in enumerate(item):
                x = column_index * platform_size
                y = row_index * platform_size
                if column == "X":
                    plataforma = Plataforma((x,y),platform_size)
                    self.platforms_list.append(plataforma)
                if column == "P":
                    self.player = Jugador(path=PATH_JUGADOR,speed_walk=5,speed_run=10,jump_power=30,jump_height=300,gravity=10,size=(100,175),pos=(x,y))
                    
    def draw(self):
        # for platform in self.platforms_list:
        #     platform.draw(self.screen)

        self.player.draw(self.screen)