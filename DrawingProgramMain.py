from drawing_program import DrawingProgram
from ShapeFactory import ShapeFactory

class DrawingProgramMain:
  """ This is the main class to run the Drawing Program """
  @staticmethod
  def run_program():
    """ runs shape management """
    print("| DRAWING PROGRAM |")
    
    print("\nPart One: initialize the program")
    program = DrawingProgram()
    print("DrawingProgram initialized")
    print(program)

    print("\nPart Two: add shapes with ShapeFactory")
    triangle_a = ShapeFactory.create_triangle(sidea=30, sideb=40, sidec=50, height=40, base=30)
    rectangle_a = ShapeFactory.create_rectangle(length=50.0, width=20.0)
    square_a = ShapeFactory.create_square(side=30.0)
    circle_a = ShapeFactory.create_circle(radius=10.0)

    program.add_shape(triangle_a)
    program.add_shape(rectangle_a)
    program.add_shape(square_a)
    program.add_shape(circle_a)

    print(f"Shapes added. Current shape list:\n{program}")

    print("\nPart Three: sort the shapes")
    program.sort_shapes()
    print(f"Updated shape list after sorting:\n{program}")

    print("\nPart Four: add shapes")
    square_b = ShapeFactory.create_square(side=45.0)
    circle_b = ShapeFactory.create_circle(radius=5.0)

    program.add_shape(square_b)
    program.add_shape(circle_b)

    print("\nPart Five: replace a shape")
    replace_index = 0
    old_shape = program.get_shape(replace_index)
    new_circle = ShapeFactory.create_circle(radius=60.0)
    program.set_shape(replace_index, new_circle)
    print(f"Updated list after replacement circle added:\n{program}")

    print("\nPart Six: print a shape")
    program.print_shape(triangle_a)

    print("\nPart Seven: remove a shape")
    program.remove_shape(rectangle_a)
    print(f"Updated list after rectangle_a was removed:\n{program}")

    print("\nPart Eight: iterator")
    iterator_list = []
    for shape in program:
      iterator_list.append(shape.name)
    
    print(f"Final print of shapes from iterator: {', '.join(iterator_list)}")

if __name__ == "__main__":
  DrawingProgramMain.run_program()
