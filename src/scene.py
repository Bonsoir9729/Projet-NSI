from gameobject import GameObject

class Scene :

    objects:list[Object]

    def __init__(self) -> None :
        self.objects = []

    def Add(self, obj:Object) :
        self.objects.append(obj)

