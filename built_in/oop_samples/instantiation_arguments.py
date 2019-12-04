"""
Example for instatiating a class with variables
"""


class Item:
    """Represents an item"""

    def __init__(self, name, *args, **kwarfs):
        """
        name: (str) name of the item
        """
        self.name = name

    def get_name(self):
        """
        gets the name of the item
        
        return: (str) self.name: Name of the item
        """
        return self.name


def main():
    """Main method"""
    item1 = Item("Item1")
    print(item1.name)
    print(item1.get_name())


if __name__ == "__main__":
    main()
