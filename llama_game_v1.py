"""program for a llama game similar to the dinosaur game - v1
beginning display screen
created by Charlotte"""

import pygame
import time  # allows sleep to be accessed
pygame.init()

# set the size of the display screen
screen = pygame.display.set_mode((1000, 720))

# upload llama icon image in caption
game_icon = pygame.image.load("images/llama_icon.png")

# display the icon
pygame.display.set_icon(game_icon)

# set the caption
pygame.display.set_caption("Llama game - by Charlotte")

time.sleep(5)  # close display screen after 5 seconds
pygame.quit()
quit()
