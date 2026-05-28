"""Main game loop"""
from cave import Cave

# Instantiate the cave objects
cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")

# Set the cave descriptions
cavern.set_description("A dark and dirty cavern")
grotto.set_description("A small cave with ancient markings")
dungeon.set_description("A large carve with a rack.")

# Set links between caves
cavern.set_link_caves(dungeon, "south")
dungeon.set_link_caves(cavern, "north")
dungeon.set_link_caves(grotto, "west")
grotto.set_link_caves(dungeon, "east")

# Main game loop
current_cave = cavern
while True:
    print("\n")
    current_cave.describe()
    command = input("> ")
    current_cave = current_cave.move(command)
