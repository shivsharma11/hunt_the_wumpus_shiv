class Classroom:
    def __init__(self, name):
        self.name = name
        self.item = None
        self.description = ""
        self.linked_classrooms = {}
        self.character = None
    
    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f"\nYou are in: {self.name}")
        print(self.description)
        if self.item:
            print("You see a", self.item.get_name())

    def set_link_classroom(self, classroom, direction):
        self.linked_classrooms[direction] = classroom

    def move(self, direction):
        if direction in self.linked_classrooms:
            return self.linked_classrooms[direction]
        else:
            print("You can't go that way.")
            return self

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character
