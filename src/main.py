import pygame
import sys
from UI import UI
from UIBlock import UIBlock
from const import *

# Utilisée pour le Drag & Drop
UI.block_selected = None

def main() :
    Init()
    while True:
        Update()

def Init() :
    pygame.init()
    pygame.mouse.get_rel()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)

    UI.Init()

    #Debug
    a = UIBlock((50,50),coords=(50,50),color=DARK)
    b = UIBlock((100,50),color=WHITE)
    c = UIBlock((150,20),color=DARK)
    d = UIBlock((200,100),color=WHITE)


def Update() :
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit()

        # Drag & drop
        if event.type == pygame.MOUSEBUTTONDOWN :
            UI.block_selected = UI.CollisionPoint(mousepos)
            # Commencer à drag seulement si une collision est detectée avec le curseur
            if UI.block_selected :
                pygame.mouse.get_rel()
                UI.block_selected.layer = 1

        elif event.type == pygame.MOUSEBUTTONUP and UI.block_selected :
            overlap = UI.block_selected.Overlap()

            if overlap :
                if UI.block_selected.y < overlap.y :
                    UI.block_selected.Attacher(overlap)
                else :
                    overlap.Attacher(UI.block_selected)

            UI.block_selected.layer = 0
            UI.block_selected = None

    UI.Update()
    pygame.display.flip()

def Quit() :
    pygame.quit()
    sys.exit()

    #Sauvegarde du fichier en cours de modification à implémenter ici

if __name__ == "__main__" :
    main()