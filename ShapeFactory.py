from shapes import Circle, Square, Rectangle, Triangle

class ShapeFactory():
  """ The Shape Factory contains individual static methods which create shapes within the program """

  @staticmethod
  def create_circle(radius):
    """ creates and returns a circle """
    return Circle(radius)

  @staticmethod
  def create_square(side):
    """ creates and returns a square """
    return Square(side)

  @staticmethod
  def create_rectangle(length, width):
    """ creates and returns a rectangle object """
    return Rectangle(length, width)

  @staticmethod
  def create_triangle(sidea, sideb, sidec, height, base):
    """ creates and returns a triangle object """
    return Triangle(sidea, sideb, sidec, height, base)