import math # Need it for pi
from abc import ABC
from abc import abstractmethod

"""Creating the Shape class and passing the ABC class to inherit its @abtractmethod method"""

class Shape(ABC):
    """
    Blueprint class for all Shapes. All shapes need a name, area, and perimeter. 
    """

    def __init__(self, shape_name):
        self._name = shape_name # setting attibute name of shape

    """@property is used to call the name method like an attribute (shape.name) and prevents accidental modification of 
    the attribute outside the method
    """
    @property
    def name(self):
        return self._name

    """Child classes must provide an area and perimeter method specific to their shapes. We can use the @abstractmethod to 
    to achieve this 
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    """Format the ouput of print() when we print a shape"""
    def __str__(self):

        text = self.name + ", area: " + str(self.area()) + ", perimeter: " + str(self.perimeter())
        return text
    
    def draw(self):

        print(self.__str__())

class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, "Circle")
        self.radius = radius

    def area(self):
        circle_area = math.pi * self.radius * self.radius
        return circle_area

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        return circle_perimeter
    
class Square(Shape):

    def __init__(self, side):
        Shape.__init__(self, "Square")
        self.side = side

    def area(self):

        square_area = self.side * self.side
        return square_area
    
    def perimeter(self):

        square_perimeter = 4 * self.side
        return square_perimeter
    
class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self, "Rectangle")

        self.length = length
        self.width = width

    def area(self):

        rectangle_area = self.length * self.width
        return rectangle_area
    
    def perimeter(self):

        rectangle_perimeter = (2 * self.length) + (2 * self.width)
        return rectangle_perimeter
    

class Triangle(Shape):

    def __init__(self, sidea, sideb, sidec, height, base):
        Shape.__init__(self, "Triangle")

        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec
        self.base = base
        self.height = height

    def area(self):

        triangle_area = 0.5 * self.base * self.height
        return triangle_area
    
    def perimeter(self):

        triangle_perimeter = self.sidea + self.sideb + self.sidec
        return triangle_perimeter
        
