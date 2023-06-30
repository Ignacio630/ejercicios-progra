import pygame
from constantes import*

class Enemy:

    def __init__(self,size,pos,gravity,move_x) -> None:
        self.surface_enemy = pygame.surface.Surface((size,size))
        self.surface_enemy.fill(R)
        self.rect_enemy = self.surface_enemy.get_rect(topleft = pos)
        self.gravity = gravity
        self.move_x = move_x
    def update(self):
        
        self.rect_enemy.x += self.move_x

        if self.rect_enemy.y > ALTO_PANTALLA:
            self.rect_enemy.y += self.gravity

    def draw(self,pantalla):
        
        pantalla.blit(self.surface_enemy,self.rect_enemy)