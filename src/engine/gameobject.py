from vector import Vector
from script import Script

class GameObject :

    name:str
    position:Vector
    scripts:list[Script]

    def __init__(self, name="New GameObject", startpos=Vector.zero, scripts=[]) :
        self.name = name
        self.position = startpos
        self.scripts = [script(self) for script in scripts]
        for script in self.scripts :
            assert isinstance(script, Script)

    def Start(self) :
        for script in self.scripts :
            script.Start()

    def Update(self, deltaTime) :
        for script in self.scripts :
            script.Update(deltaTime)