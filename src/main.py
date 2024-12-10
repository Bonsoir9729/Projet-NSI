import pygame
import sys
from UI import UI
from UIBlock import UIBlock
from const import *

def main() :

    Init()
    while True:
        Update()

def Init() :
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)

    UI.Init()

    #Debug
    UIBlock(None, (200,100), color=DARK)
    UIBlock(None, (200,100), color=WHITE)
    UIBlock(None, (200,100), color=DARK)
    UIBlock(None, (200,100), color=WHITE)


def Update() :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit()
        # Drag & drop
        if event.type == pygame.MOUSEBUTTONDOWN :
            UI.HandleMouseButtonDown()

        elif event.type == pygame.MOUSEBUTTONUP :
            UI.HandleMouseButtonUp()

    UI.Update()
    pygame.display.flip()

def Quit() :
    pygame.quit()
    sys.exit()

    #Sauvegarde du fichier en cours de modification à implémenter ici

if __name__ == "__main__" :
    main()