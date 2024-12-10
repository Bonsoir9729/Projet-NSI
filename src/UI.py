from const import *
import pygame
from UIBlock import UIBlock

class UI :

    block_selected = None

    def Init() -> None :
        pass

    def Update() -> None :
        screen = pygame.display.get_surface()
        screen.fill(BLACK)

        UI.HandleBlockDragging()

        UI.Draw_Blocks(screen)

    def Draw_Blocks(screen:pygame.Surface) -> None :
        """
        Dessine les rectangles su l'écran passé en argument
        """
        for block in sorted(UIBlock.Get(), key=lambda block : block.layer) :
            pygame.draw.rect(screen, block.color, block.Rect())
            if block.suivant :
                block.suivant.x, block.suivant.y = block.x, block.y + block.height

    def HandleBlockDragging() -> None :
        """
        Le block selectionné suit la souris grâce à cette fonction
        """
        if not UI.block_selected :
            return

        # block_selected suit la souris
        x, y = pygame.mouse.get_pos()
        dx, dy = pygame.mouse.get_rel()
        UI.block_selected.x, UI.block_selected.y = x - dx, y - dy
        if not UI.block_selected.EstRacine() :
            for block in UIBlock.Get() :
                if block.Detacher(UI.block_selected) :
                    return

    def CollisionPoint(point:tuple[int,int]) -> object :
        """
        :param point: Tuple sous la forme (x,y)
        Retourne le premier élement pour lequel une collision est détectée
        Retourne None si aucun n'objet n'est en collision avec le point
        """
        for block in sorted(UIBlock.Get(), key=lambda block : block.layer) :
            if block.Rect().collidepoint(point) :
                return block