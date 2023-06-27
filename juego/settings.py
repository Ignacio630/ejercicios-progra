#colores

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)



level_map = [
    '                                  ',
    '                                  ',
    'XXXX      XX             XX       ',
    'XXXX      XX                      ',
    'XXXXXX                        XX  ',
    'XXXXXX           XX               ',
    'XX             XX                 ',
    '          X  XXXX      XX  XX     ',
    '          X  XXXX      XX  XXXX   ',
    '        XXX  XXXXXXXX  XX  XXXX   ',
    'XXXXXXXXXXX  XXXXXXXX  XX  XXXX   '
]
platform_size = 64
#definimos las dimensiones iniciales de la pantalla
screen_width = 1200
screen_height = len(level_map) * platform_size
#fotogramas por segundo del juego
FPS = 120    


