import pygame

pygame.init()

height = 600
width = 800

size = (width, height)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

running = True

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Player
speed_player = 5  
player_x = width // 2 - 30
player_y = height - 30  

player = pygame.Rect(player_x, player_y, 30, 30)

#shoot


speed_shoot = 30
shoot_x = width /2 - 15 
shoot_y = height - 15
shoot_player = pygame.Rect(player_x,player_y+15,5,5)


def movement_player():
    if keys[pygame.K_LEFT]:
        player.left -= speed_player
        shoot_player.left -= shoot_player
    elif keys[pygame.K_RIGHT]:
        player.right += speed_player


def shooting():
    if keys[pygame.K_SPACE]:
        shoot_player.y -= speed_shoot
        
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    movement_player()
    shooting()

    screen.fill(black)
    pygame.draw.rect(screen,blue,shoot_player)
    pygame.draw.rect(screen, red, player)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
