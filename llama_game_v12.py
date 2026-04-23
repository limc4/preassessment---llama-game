"""program for a llama game similar to the dinosaur game - v12
fix floating cactus
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
grey = (56, 56, 56)
msg_font = pygame.font.SysFont("arial black", 20)

score_tick = pygame.USEREVENT + 1  # unique event ID for score
pygame.time.set_timer(score_tick, 1000)

def message(msg, txt_colour, center_):
    """display messages"""
    txt = msg_font.render(msg, True, txt_colour)

    # centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=center_)

    SCREEN.blit(txt, text_box)

def vary_cacti(x_cactus, image, rect):
    """Vary scale of cactus and distance it spawns from screen"""
    if x_cactus < 0:
        # randomize size of cactus
        scales = [32, 38, 45]
        scale_choice = random.randint(0, 2)
        scale_cactus = scales[scale_choice]
        image = pygame.transform.smoothscale(image,[scale_cactus,
                                                      scale_cactus])
        rect = image.get_rect()

        # randomize when cactus returns to screen
        x_cactus = random.randint(1000, 1200)
    else:
        x_cactus -= 5
    return x_cactus, image, rect

def game_loop():
    score = 0000
    speed = 60

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

    SCREEN.fill(white)  # white background

    quit_game = False
    game_over = False  # if player loses, game_over = True
    starting_screen = True

    while not quit_game:  # let user quit
        while starting_screen:
            SCREEN.fill(white)
            SCREEN.blit(GROUND, (295, 340))
            # update score
            message(str(f"Score: {score:04}"), grey, (900, 25))
            llama_rect = STANDING_SURFACE.get_rect(center=(X_POSITION,
                                                           Y_POSITION))
            SCREEN.blit(JUMPING_SURFACE, llama_rect)
            message("This is the offline llama game!", black,
                    (500, 250))
            message("Press the SPACEBAR to start", black,
                    (500, 270))
            pygame.display.update()

            for event in pygame.event.get():
                # if user presses the space-bar, game starts
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("key pressed: space-bar")
                        # update ground x,y
                        SCREEN.fill(white)  # update white background
                        SCREEN.blit(RESIZED_GROUND, (0, 370.5))
                        starting_screen = False

        # give the option to quit or play again when they die
        while game_over:
            SCREEN.fill(white)
            message(f"You died!", black, (500, 340))
            message(f"Your score was {score}", black, (500, 360))
            message("Press 'Q' or the top right X button to Quit or 'A' "
                    "to play Again",
                    black, (500, 380))
            pygame.display.update()

            # check if user wants to quit (Q) or play again (A)
            for event in pygame.event.get():
                # if user presses X button, game quits
                if event.type == pygame.QUIT:
                    print("quit")
                    quit_game = True
                    game_over = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    elif event.key == pygame.K_a:
                        game_loop()  # restart the main game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = ("Exit: click X again or 'q' to Quit, SPACE to "
                                "resume, 'R' to reset")
                message(instructions, black, (500, 360))
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

            elif event.type == score_tick:
                score += 1  # increase score every second

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:
            jumping = True

        # update ground x,y
        SCREEN.fill(white)  # update white background
        SCREEN.blit(RESIZED_GROUND, (0, 370.5))

        # update score
        message(str(f"Score: {score:04}"), grey, (900, 25))

        # link speed of game to score
        if score > 10:
            speed = score + 50
        else:
            speed = 60

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

        # detect if llama centre collides with cactus 1 or 2
        if llama_rect.colliderect(cactus1.rect):
            game_over = True

        if llama_rect.colliderect(cactus2.rect):
            game_over = True


        x_cactus1 = vary_cacti(x_cactus1, cactus1.image, cactus1.rect)[0]
        print(x_cactus1)
        cactus1.image = vary_cacti(x_cactus1, cactus1.image, cactus1.rect)[1]
        print(cactus1.image)
        cactus1.rect = vary_cacti(x_cactus1, cactus1.image, cactus1.rect)[2]
        print(cactus1.rect)

        if x_cactus2 < 0:
            # randomize size of cactus2
            scales = [32, 38, 45]
            choice = random.randint(0,2)
            scale_cactus2 = scales[choice]
            cactus2.image = pygame.transform.smoothscale(cactus2.image,
                                                        [scale_cactus2,
                                                            scale_cactus2])
            cactus2.rect = cactus2.image.get_rect()

            x_cactus2 = random.randint(1000,1200)
        else:
            x_cactus2 -= 5

        cactus1.rect.center = x_cactus1, y_cactus1
        SCREEN.blit(cactus1.image, cactus1.rect)

        cactus2.rect.center = x_cactus2, y_cactus2
        SCREEN.blit(cactus2.image, cactus2.rect)

        pygame.display.update()
        CLOCK.tick(speed)  # FPS

    pygame.quit()
    quit()

# Main routine
game_loop()
