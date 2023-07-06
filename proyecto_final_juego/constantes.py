#fotogramas por segundo del juego
FPS = 60    

#debug
DEBUG = True

#definimos la direccion de la carpeta con los recursos

PATH_RECURSOS = "recursos"
PATH_SPRITES = "{0}/sprites/".format(PATH_RECURSOS)
PATH_ENEMIGO = "{0}enemigo/".format(PATH_SPRITES)
PATH_JUGADOR = "{0}jugador/".format(PATH_SPRITES)
PATH_STAND = "stand/"
PATH_WALK = "walk/"
PATH_RUN = "run/"
PATH_JUMP = "jump/"
PATH_ATTACK = "attack/"
PATH_FONDO = "{0}/fondo/".format(PATH_RECURSOS)
#colores

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
B = (0,0,0)
W = (255,255,255)

#direccion

DIRECCION = True

platform_size = 50


level_map = [
    '                               ',
    '                               ',
    '                               ',
    'E                              ',
    'XXXX      XX             XX    ',
    'XXXX      XX                   ',
    'XXXXXX                       XX',
    'XXXXXX      P    XX            ',
    'XX             XX            E ',
    '          X  XXXX      XX  XXXX',
    '          X  XXXX      XX  XXXX',
    '        XXX  XXXXXXXX  XX  XXXX',
    'XXXXXXXXXXX  XXXXXXXX  XX  XXXX'
]

#definimos las dimensiones iniciales de la pantalla
ANCHO_PANTALLA = 1200
ALTO_PANTALLA = len(level_map) * platform_size
