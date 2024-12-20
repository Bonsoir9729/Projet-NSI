import pygame
import sys
from clock import Time

from scene import Scene
from settings import *

from game import Game


def main() :

    Init()

    while True:
        Update(Time.delta)

def Init() :

    if not pygame.get_init() :
        pygame.init()

    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)

    Time.Init()

def Update(deltaTime:float) :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit()
    
    Game.scene.Update(deltaTime)

    pygame.display.flip()

    Time.Update(FPSCAP)

def Quit() :

    pygame.quit()
    sys.exit()

if __name__ == "__main__" :
    main()