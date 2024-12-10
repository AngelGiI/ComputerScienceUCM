from math import sqrt, pi
from copy import deepcopy as dcopy

class Vector(object):
    """This class reperesents a 2D vector
    Attributes
    ---------
    x,y: x-coordinate, y-coordinate
    """
    def __init__(self, px:float, py:float):
        """
        Constructor
        """
        self.x:float = px
        self.y:float = py
    def __str__(self)->str:
        """
        This method returns str representation of the Vector
        """
        return 'Vector(́{0:.2f}, {1:.2f})'.format(self.x, self.y)

class Point(object):
    """
    Point class. It represents 2D points.
    """
    def __init__(self, px, py):
        """
        Constructor
        Parameters
        ----------
        px: x-coordinate
        py: y-coordinate
        """
        self.x:float = px
        self.y:float = py
    def __str__(self)->str:
        """
        This method returns str representation of a Point
        """
        return f'Point(́{self.x:.2f}, {self.y:.2f})'
    def distance(self, other)->float:
        """
        This function returns the distance from this object to other
        """
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    def move(self, v:Vector):
        """
        This function move this point applying the vector v
        """
        self.x = self.x + v.x
        self.y = self.y + v.y
        
    
class Circle(object):
    """
    Class to represents a circle.
    """
    def __init__(self, center:Point, radius:float):
        """
        Constuctor
        Parameters:
        center: center of the circle
        radius: radius of the circle
        8
        """
        self.center:Point = center
        self.radius:float = radius
    def __str__(self)->str:
        return f'Circle({self.center}, {self.radius:.2f})'
    def surface(self)->float:
        """
        This function returns the surface of the circle
        """
        return pi*self.radius**2
    def move(self, v:Vector):
        """
        This funciton move the Circle applying vector v
        """
        self.center.move(v)
        
class Recta(object):
    """
    Class to represent a line.
    """
    def __init__(self, pendiente:float, altura:float):
        """
        Constuctor
        Parameters:
        pendiente: pendiente de la recta
        altura: coeficiente de posición de la rect
        """
        self.m:float = pendiente
        self.n:float = altura
        
    def __str__(self)->str:
        return 'Recta(y={0:.2f}x+{1:.2f})'.format(self.m, self.n)
    
    def distancePtoR(self, p:Point)->float:
        """
        This function returns the distance from a point to a line
        """
        if abs(p.y - p.x*self.n - self.m) < 10.0**(-5):
            return 0.0
        else:
            return (abs(self.m*p.x-p.y+self.n)/sqrt(1+self.m**2))
                 
    def distanceRtoR(self,other)->float:
        if self.m == other.m:
            if abs(self.n - other.n) < 10.0**(-5):
                return 0.0
            else:
                return (abs(-other.n+self.n)/sqrt(1+self.m**2))
        else:
            return 0.0
        
class Vector(object):
    """This class reperesents a 2D vector
    Attributes
    ---------
    x,y: x-coordinate, y-coordinate
    """
    def __init__(self, px:float, py:float):
        """
        Constructor
        """
        self.x:float = px
        self.y:float = py
    def __str__(self)->str:
        """
        This method returns str representation of the Vector
        """
        return 'Vector(́{0:.2f}, {1:.2f})'.format(self.x, self.y)

class Point(object):
    """
    Point class. It represents 2D points.
    """
    def __init__(self, px, py):
        """
        Constructor
        Parameters
        ----------
        px: x-coordinate
        py: y-coordinate
        """
        self.x:float = px
        self.y:float = py
    def __str__(self)->str:
        """
        This method returns str representation of a Point
        """
        return f'Point(́{self.x:.2f}, {self.y:.2f})'
    def distance(self, other)->float:
        """
        This function returns the distance from this object to other
        """
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    def move(self, v:Vector):
        """
        This function move this point applying the vector v
        """
        self.x = self.x + v.x
        self.y = self.y + v.y
        
    def distanceRtoP(self, r:Recta)->float:
        """
        This function returns the distance from a point to a line
        """
        if abs(self.y - self.x*r.n - r.m) < 10.0**(-5):
            return 0.0
        else:
            return (abs(r.m*self.x-self.y+r.n)/sqrt(1+r.m**2))