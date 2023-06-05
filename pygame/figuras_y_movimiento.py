import pygame

pygame.init()

ancho = 1280
alto = 720

tamaño_pantalla = (ancho,alto)

pantalla = pygame.display.set_mode(tamaño_pantalla)

tiempo = pygame.time.Clock()

#colores
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

running = True

obj_1_cord_y = 460 
obj_1_cord_x = 640

speed_y = 3
speed_x = 3
while running:
    teclas = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    pantalla.fill(white)

    pygame.draw.rect(pantalla,white,(obj_1_cord_x,obj_1_cord_y,50,50))
    objeto_1 = pygame.draw.rect(pantalla,black,(obj_1_cord_x,obj_1_cord_y,100,100))
    if teclas[pygame.K_UP]:
        obj_1_cord_y += -speed_y
    elif teclas[pygame.K_DOWN]:
        obj_1_cord_y += speed_y
    elif teclas[pygame.K_RIGHT] and obj_1_cord_x < 50:
        obj_1_cord_x += speed_x
    elif teclas[pygame.K_LEFT] and obj_1_cord_x < 1180:
        obj_1_cord_x += -speed_x

    if obj_1_cord_x > 1180 or obj_1_cord_x < 50:
        speed_x *= -1
    if obj_1_cord_y > 620 or obj_1_cord_y < 50: 
        speed_y *= -1

    pygame.display.flip()
    tiempo.tick(60)
