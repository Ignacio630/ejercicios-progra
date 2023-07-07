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
                    self.player = Jugador(path=PATH_JUGADOR,speed_walk=5,speed_run=10,jump_power=-16,gravity=0.8,size=(50,90),pos=(x,y))
                if row == "L":
                    limite = Limits(platform_size,(x,y),self.screen)
                    self.limits_list.append(limite)

    def colliders_player_x(self):
        player = self.player
        player.rect_jugador.x += player.direction.x * player.walk_speed

        for platform in self.platforms_list:
            if platform.rect.colliderect(player.rect_jugador):
                if player.direction.x < 0:
                    player.rect_jugador.left = platform.rect.right
                elif player.direction.x > 0:
                    player.rect_jugador.right = platform.rect.left
                    
    def colliders_player_y(self):
        player = self.player
        player.apply_gravity()

        for platform in self.platforms_list:
            if platform.rect.colliderect(player.rect_jugador):
                if player.direction.y < 0:
                    player.rect_jugador.top = platform.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect_jugador.bottom = platform.rect.top                
                    player.direction.y = 0
        # if player.rect_jugador.bottom == ALTO_PANTALLA:



    def move_world_player(self):
        direction_x = self.player.direction.x

        if self.player.rect_jugador.centerx < ANCHO_PANTALLA/5 and direction_x < 0:
            self.world_move_x = 5
            self.player.walk_speed = 0
        elif self.player.rect_jugador.centerx > ANCHO_PANTALLA -(ANCHO_PANTALLA/5) and direction_x > 0:
            self.world_move_x = -5
            self.player.walk_speed = 0
        else:
            self.world_move_x = 0
            self.player.walk_speed = 5

        # if self.player.rect_jugador.centerx <= ANCHO_PANTALLA/5:
        #      self.world_move_x = 0
        #      if self.player.rect_jugador.left >= 0:
        #          self.player.walk_speed = 5

        for limits in self.limits_list:
            if limits.rect.colliderect(self.player.rect_jugador):
                print("a")

    def draw(self,delta_ms):
        #fondo
        self.screen.fill(W)
        #mundo
        for platform in self.platforms_list:
            platform.update(self.world_move_x)
            platform.draw(self.screen)

        for limits in self.limits_list:
            limits.draw()
            
        self.move_world_player()


        #jugador
        self.player.update(delta_ms)
        self.colliders_player_x()
        self.colliders_player_y()
        self.player.draw(self.screen)
