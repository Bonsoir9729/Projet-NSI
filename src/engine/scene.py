from gameobject import GameObject

class Scene :

    gameObjects:list[GameObject]

    def __init__(self, *args) -> None :
        self.gameObjects = args

    def Add(self, gameObject:GameObject) :
        self.gameObjects.append(gameObject)

    def Start(self) -> None :
        for gameObject in self.gameObjects :
            gameObject.Start()

    def Update(self, deltaTime) -> None :
        for gameObject in self.gameObjects :
            gameObject.Update(deltaTime)