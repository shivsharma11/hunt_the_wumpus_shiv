from character import Character, Enemy 
from cave import Cave 

dead = False
# Instantiate the cave objects
cavern = Cave("Cavern") 
grotto = Cave("Grotto") 
dungeon = Cave("Dungeon") 

# Set the cave descriptions
cavern.set_description("A dark and dirty cavern") 
grotto.set_description("A small cave with ancient markings") 
dungeon.set_description("A large cave with a rack") 

# Set links between caves 
cavern.set_link_caves(dungeon, "south") 
dungeon.set_link_caves(cavern, "north") 
dungeon.set_link_caves(grotto, "west") 
grotto.set_link_caves(dungeon, "east") 

# Instantiate Enemy and add to cave
harry = Enemy("Harry", "A hairy, smelly wumpus") 
dungeon.set_character(harry) 
harry.set_conversation("Come closer... I can't see you.") 
harry.set_weakness("aura")

# Main game loop
current_cave = cavern 

while dead == False:
    print("\n")
    current_cave.describe()
    
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        
    command = input("> ").lower()
    
    if command in ["north", "east", "south", "west"]:
        current_cave = current_cave.move(command)
        
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is nobody here to talk to.")
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            fight_with = input("What will you fight with? ")
            if inhabitant.fight(fight_with) is True:
                print("You won the fight!")
                current_cave.set_character(None)
            else:
                print("Scurry home, you lost the battle.")
                print("Game over")
                dead = True
        else:
            print("You lost the fight.")
    else:
        print("There is nobody to fight with.")
