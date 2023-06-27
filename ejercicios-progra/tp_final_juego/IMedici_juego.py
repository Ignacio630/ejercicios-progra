import pygame, sys


pygame.init()

#colores

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

size = (800,500)

screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    

    #rellenar pantalla
    screen.fill(white)
    #### Zona de dibujo
    for i in range(100,700,100):
        pygame.draw.line(screen,black,(i,100),(i,400),5)

    #actualizar pantalla
    pygame.display.flip()