"""
Example of a minimal class
"""


class Item:
    """
    Represents an item
    """

    def __new__(cls, name):
        """ 
        to override __new__() properly, it must return the new instance
        otherwise __init__ will not be called
        """
        print("first")
        instance = object.__new__(cls)
        return instance

    def __init__(self, name):
        """
        Initialization method, gets called after __new__() created new instance
        """
        self.name = name
        print("second")
        print(name)

    def __str__(self):
        """
        gets called by the print(instance) method. Anything that should be printed as
        representation of the class
        """
        return f"{self.name}"

    def __repr__(self):
        """
        gets called when as a representation of the instance itself
        Debuggers, mouseover, etc show this
        """
        return "Item Representation"


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Point"

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



def main():
    """
    Main method
    """
    item1 = Item("Name")
    print(item1)

    p1 = Point(1, 2)
    p2 = Point(-2, 1)
    print(p1 + p2)
    print(p1 - p2)
    print(p1 == p2)


if __name__ == "__main__":
    main()
