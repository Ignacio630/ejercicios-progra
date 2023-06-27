import pygame as pg
import random 

pg.init()

# Dimensiones de la pantalla
height = 600
width = 800
size = (width, height)

# Configuración de la pantalla
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Jugador
player_speed = 10
player_x = width // 2 - 30
player_y = height - 30
player = pg.Rect(player_x, player_y, 30, 30)
img_player = pg.image.load("pygame/img/inave.png")
img_pj = pg.transform.scale(img_player, (30, 30))

def movement_player():
    global player_x
    if keys[pg.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pg.K_RIGHT] and player_x < width - 30:
        player_x += player_speed
    player.x = player_x

# Disparo
shoot_speed = 10
bullet_y = 0
bullet_x = 0
fire_state = "ready"

def bullet_generation(x: int, y: int):
    bullet = pg.draw.circle(screen, red, (x, y), 3)

    return bullet

def shooting():
    global fire_state, bullet_y, bullet_x
    if fire_state == "ready":
        if keys[pg.K_SPACE]:
            bullet_x = player_x + 15
            bullet_y = player_y + 1
            fire_state = "fire"
    
    if fire_state == "fire":
        bullet_y -= shoot_speed
        if bullet_y <= 0:
            fire_state = "ready"

# Enemigos
enemies = []
enemy_size = 30
cantidad_enemigos = range(0,20)
enemy_pos_x = width/2 - 30 * 10
enemy_pos_y = 0
enemy_speed = 0.5
img_enemy = pg.image.load("pygame/img/enemy.png")
img_enemy_re = pg.transform.scale(img_enemy, (enemy_size, enemy_size))

contador_enemigos = 0
for _ in cantidad_enemigos:
    enemy = pg.Rect(enemy_pos_x, enemy_pos_y, enemy_size, enemy_size)
    enemies.append(enemy)
    enemy_pos_x += enemy_size * 2
    contador_enemigos += 1
    if contador_enemigos % 10 == 0 :
        enemy_pos_x = width / 2 - 30 * contador_enemigos
        enemy_pos_y += enemy_size * 2
def enemy_spawn():
    for enemy in enemies:
        if enemy.y >= 0 and enemy.y < height:
            enemy.y += enemy_speed
        else:
            enemy.y = 0

def remove_enemy(enemy):
    if enemy in enemies:
        enemies.remove(enemy)


def game_over(running):
    for enemy in enemies:
        if player.colliderect(enemy):
            running = False
    return running

# Running
running = True

while running:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    movement_player()
    enemy_spawn()
    running = game_over(running)

    screen.fill(black)

    shooting()
    bullet = bullet_generation(bullet_x, bullet_y)

    screen.blit(img_pj, (player_x, player_y))
    for enemy in enemies:
        screen.blit(img_enemy_re, (enemy.x, enemy.y))
        if enemy.colliderect(bullet):
            remove_enemy(enemy)

    pg.display.flip()
    clock.tick(60)

pg.quit()
