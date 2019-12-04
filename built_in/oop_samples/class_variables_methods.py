"""
Example of class variables and methods
"""


class Item:
    """Represents an item"""

    # name of the item
    name = "Item"

    def get_name(self):
        """
        gets the name of the item
        
        return: (str) self.name: Name of the item
        """
        return self.name


def main():
    """Main method"""
    item1 = Item()
    print(item1.name)
    print(item1.get_name())


if __name__ == "__main__":
    main()
