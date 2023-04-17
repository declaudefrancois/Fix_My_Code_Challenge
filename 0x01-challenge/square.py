#!/usr/bin/python3
"""Square module.
"""


class Square():
    """
        Defines a squares.

        Attributes:
            width (int): the width
            height (int): the height
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instanciates a new square. """
        for key, value in kwargs.items():
            if key in ["width", "height"]:
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiterOfMySquare(self):
        """ Calculates and returns the square's perimeter. """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Returns a string representationof the sqare. """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterOfMySquare())
