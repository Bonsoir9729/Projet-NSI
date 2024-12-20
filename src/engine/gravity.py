from script import Script
from vector import Vector

class Gravity(Script) :

    active:bool
    poids:float

    g = 9.81

    def __init__(self, parent, poids=1, active=True) -> None:
        super().__init__(parent)
        self.poids = poids
        self.active = active

    def TurnOn(self) -> None :
        self.active = True

    def TurnOff(self) -> None :
        self.active = False

    def Update(self, deltaTime:float) -> None:
        if self.active :
            self.parent.position += Vector.down * (self.g * deltaTime * self.poids)