"""program for a llama game similar to the dinosaur game - v6
allow player to quit or play again after losing
created by Charlotte"""

import pygame
import random

class Cactus:
    def __init__(self, x, y):
        self.image = pygame.image.load("images/cactus.png").convert_alpha()
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

black = (0, 0, 0)
white = (255, 255, 255)
msg_font = pygame.font.SysFont("arialblack", 20)

def message(msg, txt_colour):
    """display messages"""
    txt = msg_font.render(msg, True, txt_colour)

    # centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))

    SCREEN.blit(txt, text_box)

def game_loop():
    X_POSITION, Y_POSITION = 300, 400  # x and y position of the llama
    x_cactus1, y_cactus1 = 1000, 412  # x and y position of cactus to be changed
    x_cactus2, y_cactus2 = 1300, 412  # x and y position of cactus to be changed

    # for gravity
    jumping = False

    Y_GRAVITY = 1  # can't be < 0.01 * JUMP_HEIGHT
    JUMP_HEIGHT = 17
    Y_VELOCITY = JUMP_HEIGHT

    # surfaces to represent llama and ground - 2 surfaces for jump/standing llama
    STANDING_SURFACE = pygame.transform.scale(
        pygame.image.load("images/Llama2.png"),
        (42, 58))
    JUMPING_SURFACE = pygame.transform.scale(
        pygame.image.load("images/Llama.png"),
        (42, 58))
    GROUND = pygame.image.load("images/ground.png")
    RESIZED_GROUND = pygame.transform.smoothscale(GROUND, [1000, 100])
    cactus1 = Cactus(x_cactus1, y_cactus1)
    cactus2 = Cactus(x_cactus2, y_cactus2)

    # # to allow program to randomize size of cactus
    # resized_cactus = pygame.transform.smoothscale(cactus2,
    #                                        [width_cactus, height_cactus])

    SCREEN.fill(white)  # white background

    quit_game = False

    while not quit_game:  # let user quit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = ("Exit: click X again or 'q' to Quit, SPACE to "
                                "resume, 'R' to reset")
                message(instructions, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        # if user presses X button, game quits
                        if event.type == pygame.QUIT:
                            print("quit")
                            quit_game = True
                            end = True

                        if event.type == pygame.KEYDOWN:
                            # if user presses 'R' button, game is reset
                            if event.key == pygame.K_r:
                                print("key pressed: r")
                                end = True, game_loop()

                            # if user presses the space-bar, game continues
                            elif event.key == pygame.K_SPACE:
                                print("key pressed: space-bar")
                                end = True

                            # if user presses 'Q' game quits
                            elif event.key == pygame.K_q:
                                print("key pressed: q")
                                quit_game = True
                                end = True

                            # if user presses 0, nothing happens (just for update)
                            elif event.key == pygame.K_0:
                                print("key pressed: 0")


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
            scale_cactus = random.randint(32, 45)
            cactus1.image = pygame.transform.smoothscale(cactus1.image,
                                                         [scale_cactus,
                                                          scale_cactus])
            cactus1.rect = cactus1.image.get_rect()
            x_cactus1 = random.randint(1000, 1200)
        else:
            x_cactus1 -= 5

        if x_cactus2 < 0:
            scale_cactus = random.randint(32, 45)
            cactus2.image = pygame.transform.smoothscale(cactus2.image,
                                                 [scale_cactus, scale_cactus])
            cactus2.rect = cactus2.image.get_rect()
            x_cactus2 = 1000
        else:
            x_cactus2 -= 5

        cactus1.rect.center = x_cactus1, y_cactus1
        SCREEN.blit(cactus1.image, cactus1.rect)

        cactus2.rect.center = x_cactus2, y_cactus2
        SCREEN.blit(cactus2.image, cactus2.rect)

        pygame.display.update()
        CLOCK.tick(60)  # FPS

    pygame.quit()
    quit()

# Main routine
game_loop()
