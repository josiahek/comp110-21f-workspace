"""Example of a point class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates multiple components by factor."""
        self.x *= factor
        self.y *= factor
 
    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Overload the addition operator."""
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else: 
            raise IndexError

    def __repr__(self) -> str:
        """Produce a str representation of a Point for python."""
        return f"Point({self.x}, {self.y})"


p0: Point = Point(1.0, 2.0)
p1: Point = p0 * 2.0
p2: Point = p0 + p1

print(f"a: {p0}")
print(f"b: {p1}")
print(f"c: {p2}")

print(p0[0])
print(p1[0])