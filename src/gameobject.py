from vector import Vector

class GameObject :

    position:Vector

    def __init__(self, position=Vector.zero) :
        self.position = position

    def Update(self) :
        pass