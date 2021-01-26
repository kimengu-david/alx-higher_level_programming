#!/usr/bin/python3
"""
This module defines the rectangle class

"""

from models.base import Base


class Rectangle(Base):
    """Class denotes a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle properties"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for the width"""
        return self.__width

    @property
    def height(self):
        """getter method for the height"""
        return self.__height

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """Setter method for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
