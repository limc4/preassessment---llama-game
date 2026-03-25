"""program for a llama game similar to the dinosaur game - v2
initialising the llama and the ground
created by Charlotte"""

import pygame
import sys

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

# surfaces to represent llama and ground
STANDING_SURFACE = pygame.transform.scale(pygame.image.load("images/Llama.png"), (42, 58))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("images/Llama2.png"), (42, 58))
GROUND = pygame.image.load("images/ground.png")

llama_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
SCREEN.fill(white)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(GROUND, (295, 340))
    SCREEN.blit(JUMPING_SURFACE, llama_rect)

    llama_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
    SCREEN.blit(STANDING_SURFACE, llama_rect)

    pygame.display.update()
    CLOCK.tick(60)  # FPS
