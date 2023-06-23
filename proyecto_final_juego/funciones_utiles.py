import pygame
from constantes import *


def getSurfaceFromSprites(path:str,columnas:int,filas:int,step:int,flag_flip:bool):
    lista_frames = []
    surface_sprite = pygame.image.load(path)
    ancho_frame = (surface_sprite.get_width()/columnas)
    alto_frame = (surface_sprite.get_height()/filas)

    for fila in range(filas):
        for columna in range(0,columnas,step):
            x = columna*ancho_frame
            y = fila*alto_frame
            surface_frame = surface_sprite.subsurface(x,y,ancho_frame,alto_frame)
            if(flag_flip):
                surface_frame = pygame.transform.flip(surface_frame,True,False)
            lista_frames.append(surface_frame)
    return lista_frames

