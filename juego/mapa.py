import pygame 
from settings import *
from plataforma import Plataforma



class Mapa:
    def __init__(self,level_data,surface) -> None:
        self.display_surface = surface
        self.level_design(level_data)
    
    def level_design(self,design):
        self.platforms = pygame.sprite.Group()
        for i,row in enumerate(design):
            for j,cell in enumerate(row):
                if cell == "x":
                    x = j * platform_size
                    y = i * platform_size 
                    platform = Plataforma((x,y),platform_size)
                    self.platforms.add(platform)
    def run(self):
        self.platforms.draw(self.display_surface)