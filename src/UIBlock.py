import pygame
from block import Block
from const import *

class UIBlock(Block) :
    """
    :param size: sous la forme (longueur, hauteur). size n'est pas un attribut accessible de UIBlock
    """
    def __init__(self, size:tuple[int,int], coords:tuple[int,int]=(0,0), color:tuple[int,int,int]=DARK) -> None :
        super().__init__()
        self.width, self.height = size
        self.x, self.y = coords
        self.color = color
        self.layer = 0

    def Rect(self) -> pygame.Rect :
        """
        Permet d'obtenir un pygame.Rect du block pour l'afficher à l'écran
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def Overlap(self,margin:float=10) -> object :
        """
        Retourne le premier block supperposé (ou presque) avec
        """
        for block in UIBlock.Get() :
            rect = block.Rect()
            rect.h += margin
            rect.w += margin
            if not self == block and self.Rect().colliderect(rect) :
                return block

    def Get() -> list[object]:
        """
        Retourne tous les objets UIBlock ordonnés par chaîne
        Les chaînes ne sont pas ordonnées
        """
        liste = []
        for block in Block.Get() :
            if isinstance(block, UIBlock) :
                liste.append(block)
        return liste