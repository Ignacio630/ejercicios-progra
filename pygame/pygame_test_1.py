import pygame

pygame.init

size = (800, 600)

screen = pygame.display.set_mode(size)

time = pygame.time.Clock()

initial_cord_pj = 
img_pj = pygame.image.load("pygame\img\pj.png")
img_r = pygame.transform.scale(img_pj, (100, 100))
running = True

# colors

white = (255, 255, 255)
black = (0, 0, 0)
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    player = img_r.get_rect()

    screen.blit(img_r, player)
    pygame.display.flip()
    time.tick(60)


pygame.quit()
