"""
We'll create the drawing program class here. We need to create methods to add, remove, print, sort, and
access shapes. It also has an iterator class to loop through the shapes in the list. 

"""

from ShapeFactory import ShapeFactory
from shapes import Shape
from drawing_program_iterator import DrawingProgramIterator

class DrawingProgram:
    """ 
    The class will have a list of shapes and provide add, remove, print, and sort shapes 
    """
    def __init__(self, initial_shapes=None):
        """Constructor method. We will pass shapes or None """

        if initial_shapes is None:
            self.shapes = [] # edge case. Empty list when no shapes are passed.

        else:
            self.shapes = initial_shapes

    def add_shape(self, shape):
        """
        Adds a shape to the list. 

        """
        self.shapes.append(shape)
    
    def remove_shape(self, shape_to_remove):
        """
        Removes shapes that match the type passed. 
        
        """

        removed_count = 0 # we will return the number of shapes removed
        new_list = [] #we will construct a new list of shapes that weren't removed

        for shape in self.shapes:
            """
            We will compare the type of the shape passed against our list of shapes. If the type matches we will increase the 
            our counter. This loop will add only the shapes that don't match the type we need to remove to a new list.  
            """
            if type(shape) is type(shape_to_remove):
                removed_count = removed_count + 1

            else:
                new_list.append(shape)

        #We will replace the old shapes list with the new shapes list
        self.shapes = new_list

        return removed_count
    
    def print_shape(self, target_shape):
        """
        Prints the shape that matches the shape passed. 

        """
        for shape in self.shapes:
            if type(shape) is type(target_shape):
                print(shape)

    def sort_shapes(self):
        """ 
        This method sorts the shapes in the list by alphabetical order first and by area is the names match
        """

        """Create a key:value tuple from the shape passed in and use the sorted funcion:
        #https://www.w3schools.com/python/ref_func_sorted.asp
        """
        def sorting_hat(shape):
            return (shape.name, shape.area()) #sorted will call this function as a key
        
        self.shapes = sorted(self.shapes, key=sorting_hat)

    def get_shape(self, index):
        """
        Returns the shape at the specified index

        """
        return self.shapes[index]
    
    def set_shape(self, index, add_shape):
        """
        Replaces the shape at the specified index with the passed shape

        """
        self.shapes[index] = add_shape

    def __str__(self):
        """
        Format the output of the print function with each shape separated by a new line
        """
        string = ""

        for shape in self.shapes:
            string = string + str(shape) + "\n"

        return string
    
    def __iter__(self):
        """
        Function to loop over all shapes using a foor loop
    
        """
        return DrawingProgramIterator(self.shapes)