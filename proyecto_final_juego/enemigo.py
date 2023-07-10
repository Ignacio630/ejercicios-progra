import pygame
from constantes import*

class Enemy:

    def __init__(self,size,pos) -> None:
        self.surface_enemy = pygame.surface.Surface((size,size))
        self.surface_enemy.fill(G)
        self.rect_enemy = self.surface_enemy.get_rect(topleft = pos)

        self.speed = 0
    def update(self,world_speed):
        self.rect_enemy.x += world_speed + self.speed
    def draw(self,screen):
        screen.blit(self.surface_enemy,self.rect_enemy)
        
        if DEBUG:
            pygame.draw.rect(screen,R,self.rect_enemy,1)