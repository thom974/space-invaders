# GAME INITIALIZATION
import pygame, sys

pygame.init()

# GAME VARIABLES
size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
bg_color = (255, 255, 255)

# CREATING THE SHIP
ship = pygame.image.load("data/ship.png")
ship_x = 0
ship_y = 0
ship_left = False
ship_right = False

# BULLETS
bullets = []

# ENEMIES
enemy = pygame.image.load("data/alien.png")
enemies = []

# SCORE
score = 0
e_score = 500

font = pygame.font.Font("data/slkscreb.ttf", 24)


# SETUP
ship = pygame.transform.scale(ship, (100, 100))
ship_rect = ship.get_rect()
ship_x = width / 2 - (ship_rect.width / 2)
ship_y = 600

enemy = pygame.transform.scale(enemy, (100, 100))

for i in range(3):
    for j in range(8):
        enemy_x = 140 + 100 * j
        enemy_y = 50 + 100 * i
        enemy_hitbox = enemy.get_rect()
        enemy_hitbox.update(
            (enemy_x, enemy_y), (enemy_hitbox.width, enemy_hitbox.height)
        )
        enemies.append([[enemy_x, enemy_y], enemy_hitbox, True])

# GAME LOOP
while True:
    for event in pygame.event.get():
        # DETECT EXIT
        if event.type == pygame.QUIT:
            sys.exit()

        # DETECT KEYPRESSES
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ship_left = True
            if event.key == pygame.K_d:
                ship_right = True
            if event.key == pygame.K_SPACE:
                bullet_surface = pygame.Surface((12, 12))
                bullet_surface.fill((255, 255, 255))
                bullet_hitbox = bullet_surface.get_rect()
                bullet_location = [
                    ship_x + ship_rect.width / 2 - bullet_surface.get_width() / 2,
                    ship_y,
                ]

                pygame.draw.circle(bullet_surface, (0, 0, 0), (6, 6), 6)
                bullets.append([bullet_surface, bullet_hitbox, bullet_location, True])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                ship_left = False
            if event.key == pygame.K_d:
                ship_right = False

    # CLEAR SCREEN
    screen.fill(bg_color)

    # UPDATE SHIP MOVEMENT
    if ship_left:
        ship_x -= 3

        if ship_x < 0:
            ship_x += 3

    if ship_right:
        ship_x += 3

        if ship_x + ship_rect.width > width:
            ship_x -= 3

    # UPDATE AND DISPLAY BULLETS
    for i in range(len(bullets)):
        bullets[i][2][1] -= 5

        bullets[i][1].update(bullets[i][2], (bullets[i][1].width, bullets[i][1].height))

        if bullets[i][3]:
            screen.blit(bullets[i][0], bullets[i][1])

    # DRAW ITEMS TO SCREEN
    screen.blit(ship, (ship_x, ship_y))

    # UPDATE AND DISPLAY SCORE
    text = font.render("SCORE: " + str(score), True, (0, 0, 0))
    screen.blit(text, (15, 15))

    # UPDATE AND DISPLAY ENEMIES
    for e_num, e in enumerate(enemies):
        if e[2]:
            screen.blit(enemy, e[0])

        for b_num, b in enumerate(bullets):
            if e[1].colliderect(b[1]) and b[3] and e[2]:
                enemies[e_num][2] = False
                bullets[b_num][3] = False

                score += e_score

    pygame.display.flip()
