import pygame 
from constantes import * 
from  jugador import Jugador
from enemigo import Enemy
from plataformas import Plataforma
from limits import *

class Mapa:
    def __init__(self,level_design,screen) -> None:
        self.platforms_list = []
        self.limits_list = []
        self.player = 0
        self.screen = screen
        self.setup_map(level_design)
        self.world_move_x = 0
    
    def setup_map(self,level_map):

        for column_index,column in enumerate(level_map):
            for row_index,row in enumerate(column):
                x = row_index * platform_size
                y = column_index * platform_size
                if row == "X":
                    plataforma = Plataforma((x,y),platform_size)
                    self.platforms_list.append(plataforma)
                if row == "P":
                    self.player = Jugador(path=PATH_JUGADOR,speed_walk=SPEED_WALK,speed_run=SPEED_RUN,jump_power=20,jump_height=200,gravity=10,size=(50,90),pos=(x,y))
                if row == "L":
                    limite = Limits(platform_size,(x,y),self.screen)
                    self.limits_list.append(limite)



    def player_camara(self):
        player = self.player
        # if player.rect_jugador.centerx < ANCHO_PANTALLA/5 and player.move_x < 0:
        #     self.world_move_x = 5
        #     player.speed_walk = 0
        if player.rect_jugador.centerx > ANCHO_PANTALLA -(ANCHO_PANTALLA/5):
            self.world_move_x = -5
            player.speed_walk = 0
            player.move_x = 0

        else:
            self.world_move_x = 0
            player.speed_walk = SPEED_WALK


    def draw(self,delta_ms):
        #fondo
        self.screen.fill(W)
        #mundo
        for platform in self.platforms_list:
            platform.update(self.world_move_x)
            platform.draw(self.screen)

        for limits in self.limits_list:
            limits.draw()
            


        #jugador
        self.player_camara()
        self.player.update(delta_ms)
        self.player.draw(self.screen)
