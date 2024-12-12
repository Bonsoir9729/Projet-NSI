from engine.vector import Vector
from script import Script

class GameObject :

    position:Vector
    scripts:list[Script]

    def __init__(self, position=Vector.zero) :
        self.position = position
        self.scripts = []

    def Start(self) :
        for script in self.scripts :
            script.Start()

    def Update(self, deltaTime) :
        for script in self.scripts :
            script.Update(deltaTime)