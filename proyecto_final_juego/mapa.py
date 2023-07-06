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
        self.world_move_x = 0

    
    def setup_map(self,level_map):
        for row_index,item in enumerate(level_map):
            for column_index,column in enumerate(item):
                x = column_index * platform_size
                y = row_index * platform_size
                if column == "X":
                    plataforma = Plataforma((x,y),platform_size)
                    self.platforms_list.append(plataforma)
                if column == "P":
                    self.player = Jugador(path=PATH_JUGADOR,speed_walk=5,speed_run=10,jump_power=30,jump_height=300,gravity=10,size=(50,90),pos=(x,y))
    

    def colliders_player_x(self):
        pass

    def move_world_player(self):
        if self.player.rect_jugador.centerx < ANCHO_PANTALLA/5 and self.player.move_x < 0:
            self.world_move_x = 5
            self.player.move_x = 0
        elif self.player.rect_jugador.centerx > ANCHO_PANTALLA -(ANCHO_PANTALLA/5) and self.player.move_x > 0:
            self.world_move_x = -5
            self.player.move_x = 0
        else:
            self.world_move_x = 0
            self.player.speed_walk = 5

    def draw(self,delta_ms):
        
        #fondo
        self.screen.fill(W)
        
        #mundo
        for platform in self.platforms_list:
            platform.update(self.world_move_x)
            platform.draw(self.screen)
        


        #jugador
        self.player.inputs()
        self.move_world_player()

        self.player.update(delta_ms)
        self.player.draw(self.screen)