"""CLASSROOM CLASS"""


class Classroom:

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.linked_classrooms = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def describe(self):

        print("\n" + "=" * 50)
        print("location:", self.name.lower())
        print("=" * 50)

        print(self.description)

        if self.character:

          print("\nperson")
          print("------")
          print(self.character.name)

        if self.item:

            print("\nitem")
            print("----")
            print(self.item.get_name())

            print("\nexits")
            print("-----")

        for direction in self.linked_classrooms:
            print(direction)

    def set_link_classroom(self, classroom, direction):
        self.linked_classrooms[direction] = classroom

    def move(self, direction):

        if direction in self.linked_classrooms:
            return self.linked_classrooms[direction]

        print("You can't go that way.")
        return self

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item