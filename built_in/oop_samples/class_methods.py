"""
Example of class methods
"""


class Item:
    """
    Represents an Item
    """

    # class variable (all instances of the class have access)
    index = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def gen_item_type_a(cls, names):
        """
        classmethod has access to the class itself
        """
        # can instantiate the class
        for name in names:
            cls.index += 1
            yield cls(name)

    @classmethod
    def gen_item_type_b(cls, name):
        """
        classmethod has access to the class itself
        """
        # has access to class variables
        cls.index += 1
        # can instantiate the class
        return cls(name)

    @classmethod
    def gen_part(cls, name):
        """
        class method has also acces to a nested class
        """
        return cls.Part(name)

    class Part:
        """
        Nested class, represents a part of the item
        """
        def __init__(self, name):
            self.name = name


def main():
    """
    Main method
    """
    factory = Item.gen_item_type_a(["Item1A", "Item2A"])
    item1a = next(factory)
    item2a = next(factory)
    print(item1a.name)
    print(item2a.name)

    item1b = Item.gen_item_type_b("Item1B")
    item2b = Item.gen_item_type_b("Item2B")

    print(item1b.name)
    print(item2b.name)

    part = Item.gen_part("Part")
    print(part.name)

    print(Item.index)


if __name__ == "__main__":
    main()
