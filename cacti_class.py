"""program for a llama game similar to the dinosaur game - v4
cactus class to instantiate multiple cacti onscreen
created by Charlotte"""

import pygame
import sys

class Cactus:
    def __init__(self, x, y):
        self.image = pygame.image.load("images/cactus.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y

pygame.init()

CLOCK = pygame.time.Clock()  # regulate the FPS (under CLOCK.tick() at bottom)
# set the size of the display screen
SCREEN = pygame.display.set_mode((1000, 720))

# upload llama icon image in caption
game_icon = pygame.image.load("images/llama_icon.png")

# display the icon
pygame.display.set_icon(game_icon)

# set the caption
pygame.display.set_caption("Llama game - by Charlotte")

white = (255, 255, 255)

X_POSITION, Y_POSITION = 300, 400  # x and y position of the llama
x_cactus1, y_cactus1 = 1000, 412  # x and y position of cactus to be changed
x_cactus2, y_cactus2 = 1300, 412  # x and y position of cactus to be changed
width_cactus, height_cactus = 32, 32

# for gravity
jumping = False

Y_GRAVITY = 1 # can't be < 0.01 * JUMP_HEIGHT
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

# surfaces to represent llama and ground - 2 surfaces for jump/standing llama
STANDING_SURFACE = pygame.transform.scale(pygame.image.load("images/Llama2.png"),
                                          (42, 58))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("images/Llama.png"),
                                         (42, 58))
GROUND = pygame.image.load("images/ground.png")
RESIZED_GROUND = pygame.transform.smoothscale(GROUND, [1000, 100])
cactus1 = Cactus(x_cactus1, y_cactus1)
cactus2 = Cactus(x_cactus2, y_cactus2)

# # to allow program to randomize size of cactus
# resized_cactus = pygame.transform.smoothscale(cactus2,
#                                        [width_cactus, height_cactus])

SCREEN.fill(white)  # white background

# rectangle to control the position of llama
llama_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
# cactus_rect = CACTUS.get_rect(center=(x_cactus, y_cactus))

while True:  # let user quit
    # x_cactus, y_cactus = 1000, 412  # x and y position of cactus to be changed
    # cactus_rect = CACTUS.get_rect(center=(x_cactus, y_cactus))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    # update ground x,y
    SCREEN.fill(white)  # update white background
    SCREEN.blit(RESIZED_GROUND, (0, 370.5))

    if jumping:  # jump with gravity
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:  # jump velocity increases until max then
        # decrease until negative jump height
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        llama_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, llama_rect)
    else:
        llama_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, llama_rect)

    # position llama x,y
    llama_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
    SCREEN.blit(STANDING_SURFACE, llama_rect)

    # move cacti left across screen unless off-screen
    if x_cactus1 < 0:
        x_cactus1 = 1000
    else:
        x_cactus1 -= 5

    if x_cactus2 < 0:
        x_cactus2 = 1000
    else:
        x_cactus2 -= 5

    # if cactus1.x < 0:
    #     cactus1.x = 1000
    # else:
    #     cactus1.x -=5

    # cactus_rect = CACTUS.get_rect(center = (x_cactus, y_cactus))
    # SCREEN.blit(CACTUS, cactus_rect)
    # cactus1.rect.center = x_cactus1, y_cactus1
    # SCREEN.blit(cactus1.image, cactus1.rect)

    cactus1.rect.center = x_cactus1, y_cactus1
    SCREEN.blit(cactus1.image, cactus1.rect)

    cactus2.rect.center = x_cactus2, y_cactus2
    SCREEN.blit(cactus2.image, cactus2.rect)

    pygame.display.update()
    CLOCK.tick(60)  # FPS
