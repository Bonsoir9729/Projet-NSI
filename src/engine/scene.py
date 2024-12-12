from engine.gameobject import GameObject

class Scene :

    gameObjects:list[GameObject]

    def __init__(self) -> None :
        self.gameObjects = []

    def Add(self, gameObject:GameObject) :
        self.gameObjects.append(gameObject)

    def Start(self) :
        for gameObject in self.gameObjects :
            gameObject.Start()

    def Update(self, deltaTime) :
        for gameObject in self.gameObjects :
            gameObject.Update(deltaTime)

