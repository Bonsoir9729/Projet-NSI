import math

class Vector :

    x:float
    y:float

    def __init__(self, x:float, y:float) -> None :
        self.x, self.y = x, y

    def NormSquared(self) -> float:
        return self.x**2 + self.y**2

    def Norm(self) -> float:
        return round(math.sqrt(self.NormSquared()),10)

    def Rotate(self, angle:float) -> object:
        """
        :param angle: angle en degré
        Tourne le vecteur dans le sens horaire
        """
        angle = -angle*math.pi/180
        return Vector(
            round((math.cos(angle)*self.x)-(math.sin(angle)*self.y),10),
            round((math.sin(angle)*self.x)+(math.cos(angle)*self.y),10)
        )

    def coords(self) -> tuple[int,int] :
        return (self.x, self.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, obj:any) -> object :
        if isinstance(obj, Vector) :
            return Vector(self.x+obj.x, self.y+obj.y)
        raise TypeError(f'Trying to add Vector and {type(obj).__name__}.')

    def __sub__(self, obj:any) -> object :
        if isinstance(obj, Vector) :
            return Vector(self.x-obj.x, self.y-obj.y)
        raise TypeError(f'Trying to substract Vector and {type(obj).__name__}.')

    def __mul__(self, k:float) -> object :
        if type(k) == float or type(k) == int :
            return Vector(k*self.x, k*self.y)
        raise TypeError(f'Trying to multiply Vector and {type(k).__name__}.')


Vector.zero = Vector(0,0)
Vector.right = Vector(1,0)
Vector.left = Vector(-1,0)
Vector.up = Vector(0,1)
Vector.down = Vector(0,-1)