class Classroom:
    """Defines the classroom class"""

    def __init__(self, classroom_name):
        """Classroom attributes"""
        self.name = classroom_name
        self.description = None
        self.linked_classrooms = {}
        self.character = None

    def set_description(self, classroom_description):
        """Sets classroom description"""
        self.description = classroom_description

    def get_description(self):
        """Gets classroom description"""
        return self.description
    
    def set_name(self, classroom_name):
        """Sets classroom name"""
        self.name = classroom_name

    def get_name(self):
        """Gets classroom name"""
        return self.name

    def set_link_classroom(self, classroom_to_link, direction):
        """Links this classroom to another classroom"""
        self.linked_classrooms[direction] = classroom_to_link
    
    def get_link_classroom(self):
        """Displays linked classrooms"""
        for direction, classroom in self.linked_classrooms.items():
            print("The " + classroom.get_name() + " is " + direction)

    def set_character(self, new_character):
        """Places a character in the classroom"""
        self.character = new_character

    def get_character(self):
        """Returns the character in the classroom"""
        return self.character

    def move(self, direction):
        """Allows player to move between classrooms"""
        if direction in self.linked_classrooms:
            return self.linked_classrooms[direction]
        else:
            print("You can't go that way")
            return self
    
    def describe(self):
        """Organises outputs for the main loop"""
        print(self.description)
        self.get_link_classroom()

