
#definimos las dimensiones iniciales de la pantalla
ANCHO_PANTALLA = 990
ALTO_PANTALLA = 600
#fotogramas por segundo del juego
FPS = 60    

#debug
DEBUG = False

#definimos la direccion de la carpeta con los recursos

PATH_RECURSOS = "proyecto_final_juego/recursos"
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
W = (0,0,0)
B = (255,255,255)

#direccion

DIRECCION = True

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
    '   P    XXX  XXXXXXXX  XX  XXXX   ',
    'XXXXXXXXXXX  XXXXXXXX  XX  XXXX   '
]