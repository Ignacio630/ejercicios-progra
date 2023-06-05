import pygame

pygame.init()

# tamaño pantalla
height = 800
width = 500
#
size = (height, width)
screen = pygame.display.set_mode(size)

# timpo
clock = pygame.time.Clock()


# colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# posicion jugadores
pos_j1 = 220
pos_j2 = 220

# posicion linea porteria j2


# posicion pelota
pos_pelota_x = 400
pos_pelota_y = 250

# velocida pelota

speed_y = 3
speed_x = 3

# puntos jugadores
puntos_j1 = 0
puntos_j2 = 0

# texto

fuente = pygame.font.SysFont("Arial Narrow", 25)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    # Obtener el estado de las teclas presionadas
    pressed_keys = pygame.key.get_pressed()

    # Movimiento jugador 1
    if pressed_keys[pygame.K_w] and pos_j1 > 0:
        pos_j1 -= 5
    elif pressed_keys[pygame.K_s] and pos_j1 < 500 - 60:
        pos_j1 += 5

    # Movimiento jugador 2
    if pressed_keys[pygame.K_UP] and pos_j2 > 0:
        pos_j2 -= 5
    elif pressed_keys[pygame.K_DOWN] and pos_j2 < 500 - 60:
        pos_j2 += 5

    pos_pelota_x += speed_x
    pos_pelota_y += speed_y

    # color de fondo
    screen.fill(black)
    # dibujar formas
    jugador_1 = pygame.draw.rect(screen, white, (0, pos_j1, 10, 60))
    jugador_2 = pygame.draw.rect(screen, white, (790, pos_j2, 10, 60))
    porteria_j1 = pygame.draw.line(screen, white, (0, 0), (0, 500), 20)
    porteria_j2 = pygame.draw.line(screen, white, (800, 500), (800, 0), 20)
    linea_central = pygame.draw.line(screen, white, (398, 0), (398, 500), 4)
    bola = pygame.draw.circle(screen, white, (pos_pelota_x, pos_pelota_y), 10)

    # Movimiento pelota

    if pos_pelota_x > 790 or pos_pelota_x < 10 or jugador_1.colliderect(bola) or jugador_2.colliderect(bola):
        speed_x *= -1
    if pos_pelota_y > 490 or pos_pelota_y < 10 or jugador_1.colliderect(bola) or jugador_2.colliderect(bola):
        speed_y *= -1

    # contador puntos jugadores
    if porteria_j1.colliderect(bola) and speed_x < 0:
        puntos_j2 += 0.5

    if porteria_j2.colliderect(bola) and speed_x > 0:
        puntos_j1 += 0.5

    # contador puntos jugadores
    contador_j1 = fuente.render(
        "Jugador 1: {0:.0f}".format(puntos_j1), True, white)
    contador_j2 = fuente.render(
        "Jugador 2: {0:.0f}".format(puntos_j2), True, white)

    screen.blit(contador_j1, (295, 0))
    screen.blit(contador_j2, (405, 0))
    
    if puntos_j1 >= 10:
        ganador = fuente.render("GANADOR JUGADOR 1", True, white)
        screen.fill(black)
        screen.blit(ganador, (300, 200))

    elif puntos_j1 >= 10:
        ganador = fuente.render("GANADOR JUGADOR 2", True, white)
        screen.fill(black)
        screen.blit(ganador, (400, 250))
        
    # actualiza pantalla
    pygame.display.flip()
    clock.tick(120)
