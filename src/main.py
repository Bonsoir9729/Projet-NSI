import pygame
import sys
import time
from UI import UI
from UIBlock import UIBlock
from const import *

def main() :

    Init()
    deltaTime = 1/FPSCAP
    while True:
        start = time.time()
        Update(deltaTime)
        end = time.time()
        time.sleep(max(0, (1/FPSCAP)-end+start))
        deltaTime = time.time() - start
        print(deltaTime)

def Init() :
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)

    UI.Init()

    #Debug
    for i in range(10) :

        UIBlock(None, (200,100), color=DARK)
        UIBlock(None, (200,100), color=WHITE)


def Update(deltaTime) :

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