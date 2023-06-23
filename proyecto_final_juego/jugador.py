import pygame
from constantes import *
from funciones_utiles import *


class Jugador:
    def __init__(self,path,frame_rate,speed_walk,speed_run,jump_power,jump_height,gravity) -> None:
        self.stay_frames_l = getSurfaceFromSprites(path=path,columnas=9,filas=1,step=1,flag_flip=False)
        self.stay_frames_r = getSurfaceFromSprites(path=path,columnas=9,filas=1,step=1,flag_flip=False)
        self.walk_frame_l = getSurfaceFromSprites("{0}walk_frames.png".format(PATH_JUGADOR),columnas=1,filas=1,step=1,flag_flip=False)
        self.walk_frame_r = getSurfaceFromSprites("{0}walk_frames.png".format(PATH_JUGADOR),columnas=1,filas=1,step=1,flag_flip=False)
        # self.run_frame_l = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),columnas=9,filas=1,step=1,flag_flip=False)
        # self.run_frame_r = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),columnas=9,filas=1,step=1,flag_flip=False)
        # self.jump_frame_l = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),columnas=9,filas=1,step=1,flag_flip=False)
        # self.jump_frame_r = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),columnas=9,filas=1,step=1,flag_flip=False)

        self.frame = 0
        self.animation = self.stay_frames_r
        self.imagen_jugador = self.animation[self.frame]
        self.rect_jugador = self.imagen_jugador.get_rect()

        self.frame_rt = frame_rate
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.jump_power = jump_power
        self.jump_height = jump_height
        self.is_jump = False
        self.gravity = gravity
        self.move_x = 0
        self.move_y = 0
        self.time_elapsed = 0
        self.direction = DIRECTION
        self.is_ground = True

        



    def stay(self):
        if self.direction:
            self.animation = self.stay_frames_r
        else:
            self.animation = self.stay_frames_l
        
        self.move_x = 0
        self.move_y = 0
        self.frame = 0
    def walk(self,keys):
        if keys[pygame.K_LEFT]:
            self.move_x = -self.speed_walk
            self.animation = self.walk_frame_l
        elif keys[pygame.K_RIGHT]:
            self.move_x = self.speed_walk
            self.animation = self.walk_frame_r
        else:
            self.move_x = 0
            
    def jump(self,keys):
        if keys[pygame.K_SPACE] and self.is_jump == False:
            if self.direction:
                self.move_y = -self.jump_power
                self.animation = self.walk_frame_r
            else:
                self.move_y = -self.jump_power
                self.animation = self.walk_frame_l
            self.frame = 0
            self.is_jump = True

    def inputs(self,keys):
        self.stay()
        self.walk(keys)
        self.jump(keys)

    def update(self,delta_ms):
        self.time_elapsed += delta_ms    
        if (self.time_elapsed >= 200):
            self.time_elapsed = 0
            if(self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0
        self.rect_jugador.x += self.move_x
        self.rect_jugador.y += self.move_y

        if self.rect_jugador.bottom == 450 and self.is_ground == True:
                self.is_jump = False

        if(self.rect_jugador.bottom < 450):
            self.rect_jugador.y += self.gravity

    def draw(self,screen):
        self.imagen_jugador = self.animation[self.frame]
        if(DEBUG):
            pygame.draw.rect(screen,R,self.rect_jugador)
        screen.blit(self.imagen_jugador,self.rect_jugador)