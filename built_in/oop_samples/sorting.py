# -*- coding: utf-8 -*-

class Color:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"{self.name}, {self.code}"

    def __lt__(self, other):
        return self.name < other.name


black = Color("Black", "#000000")
white = Color("White", "#FFFFFF")
red = Color("Red", "#FF0000")

colors = [black, white, red]

colors.sort()

print(colors)
