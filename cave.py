"""Cave class"""
class Cave:
    """Defines the cave class"""
    def __init__(self, cave_name):
        """Cave class attributes"""
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None

    def set_description(self, cave_description):
        """Sets cave description"""
        self.description = cave_description

    def get_description(self):
        """Gets cave description"""
        return self.description
    
    def set_name(self, cave_name):
        """Sets cave name"""
        self.name = cave_name

    def get_name(self):
        """Gets cave name"""
        return self.name

    def set_link_caves(self, cave_to_link, direction):
        """Sets cave linking"""
        self.linked_caves[direction] = cave_to_link
    
    def get_link_caves(self):
        """Gets cave links"""
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)

    def set_character(self, new_character):
        '''Sets characters in caves'''
        self.character = new_character

    def get_character(self):
        '''Returns character in cave'''
        return self.character


    def move(self, direction):
        """Allows player to move between caves"""
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You cant go that way")
            return self
    
    def describe(self):
        """Organises outputs for the main loop"""
        print(self.description)
        self.get_link_caves()
