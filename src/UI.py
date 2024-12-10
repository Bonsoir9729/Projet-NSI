from const import *
import pygame
from UIBlock import UIBlock

class UI :

    def Init() -> None :
        UI.block_selected = None
        UI.screen = pygame.display.get_surface()
        UI.mousepos = pygame.mouse.get_pos()

    def Update() -> None :
        screen = pygame.display.get_surface()
        screen.fill(BACKGROUND_COLOR)

        UI.mousepos = pygame.mouse.get_pos()

        UI.HandleBlockDragging()
        UI.Draw_Blocks()

    def Draw_Blocks() -> None :
        """
        Dessine les rectangles sur l'écran passé en argument
        """
        for block in sorted(UIBlock.Get(), key=lambda block : block.layer) :
            pygame.draw.rect(UI.screen, block.color, block.Rect())
            if block.suivant :
                block.suivant.x, block.suivant.y = block.x, block.y + block.height

    def HandleBlockDragging() -> None :
        """
        Le block selectionné suit la souris grâce à cette fonction
        """
        if not UI.block_selected :
            return

        # block_selected suit la souris
        UI.block_selected.x = UI.mousepos[0] + UI.mouseOffset[0]
        UI.block_selected.y = UI.mousepos[1] + UI.mouseOffset[1]
        if not UI.block_selected.EstRacine() :
            for block in UIBlock.Get() :
                if block.Detacher(UI.block_selected) :
                    return

    def HandleMouseButtonDown() -> None :
        """
        Appelée sur la première frame où la souris est cliquée.
        """
        UI.block_selected = UI.CollisionPoint(UI.mousepos)

        # Ne pas commencer à drag si aucune collision n'est detectée avec le curseur
        if not UI.block_selected :
            return

        UI.mouseOffset = (UI.block_selected.x - UI.mousepos[0], UI.block_selected.y - UI.mousepos[1])
        UI.block_selected.layer = 1

    def HandleMouseButtonUp() -> None :
        """
        Appelée sur la première frame où clic gauche est relaché.
        """

        #Si aucun block n'est selectionné, ne rien faire
        if not UI.block_selected :
            return

        overlap = UI.block_selected.Overlap()
        if overlap :
            if UI.block_selected.y < overlap.y :
                UI.block_selected.Attacher(overlap)
            else :
                overlap.Attacher(UI.block_selected)
        UI.block_selected.layer = 0
        UI.block_selected = None

    def CollisionPoint(point:tuple[int,int]) -> object :
        """
        :param point: Tuple sous la forme (x,y)
        Retourne le premier élement pour lequel une collision est détectée
        Retourne None si aucun n'objet n'est en collision avec le point
        """
        for block in sorted(UIBlock.Get(), key=lambda block : block.layer) :
            if block.Rect().collidepoint(point) :
                return block