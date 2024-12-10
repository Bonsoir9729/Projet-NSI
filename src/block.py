class Block :
    """
    :param suivant: Block suivant, None si l'objet est une feuille
    :param imbrique: Block imbriqué, dans les block if par exemple
    """

    racinesBlocks = []

    def __init__(self, valeur:any) :
        self.suivant = None
        self.valeur = valeur
        Block.racinesBlocks.append(self)

    def EstFeuille(self) -> bool :
        return not self.suivant

    def EstRacine(self) -> bool :
        """
        ATTENTION : à ne pas abuser, O(nombre de racines)
        """
        for block in Block.racinesBlocks :
            if block == self :
                return True
        return False

    def Parent(self) -> object :
        """
        Retourne le parent du block s'il existe, sinon None
        ATTENTION : à ne pas abuser, O(nombre de blocks)
        """
        for block in Block.Get() :
            if block.EstParentDirect(self) :
                return block

    def EstParent(self, block:object) -> bool :
        """
        Un block est considéré comme son propre parent
        :return: True si self est le parent direct ou indirect de block
        """
        if self == block :
            return True
        if self.suivant :
            return self.suivant.EstParent(block)
        return False

    def EstParentDirect(self, block:object) -> bool : 
        """
        Un block n'est pas considéré comme son propre parent direct
        :return: True si self est le parent direct de block.
        """
        return self.suivant == block

    def Detacher(self,block:object) -> bool :
        """
        Détache un grand block en 2 blocks. Le deuxième block a pour racine le paramètre block. 
        :return: False si le block passé en argument n'est pas l'enfant direct de l'objet qui 
        appelle la fonction
        """
        if self.EstParentDirect(block) :
            block.parent = None
            Block.racinesBlocks.append(block)
            self.suivant = None
            return True
        return False

    def Attacher(self,block:object) -> None :
        """
        Attache le block passé en argument en bas du block qui appelle la fonction
        """
        if self.suivant :
            block.Feuille().suivant = self.suivant
        self.suivant = block

        #Remove the block from racinesBlock
        Block.racinesBlocks.remove(block)


    def Feuille(self) -> object :
        """
        Retourne la feuille du block, le block tout en bas
        """
        if self.EstFeuille() :
            return self
        return self.suivant.Feuille()

    def Enfants(self) -> list[object] :
        """
        Retourne la liste de tous les enfants du block, en s'incluant lui même
        """
        if not self.suivant :
            return [self]
        return [self] + self.suivant.Enfants()

    def Get() -> list[object] :
        """
        Retourne tous les blocks ordonnés par chaîne
        Les chaînes ne sont pas ordonnées
        """
        liste = []
        for block in Block.racinesBlocks :
            liste += block.Enfants()
        return liste