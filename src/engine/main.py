import pygame
import sys

from ..const import *
from scene import Scene

def main() :

    Init()
    while True:
        Update()

def Init() :

    pygame.init()

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)

    scene = Scene()


def Update() :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit()

    pygame.display.flip()

def Quit() :
    pygame.quit()
    sys.exit()

if __name__ == "__main__" :
    main()