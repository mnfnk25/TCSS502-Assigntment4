"""
We'll create the DrawingProgramIterator class here. Its job is to allow us to
loop through the shapes stored in the DrawingProgram using a for loop.

"""

from typing import List
from shapes import Shape


class DrawingProgramIterator:
    """
    The iterator over a list of Shape objects.
    """

    def __init__(self, shapes: List[Shape]) -> None:
        """
        Initialize the iterator with a list of Shape objects 
        """
        self._shapes = shapes
        self._index = 0  # Start from the first element (index 0)

    def __iter__(self) -> "DrawingProgramIterator":
        """
        Allows the iterator to be used in a for loop.

        """
        return self

    def __next__(self) -> Shape:
        """
        Returns the next Shape in the list and advances the index.
        If we reach the end of the list, we raise StopIteration to signal
        to the for loop that iteration is complete.

        """

        # if index is past the end of the list, stop iterating
        if self._index >= len(self._shapes):
            raise StopIteration

        # get the current shape and advance the index
        item = self._shapes[self._index]
        self._index += 1
        return item
