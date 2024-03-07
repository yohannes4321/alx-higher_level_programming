#!/usr/bin/python3
from models.rectangle import Rectangle
"""Importing Rectangle"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """INHERITANCE from Rectangle; there """
        """is no width and height in Square"""
        """super(). class must be replaced by size"""
        """self.size = size"""
        super().__init__(size, size, x, y, id)
        """k"""
        self.size = size
    """__str__"""
    def __str__(self):
        """str"""
        return f"[Square] ({self.id}) {self.x} / {self.y} - {self.size}"
