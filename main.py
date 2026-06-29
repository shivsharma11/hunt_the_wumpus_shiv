from character import Character, Teacher
from cave import Classroom

dead = False

# Create rooms

#BASIC ROOMS
math_room = Classroom("Mathematics")
english_room = Classroom("English")
science_room = Classroom("Science")
hall = Classroom("Hall")
entrance = Classroom("Entrance")
hall = Classroom("Hall")
principal_office = Classroom("Principal's Office")
exit_room = Classroom("Exit")

#Non-classroom rooms
cafe = Classroom("Cafe")
canteen = Classroom("Canteen")
library = Classroom("Library")

#Science labs & computer lab 
computer_lab = Classroom("Computer Lab")
biology = Classroom("Biology")
physics = Classroom("Physics")
chemistry = Classroom("Chemistry")

#Maths Wing (Upper Level)
mathematics = Classroom("Mathematics")
m_faculty1 = Classroom("M. Faculty 1")
m_faculty2 = Classroom("M. Faculty 2")

#English Wing (Lower Level)
english = Classroom("English")
hsie = Classroom("HSIE")

#Pe Wing (outdoors)
pe1 = Classroom("PE 1")
pe2 = Classroom("PE 2")

#Other rooms (misc.)
oval = Classroom("Oval")
detention = Classroom("Detention")


# Descriptions
hall.set_description("Hall - Students everywhere.")
math_room.set_description("Math room-  on the blackboards.")
english_room.set_description("A small cave with ancient markings")
science_room.set_description("A large cave with a rack")


# Links
math_room.set_link_classroom(math_room, "south")
english_room.set_link_classroom(english_room, "north")
science_room.set_link_classroom(science_room, "west")
science_room.set_link_classroom(math_room, "east")
entrance.set_link_classroom(hall, "north")
hall.set_link_classroom(entrance, "south")
hall.set_link_classroom(principal_office, "north")
hall.set_link_classroom(cafe, "west")
hall.set_link_classroom(canteen, "east")
hall.set_link_classroom(library, "south")
principal_office.set_link_classroom(exit_room, "north")
exit_room.set_link_classroom(principal_office, "south")
hall.set_link_classroom(computer_lab, "northeast")
computer_lab.set_link_classroom(hall, "southwest")

#Science Wing
computer_lab.set_link_classroom(biology, "east")
biology.set_link_classroom(computer_lab, "west")

biology.set_link_classroom(physics, "south")
physics.set_link_classroom(biology, "north")

physics.set_link_classroom(chemistry, "west")
chemistry.set_link_classroom(physics, "east")

hall.set_link_classroom(mathematics, "northwest")
mathematics.set_link_classroom(hall, "southeast")

mathematics.set_link_classroom(m_faculty1, "west")
m_faculty1.set_link_classroom(mathematics, "east")

m_faculty1.set_link_classroom(m_faculty2, "south")
m_faculty2.set_link_classroom(m_faculty1, "north")

hall.set_link_classroom(english, "southeast")
english.set_link_classroom(hall, "northwest")

english.set_link_classroom(hsie, "south")
hsie.set_link_classroom(english, "north")

hsie.set_link_classroom(pe1, "east")
pe1.set_link_classroom(hsie, "west")

pe1.set_link_classroom(pe2, "south")
pe2.set_link_classroom(pe1, "north")

library.set_link_classroom(oval, "south")
oval.set_link_classroom(library, "north")

oval.set_link_classroom(detention, "east")
detention.set_link_classroom(oval, "west")

# Enemy
principal = Teacher("Prin C. Pal", "The principal of the school")
math_room.set_character(principal)

principal.set_conversation("Come closer... I can't see you.")
principal.set_weakness("aura")

current_cave = math_room

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