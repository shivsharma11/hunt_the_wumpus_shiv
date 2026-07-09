class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print(self.name)
        print(self.description)

    def get_name(self):
        return self.name