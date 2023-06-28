import pygame
from settings import *
from plataforma import *



class Player:

    def __init__(self,pos,size) -> None:
        self.x = 0
        self.y = 0
        self.imagen = pygame.surface.Surface((size,size))
        self.imagen.fill(WHITE)
        self.rect = self.imagen.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        else: 
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.direction.y = -16 
    def apply_gavity(self):
        self.direction.y += 0.8
        self.rect.y += self.direction.y

    def update(self):

        self.input()
        self.apply_gavity()

        self.rect.x += self.direction.x * 8

        

    def draw(self,screen):
        screen.blit(self.imagen,self.rect)