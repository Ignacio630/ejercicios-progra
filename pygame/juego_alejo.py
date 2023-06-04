import pygame
import random

# Dimensiones de la ventana del juego
ANCHO = 800
ALTO = 400

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Tamaño de la paleta
ANCHO_PALETA = 10
ALTO_PALETA = 60

# Velocidad de movimiento de las paletas
VELOCIDAD_PALETAS = 5

# Inicialización de Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")
reloj = pygame.time.Clock()

# Posiciones iniciales de las paletas y la pelota
pos_paleta_jugador = pygame.Rect(50, ALTO // 2 - ALTO_PALETA // 2, ANCHO_PALETA, ALTO_PALETA)
pos_paleta_oponente = pygame.Rect(ANCHO - 50 - ANCHO_PALETA, ALTO // 2 - ALTO_PALETA // 2, ANCHO_PALETA, ALTO_PALETA)
pos_pelota = pygame.Rect(ANCHO // 2 - 10, ALTO // 2 - 10, 20, 20)
velocidad_pelota_x = random.choice([-2, 2])
velocidad_pelota_y = random.choice([-2, 2])
# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Movimiento de las paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        pos_paleta_jugador.y -= VELOCIDAD_PALETAS
    if teclas[pygame.K_DOWN]:
        pos_paleta_jugador.y += VELOCIDAD_PALETAS

    # Movimiento automático de la paleta del oponente
    if pos_paleta_oponente.y + ALTO_PALETA // 2 < pos_pelota.y:
        pos_paleta_oponente.y += VELOCIDAD_PALETAS
    if pos_paleta_oponente.y + ALTO_PALETA // 2 > pos_pelota.y:
        pos_paleta_oponente.y -= VELOCIDAD_PALETAS

    # Movimiento de la pelota
    pos_pelota.x += velocidad_pelota_x
    pos_pelota.y += velocidad_pelota_y

    # Colisiones de la pelota con los bordes
    if pos_pelota.y <= 0 or pos_pelota.y >= ALTO - 20:
        velocidad_pelota_y *= -1
    if pos_pelota.colliderect(pos_paleta_jugador) or pos_pelota.colliderect(pos_paleta_oponente):
        velocidad_pelota_x *= -1

    # Dibujar elementos en la ventana
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, BLANCO, pos_paleta_jugador)
    pygame.draw.rect(ventana, BLANCO, pos_paleta_oponente)
    pygame.draw.ellipse(ventana, BLANCO, pos_pelota)

    # Actualizar la pantalla
    pygame.display.flip()
    reloj.tick(60)