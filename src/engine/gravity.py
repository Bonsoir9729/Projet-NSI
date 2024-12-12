from script import Script
from vector import Vector

class Gravity(Script) :
    active:bool
    g:float

    def __init__(self, parent, g=9.81) -> None:
        super().__init__(parent)
        self.active = True
        self.g = g

    def TurnOn(self) -> None :
        self.active = True

    def TurnOff(self) -> None :
        self.active = False

    def Update(self, deltaTime:float) -> None:
        if self.active :
            self.parent.position += Vector.down * (self.g * deltaTime)