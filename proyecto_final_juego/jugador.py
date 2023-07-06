import pygame
from constantes import *
from funciones_utiles import *


class Jugador:
    def __init__(self,path,speed_walk,speed_run,jump_power,gravity,size,pos) -> None:
        self.stay_frames_r = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_STAND),9,False,size)
        self.stay_frames_l = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_STAND),9,True,size)
        self.walk_frame_r = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_WALK),6,False,size)
        self.walk_frame_l = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_WALK),6,True,size)
        self.run_frame_r = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_RUN),8,False,size)
        self.run_frame_l = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_RUN),8,True,size)
        self.attack_frame_r = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_ATTACK),5,False,size)
        self.attack_frame_l = getSurfaceFromSeparateSprite("{0}{1}".format(path,PATH_ATTACK),5,True,size)
        # self.jump_frame_l = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),9,6,1,False,size)
        # self.jump_frame_r = getSurfaceFromSprites("{0}".format(PATH_JUGADOR),9,6,1,False,size)

        self.frame = 0
        self.animation = self.stay_frames_r
        self.imagen_jugador = self.animation[self.frame]
        self.rect_jugador = self.imagen_jugador.get_rect(topleft = pos)
        self.tiempo_transcurrido = 0

        #movimiento
        self.animation_direction = DIRECCION
        self.direction = pygame.math.Vector2(0,0)
        self.walk_speed = speed_walk
        self.gravity = gravity
        self.jump_power = jump_power


    def stay(self):
        if self.animation_direction:
            self.animation = self.stay_frames_r
        else:
            self.animation = self.stay_frames_l

    def walk(self,direction):
        if direction:
            self.direction.x = 1
            self.animation = self.walk_frame_r
        else:
            self.direction.x = -1
            self.animation = self.walk_frame_l

    def jump(self,direction):
        self.direction.y = self.jump_power
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect_jugador.y += self.direction.y
        
    def inputs(self):
        self.stay()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.animation_direction = True
            self.walk(self.animation_direction)
        elif keys[pygame.K_LEFT]:
            self.animation_direction = False
            self.walk(self.animation_direction)
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump(self.animation_direction)

    def update(self,delta_ms): 
        self.inputs()
        #Aplicar animacion
        self.tiempo_transcurrido += delta_ms    
        if (self.tiempo_transcurrido >= 200):
            self.tiempo_transcurrido = 0
            if(self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0
        

    def draw(self,screen):
        if self.frame < len(self.animation):
            self.imagen_jugador = self.animation[self.frame]
        else:
            self.frame = 0

        if DEBUG:
            pygame.draw.rect(self.imagen_jugador,R,self.rect_jugador)
        screen.blit(self.imagen_jugador,self.rect_jugador)