import pygame
from constantes import *
from gui_boton import Button

pantalla = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

pygame.init()

tiempo = pygame.time.Clock()
esta_corriendo = True

boton_1 = Button(screen=pantalla,w=200,h=50,x=0,y=0,path=PATH_MENU,image_name="new_game",event="click",event_type="click")

# bucle principal
while esta_corriendo:
    delta_ms = tiempo.tick(FPS)  
    keys = pygame.key.get_pressed() 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            esta_corriendo = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     print(event.pos)
        # menu.update(event=event)

    #Update jugador, enemigo, mapa, etc
    # mapa_1.run(delta_ms)
    # menu.draw(event=event)

    boton_1.update()
    boton_1.draw()

    pygame.display.flip()
    
pygame.quit()   