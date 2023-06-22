import pygame
from constantes import *
from funciones_utiles import *


class Jugador:
    def __init__(self,path,frame_rate,speed_walk,speed_run,jump_power,jump_height,gravity,size) -> None:
        self.stay_frames = getSurfaceFromSprites(path,9,1,1,False,size)
        self.walk_frame_l = getSurfaceFromSprites("{0}walk_frames.png".format(PATH_JUGADOR),6,1,1,True,size)
        self.walk_frame_r = getSurfaceFromSprites("{0}walk_frames.png".format(PATH_JUGADOR),6,1,1,False,size)
        # self.run_frame_l = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),9,6,1,False,size)
        # self.run_frame_r = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),9,6,1,True,size)
        # self.jump_frame_l = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),9,6,1,False,size)
        # self.jump_frame_r = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),9,6,1,False,size)

        self.frame = 0
        self.animation = self.stay_frames
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
        self.collition_ground = pygame.Rect(self.rect_jugador.x,self.rect_jugador.bottom,self.rect_jugador.w,self.rect_jugador.h)
        self.tiempo_transcurrido = 0



        



    def stay(self):
        self.animation = self.stay_frames
        self.frame = 0
        self.move_x = 0
    
    def walk(self,keys):
        if keys[pygame.K_LEFT]:
            self.move_x = -self.speed_walk
            self.animation = self.walk_frame_l
        elif keys[pygame.K_RIGHT]:
            self.move_x = self.speed_walk
            self.animation = self.walk_frame_r
            
    def jump(self,keys):
        if keys[pygame.K_SPACE]:
            self.move_y = -self.jump_power
            self.animation = self.walk_frame_r
        else:
            self.move_y = 0

    def inputs(self,keys):
        self.stay()
        self.walk(keys)
        self.jump(keys)

    def update(self,delta_ms):
        self.tiempo_transcurrido += delta_ms    
        if (self.tiempo_transcurrido >= 200):
            self.tiempo_transcurrido = 0
            if(self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0
        self.rect_jugador.x += self.move_x
        self.rect_jugador.y += self.move_y


        if(self.rect_jugador.bottom < 400):
            self.rect_jugador.y += self.gravity

    def draw(self,screen):
        self.imagen_jugador = self.animation[self.frame]
        screen.blit(self.imagen_jugador,self.rect_jugador)
        if(DEBUG):
            pygame.draw.rect(screen,R,self.rect_jugador,3)
            pygame.draw.rect(screen,R,self.collition_ground,3)