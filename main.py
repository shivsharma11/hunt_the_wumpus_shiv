from character import Character, Teacher
from cave import Classroom

dead = False

# Create caves
cavern = Classroom("Cavern")
grotto = Classroom("Grotto")
dungeon = Classroom("Dungeon")

# Descriptions
cavern.set_description("A dark and dirty cavern")
grotto.set_description("A small cave with ancient markings")
dungeon.set_description("A large cave with a rack")

# Links
cavern.set_link_classroom(dungeon, "south")
dungeon.set_link_classroom(cavern, "north")
dungeon.set_link_classroom(grotto, "west")
grotto.set_link_classroom(dungeon, "east")

# Enemy
harry = Teacher("Harry", "A hairy, smelly wumpus")
dungeon.set_character(harry)

harry.set_conversation("Come closer... I can't see you.")
harry.set_weakness("aura")

current_cave = cavern

while not dead:

    print()
    current_cave.describe()

    inhabitant = current_cave.get_character()

    if inhabitant:
        inhabitant.describe()

    command = input("> ").lower()

    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)

    elif command == "talk":

        if inhabitant:
            inhabitant.talk()
        else:
            print("There is nobody here.")

    elif command == "fight":
        if inhabitant and isinstance(inhabitant, Teacher):
            fight_with = input("What will you fight with? ")
            if inhabitant.fight(fight_with):
                print("You won!")
                current_cave.set_character(None)
            else:
                print("Game over")
                dead = True
        else:
            print("There is nobody to fight.")
    else:
        print("Invalid command.")