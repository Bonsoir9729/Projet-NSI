from engine.gameobject import GameObject
class Script :
    parent:GameObject

    def __init__(self, parent:GameObject) -> None:
        self.parent = parent

    def Start(self) :
        pass

    def Update(self, deltaTime:float) :
        pass