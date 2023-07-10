import pygame
from constantes import*

class Enemy:

    def __init__(self,size,pos) -> None:
        self.surface_enemy = pygame.surface.Surface((size,size))
        self.surface_enemy.fill(R)
        self.rect_enemy = self.surface_enemy.get_rect(topleft = pos)

        #movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0    


    def draw(self,screen):
        screen.blit(self.surface_enemy,self.rect_enemy)