"""ITEM CLASS"""


class Item:
    """Defines an item."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        print(self.name)
        print(self.description)