from script import Script
import pygame 

class Sprite(Script) :

    sprite:pygame.Surface

    def __init__(self, parent, spritepath:str="projet scratch/engine/scratch.png") :
        super().__init__(parent)
        if not pygame.get_init() :
            pygame.init()

        self.sprite = pygame.image.load(spritepath)

    def Update(self, deltaTime) :
        pygame.display.get_surface().blit(self.sprite, self.parent.position.coords())