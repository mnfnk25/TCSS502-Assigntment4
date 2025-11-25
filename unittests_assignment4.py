"""
This file create unit tests of all the classes and methods for assignment 4     
"""

import unittest # We import the unittest, python's built in testing functions
import math # we will need that pie

# Importing all the classes and methods we are going to test
from shapes import Circle,  Square, Rectangle, Triangle
from ShapeFactory import ShapeFactory
from drawing_program import DrawingProgram
from drawing_program_iterator import DrawingProgramIterator

# First we'll test the Shapes class. We need to compare the Area and Perimeter's value of the share we create for the test with a predefined value. 
# Reference for this tests come from the class slides and https://docs.python.org/3/library/unittest.html
class ShapesTest(unittest.TestCase):
    def test_circle(self):
        circle = Circle(5)
        predefined_area = math.pi * 5 * 5
        predefined_perimeter = 2 * math.pi * 5
        #We use almost equial because we're working with floats. 
        self.assertAlmostEqual(circle.area(), predefined_area)
        self.assertAlmostEqual(circle.perimeter(), predefined_perimeter)

    def test_Square(self):
        square = Square(5)
        predefined_area = 5 * 5
        predefined_perimeter = 4 * 5
        #We use assertequial because we're not working with floats
        self.assertEqual(square.area(), predefined_area)
        self.assertEqual(square.perimeter(), predefined_perimeter)

    def test_Rectangle(self):
        rectangle = Rectangle(5, 10)
        predefined_area = 5 * 10
        predefined_perimeter = 2 * (10 + 5)

        self.assertEqual(rectangle.area(), predefined_area)
        self.assertEqual(rectangle.perimeter(), predefined_perimeter)

    def test_Triangle(self):
        triangle = Triangle(10, 10, 20, 15, 20) # s1, s2, s3, height, base
        predefined_area = 0.5 * 20 * 15
        predefined_perimeter = 10 + 10 + 20

        self.assertEqual(triangle.area(), predefined_area)
        self.assertEqual(triangle.perimeter(), predefined_perimeter)

    #Test getting the name of the shape and the @property decorator
    def test_name(self):
        square = Square(10)
        self.assertEqual(square.name, "Square")

"""
Now testing the shape factory class and methods. We will create an instance of each shape and verify if the returned value is an instance 
of that same shape.         
"""

class TestShapeFactory(unittest.TestCase):
    def test_circle(self):
        circle = ShapeFactory.create_circle(5)
        self.assertIsInstance(circle, Circle)

    def test_square(self):
        square = ShapeFactory.create_square(5)
        self.assertIsInstance(square, Square)

    def test_rectangle(self):
        rectangle = ShapeFactory.create_rectangle(5, 10)
        self.assertIsInstance(rectangle, Rectangle)

    def test_trianlgle(self):
        triangle = ShapeFactory.create_triangle(10, 10, 20, 15, 20)
        self.assertIsInstance(triangle, Triangle)

""" 
Now we'll test the DrawingProgram class and methods. 
"""
class TestDrawingProgram(unittest.TestCase):

#Testing adding a shape. We'll peek at the first  index of the list and compare it to the share we drawed. 

    def test_add(self):
        draw_program = DrawingProgram() #create the drawing_program instance
        circle = Circle(5) # Create a circle
        draw_program.add_shape(circle) # add the circle to the list
        self.assertEqual(draw_program.get_shape(0), circle) # check if the share at index 0 is the same as the circle we added.

    def test_remove(self):

        draw_program = DrawingProgram() #create the drawing_program instance
        square1 = Square(10) # Create a square
        circle1 = Circle(5) # Create a circle

        draw_program.add_shape(square1) # add the square to the list
        draw_program.add_shape(circle1) # add the circle to the list

        remove = draw_program.remove_shape(square1)
        self.assertEqual(remove, 1)

    def test_set(self):

        draw_program = DrawingProgram() 
        square1 = Square(10) # Creating two shapes. We'll add square1 first, and then circle1 at index 0 and see if circle1 was set at index 0
        circle1 = Circle(5)
        draw_program.add_shape(square1)
        draw_program.set_shape(0, circle1)

        self.assertEqual(draw_program.get_shape(0), circle1) #Checking if the set_shape method put the circle shape at index 0

# Sorting ddge case: Testing empty lists. The draw program should return an empy list

    def test_sort_empty(self):
        draw_program = DrawingProgram()
        #we have an empty list at this point
        draw_program.sort_shapes()
        self.assertEqual(len(draw_program.shapes), 0)

# Test a list with one shape
    def test_sort_one(self):
        
        draw_program = DrawingProgram()
        circle1 = Circle(1)
        draw_program.add_shape(circle1)
        draw_program.sort_shapes()
        self.assertEqual(draw_program.get_shape(0), circle1)

# Test multiple shapes

    def test_sort_multiple(self):
        draw_program = DrawingProgram()
        circle_big = Circle(20)
        circle_medium = Circle(10)
        circle_small = Circle(5)

        draw_program.add_shape(circle_small)
        draw_program.add_shape(circle_medium)
        draw_program.add_shape(circle_big)

        draw_program.sort_shapes()

        self.assertEqual(draw_program.get_shape(0), circle_small)
        self.assertEqual(draw_program.get_shape(1), circle_medium)
        self.assertEqual(draw_program.get_shape(2), circle_big)

""" 
Testing the iterator
"""
class TestIterator(unittest.TestCase):

    #testing the iterator on an empty list

    def test_iterator_empty(self):
        draw_program = DrawingProgram()
        #we have an empty list now
        count = []
        # now we invoke the iterator
        for shape in draw_program:
            count.append(shape)

        self.assertEqual(count, []) # COMPARE AGAINST AN EMPTY LIST HERE AND NOT ZERO!!!! 

    def test_iterator_one(self):
        draw_program = DrawingProgram()
        #initialized our list
        circle = Circle(5)
        draw_program.add_shape(circle)
        
        count = []

        for shape in draw_program:
            count.append(shape)

        self.assertEqual(count, [circle]) # compare the internal list in the draw program with the external list with the object circle in it

    def test_iterator_multiple(self):
        draw_program =  DrawingProgram()

        square1 = Square(5)
        square2 = Square(6)
        square3 = Square(7)
        square4 = Square(8)
        square5 = Square(9)

        draw_program.add_shape(square1)
        draw_program.add_shape(square2)
        draw_program.add_shape(square3)
        draw_program.add_shape(square4)
        draw_program.add_shape(square5)

        count = []

        for shape in draw_program:
            count.append(shape)

        self.assertEqual(count, [square1, square2, square3, square4, square5])

unittest.main()