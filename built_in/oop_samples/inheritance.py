"""
Example of a minimal class
"""


class Item:
    """
    Represents an item
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item"

    @classmethod
    def makeSubItemA(cls):
        return SubItemA()


class SubItemA(Item):
    """ Subitem A"""

    def __init__(self):
        super().__init__("ItemA")

    def __repr__(self):
        return "SubItemA"


class SubItemB(Item):
    """ Subitem B"""

    def __init__(self):
        super().__init__("ItemB")

    def __repr__(self):
        return "SubItemB"


def main():
    """
    Main method
    """
    subitem_a1 = Item.makeSubItemA()
    subitem_a2 = SubItemA()
    subitem_b1 = SubItemB()
    


if __name__ == "__main__":
    main()
