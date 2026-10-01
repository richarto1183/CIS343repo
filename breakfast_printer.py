"""Student exercise: printing a breakfast syntax tree.

Implement __str__ in Crispiness, Cooked, Bacon, Sausage, Eggs, Bread, and
Breakfast so that print(breakfast) produces the menu text described by the
grammar. Return strings from these methods; do not print inside them.
Leave Node.__str__ as the base-class placeholder.

Run your completed solution with: python3 breakfast_printer.py
The example should print:
really really crispy bacon with scrambled eggs with toast on the side on the side
"""

from typing import Literal


class Node:
    """A syntax-tree node whose string is the menu text it represents."""

    def __str__(self):
        raise NotImplementedError


class Crispiness(Node):
    def __init__(self, more = None):
        self.more = more

    def __str__(self):
        return "really" if self.more is None else f"really {self.more}"


class Cooked(Node):
    def __init__(self, style: Literal["scrambled", "poached", "fried"]):
        self.style = style

    def __str__(self):
        return self.style


class Protein(Node):
    """Base class for the three protein productions."""


class Bacon(Protein):
    def __init__(self, crispiness):
        self.crispiness = crispiness

    def __str__(self):
        return str(self.crispiness) + " bacon"


class Sausage(Protein):
    def __str__(self):
        return "sausage"


class Eggs(Protein):
    def __init__(self, cooked):
        self.cooked = cooked

    def __str__(self):
        return str(self.cooked) + " eggs"


class Bread(Node):
    def __init__(self, kind: Literal["toast", "biscuits", "English muffin"]):
        self.kind = kind

    def __str__(self):
        return self.kind


class Breakfast(Node):
    def __init__(self, main, side = None):
        self.main = main
        self.side = side
        if self.side is not None and not isinstance(self.main, Protein):
            raise ValueError("Only a protein can have a breakfast on the side.")

    def __str__(self):
        if self.side is None:
            return str(self.main)
        else:
            return str(self.main) + " with " + str(self.side) + " on the side"


if __name__ == "__main__":
    breakfast = Breakfast(
        main=Bacon(Crispiness(Crispiness("crispy"))),
        side=Breakfast(
            main=Eggs(Cooked("scrambled")),
            side=Breakfast(Bread("toast")),
        ),
    )
    print(breakfast)
