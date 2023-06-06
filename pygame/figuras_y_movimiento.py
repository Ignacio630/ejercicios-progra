import pygame

pygame.init()

ancho = 1280
alto = 720

tamaño_pantalla = (ancho,alto)

pantalla = pygame.display.set_mode(tamaño_pantalla)

tick_1s = pygame.USEREVENT - 0 
pygame.time.set_timer(tick_1s,10)

tiempo = pygame.time.Clock()

#colores
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

running = True

obj_1_cord_y = 660 
obj_1_cord_x = 0

speed_x = 10
speed_y = 3

en_suelo = True
altura_maxima = 0
while running:
    teclas = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    pantalla.fill(white)

    objeto_1 = pygame.draw.rect(pantalla,black,(obj_1_cord_x,obj_1_cord_y,100,100))
    objeto_1 = pygame.draw.rect(pantalla,red,(obj_1_cord_x,obj_1_cord_y,100,100),4)
    plataforma_1 = pygame.draw.rect(pantalla,red,(200,500,100,10))
    plataforma_2 = pygame.draw.rect(pantalla,red,(400,500,100,10))
    plataforma_3 = pygame.draw.rect(pantalla,red,(600,500,100,10))
    plataforma_4 = pygame.draw.rect(pantalla,red,(800,500,100,10))
    altura_actual = objeto_1.bottom
    altura_maxima = objeto_1.bottom + 300
    if teclas[pygame.K_RIGHT]:
        obj_1_cord_x += speed_x
    if teclas[pygame.K_LEFT]:
        obj_1_cord_x -= speed_x
    print(objeto_1.bottom)
    print(plataforma_1.top)
    
    if objeto_1.colliderect(plataforma_1) and objeto_1.bottom == plataforma_1.top+1 or \
       objeto_1.colliderect(plataforma_2) and objeto_1.bottom == plataforma_2.top+1 or \
       objeto_1.colliderect(plataforma_3) and objeto_1.bottom == plataforma_3.top+1 or \
       objeto_1.colliderect(plataforma_4) and objeto_1.bottom == plataforma_4.top+1:
        en_suelo = False
        speed_y = 0
    elif en_suelo:
        speed_y = 3
    else:
        en_suelo = True
        altura_actual = objeto_1.bottom
    if teclas[pygame.K_SPACE] and en_suelo and altura_actual < altura_maxima:
        obj_1_cord_y -= 30
        altura_actual += 30

    obj_1_cord_y += speed_y

    if obj_1_cord_y < 0:
        obj_1_cord_y = 0
    elif obj_1_cord_y > alto - 100:
        obj_1_cord_y = alto - 100

    if obj_1_cord_x < 0:
        obj_1_cord_x = 0
    elif obj_1_cord_x > ancho - 100:
        obj_1_cord_x = ancho - 100

    pygame.display.flip()
    tiempo.tick(60)
