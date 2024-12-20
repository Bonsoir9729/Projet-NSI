from gameobject import GameObject
from gravity import Gravity
from scene import Scene
from sprite import Sprite

class Game :

    aliocha = GameObject("Aliocha", scripts=[Gravity, Sprite])
    
    scene = Scene(aliocha)