import pygame
from constantes import *
from funciones_utiles import *


class Jugador:
    def __init__(self,path,frame_rate,speed_walk,speed_run,jump_power,jump_height,gravity,size) -> None:
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
        self.rect_jugador = self.imagen_jugador.get_rect()

        self.direction = DIRECCION
        self.frame_rt = frame_rate
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.jump_power = jump_power
        self.jump_height = jump_height
        self.start_jump = 0
        self.is_attacking = False
        self.is_jumping = False
        self.gravity = gravity
        self.move_x = 0
        self.move_y = 0
        self.collition_ground = pygame.Rect(self.rect_jugador.x,self.rect_jugador.bottom,self.rect_jugador.w,self.rect_jugador.h)
        self.tiempo_transcurrido = 0

    #quieto
    def stay(self):
        if self.direction:
            self.animation = self.stay_frames_r
        else:
            self.animation = self.stay_frames_l
    #caminar izq-der
    def walk(self,direccion):
        if direccion:
            self.move_x = self.speed_walk
            self.animation = self.walk_frame_r
        else:
            self.move_x = -self.speed_walk
            self.animation = self.walk_frame_l
    #correr
    def run(self,direccion):
        if direccion:
            self.move_x = self.speed_run
            self.animation = self.run_frame_r
        else:
            self.move_x = -self.speed_run
            self.animation = self.run_frame_l
    #saltar
    def jump(self):
        if not self.is_jumping :
            self.start_jump = self.rect_jugador.bottom
            self.move_y -= self.jump_power
            self.frame = 0
            self.is_jumping = True
    #ataque
    def attack(self):
        if not self.is_attacking:
            if self.direction:
                self.animation = self.attack_frame_r
            else:
                self.animation = self.attack_frame_l
            self.is_attacking = True
        else:
            self.is_attacking = False    

    def inputs(self,keys):
        self.stay()
        self.move_x = 0
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.jump()     
            
        if keys[pygame.K_RIGHT]:
            self.direction = True
            self.walk(self.direction)
        
        if keys[pygame.K_LEFT]:
            self.direction = False
            self.walk(self.direction)
        
        if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]: 
            self.direction = True
            self.run(self.direction)

        if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
            self.run(self.direction)
            print("asd")
        
        if keys[pygame.K_z]:
            self.attack()

    def update(self,delta_ms): 
        self.tiempo_transcurrido += delta_ms    
        
        if (self.tiempo_transcurrido >= 200):
            self.tiempo_transcurrido = 0
            if(self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0

        if (self.start_jump - self.rect_jugador.bottom) == self.jump_height:
            self.move_y = 0
        
        self.rect_jugador.x += self.move_x
        self.rect_jugador.y += self.move_y
        

        
        if(self.rect_jugador.bottom < 500):
            self.rect_jugador.y += self.gravity

        if self.start_jump == self.rect_jugador.bottom:
            self.is_jumping = False

    def draw(self,screen):
        if self.frame < len(self.animation):
            self.imagen_jugador = self.animation[self.frame]
        else:
            self.frame = 0

        if(DEBUG):
            pygame.draw.rect(screen,R,self.rect_jugador,3)
            pygame.draw.rect(screen,R,self.collition_ground,3)
        screen.blit(self.imagen_jugador,self.rect_jugador)