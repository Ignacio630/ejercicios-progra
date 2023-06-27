import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

# posicion inicial

objeto_1 = {"y": 250, "x": 250}
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), (250, 250,100,100))

    pygame.display.flip()
pygame.quit()  # Fin
