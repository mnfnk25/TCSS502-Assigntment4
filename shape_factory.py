"""
The shape factory is required to create all shapes. 

"""

from shapes import Circle
from shapes import Square
from shapes import Rectangle
from shapes import Triangle

class ShapeFactory:
    """ 
    This class will create all the shapes. Abstraction will be used to prevent the shape function to be called elsewhere
    """

    @staticmethod
    def create_shape(shape_name, *data):
        """
        Manufacture shapes based on the name and assigns the values passed.  Calls the shape functions to create the shape. 

        """
        # convert to lowercase for conveniance. 
        name = shape_name.lower()

        #Fabricate Circle
        if name == "circle":
            radius = data[0]
            return Circle(radius)
        
        #Fabricate Square
        if name == "square":
            side = data[0]
            return Square(side)
        
        #Fabricate Rectangle
        if name == "rectangle":
            length = data[0]
            width = data[1]
            return Rectangle(length, width)
        
        #Fabricate Triangle
        if name == "triangle":
            sidea = data[0]
            sideb = data[1]
            sidec = data[2]
            height =  data[3]
            base = data[4]
            return Triangle(sidea, sideb, sidec, height, base)
        
        #Edge case: Unkown figure

        print("Shape not recognized:", shape_name)
        return None
            
