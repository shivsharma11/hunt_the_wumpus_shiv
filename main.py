from character import Character, Teacher, EvilTeacher, Student
from cave import Classroom
from item import Item

dead = False

# =========================================================
# ITEMS
# =========================================================

calculator = Item(
    "calculator",
    "A scientific calculator."
)

dictionary = Item(
    "dictionary",
    "A giant Oxford dictionary."
)

fantasy_book = Item(
    "fantasy book",
    "A magical fantasy novel."
)

pylint = Item(
    "pylint",
    "A code analysis program."
)

school_key = Item(
    "school key",
    "A rusty key that looks important."
)

# =========================================================
# ROOM CREATION
# =========================================================

entrance = Classroom("Entrance")

hall1 = Classroom("Hall 1")
hall2 = Classroom("Hall 2")
hall3 = Classroom("Hall 3")
hall4 = Classroom("Hall 4")
hall5 = Classroom("Hall 5")
hall6 = Classroom("Hall 6")
hall7 = Classroom("Hall 7")
hall8 = Classroom("Hall 8")
hall9 = Classroom("Hall 9")

principal_office = Classroom("Principal's Office")
exit_room = Classroom("Exit")

cafe = Classroom("Cafe")
canteen = Classroom("Canteen")
library = Classroom("Library")
oval = Classroom("Oval")
detention = Classroom("Detention")

computer_lab = Classroom("Computer Lab")
biology = Classroom("Biology")
physics = Classroom("Physics")
chemistry = Classroom("Chemistry")

math_classroom = Classroom("Mathematics")
math_faculty = Classroom("Math Faculty")

english_classroom = Classroom("English")
english_office = Classroom("English Office")

hsie = Classroom("HSIE")
pe1 = Classroom("PE 1")
pe2 = Classroom("PE 2")

# =========================================================
# ITEM PLACEMENT
# =========================================================

canteen.set_item(calculator)
library.set_item(dictionary)
biology.set_item(fantasy_book)
computer_lab.set_item(pylint)
principal_office.set_item(school_key)

# =========================================================
# ROOM DESCRIPTIONS
# =========================================================

entrance.set_description(
    "The school entrance. Once you walk in, there is no turning back."
)

hall1.set_description(
    "Students rush past you carrying backpacks."
)

hall2.set_description(
    "A crowded hallway filled with lockers."
)

hall3.set_description(
    "A quieter hallway with classroom doors."
)

hall4.set_description(
    "The science wing begins here."
)

hall5.set_description(
    "The smell of food drifts through the hall."
)

hall6.set_description(
    "A peaceful hallway beside the library."
)

hall7.set_description(
    "An empty hallway."
)

hall8.set_description(
    "A hallway lined with school trophies."
)

hall9.set_description(
    "A silent hallway leading towards the exit."
)

principal_office.set_description(
    "The Principal's office. His intimidating aura fills the room."
)

exit_room.set_description(
    "You've escaped Quakers Hill High School!"
)

cafe.set_description(
    "A cosy café selling snacks and drinks."
)

canteen.set_description(
    "Students are eating lunch."
)

library.set_description(
    "Rows upon rows of books fill the shelves."
)

oval.set_description(
    "A huge grassy oval."
)

detention.set_description(
    "A depressing room filled with desks."
)

computer_lab.set_description(
    "Rows of glowing computers."
)

biology.set_description(
    "Skeletons and preserved specimens surround you."
)

physics.set_description(
    "Physics equipment is scattered everywhere."
)

chemistry.set_description(
    "Beakers and chemicals cover the benches."
)

math_classroom.set_description(
    "Equations cover every whiteboard."
)

math_faculty.set_description(
    "The Maths teachers prepare tomorrow's exam."
)

english_classroom.set_description(
    "Students analyse Shakespeare."
)

english_office.set_description(
    "Stacks of essays cover every desk."
)

hsie.set_description(
    "History and Geography posters line the walls."
)

pe1.set_description(
    "Sports equipment fills the room."
)

pe2.set_description(
    "Indoor courts echo with bouncing basketballs."
)

# =========================================================
# ROOM LINKS
# =========================================================

# Entrance
entrance.set_link_classroom(hall1, "west")

# ---------------- Hall 1 ----------------

hall1.set_link_classroom(entrance, "east")
hall1.set_link_classroom(math_classroom, "north")
hall1.set_link_classroom(english_classroom, "south")
hall1.set_link_classroom(hall2, "southwest")

# ---------------- Hall 2 ----------------

hall2.set_link_classroom(hall1, "northeast")
hall2.set_link_classroom(hall3, "north")
hall2.set_link_classroom(hall4, "northwest")
hall2.set_link_classroom(hsie, "west")
hall2.set_link_classroom(english_office, "east")
hall2.set_link_classroom(oval, "south")
hall2.set_link_classroom(oval, "southwest")

# ---------------- Hall 3 ----------------

hall3.set_link_classroom(hall2, "south")
hall3.set_link_classroom(hall4, "west")
hall3.set_link_classroom(hall1, "east")

# ---------------- Hall 4 ----------------

hall4.set_link_classroom(chemistry, "north")
hall4.set_link_classroom(physics, "northwest")
hall4.set_link_classroom(hall5, "west")
hall4.set_link_classroom(hall2, "southeast")
hall4.set_link_classroom(hsie, "south")
hall4.set_link_classroom(pe1, "southwest")

# ---------------- Hall 5 ----------------

hall5.set_link_classroom(physics, "north")
hall5.set_link_classroom(biology, "northwest")
hall5.set_link_classroom(canteen, "southwest")
hall5.set_link_classroom(pe1, "south")
hall5.set_link_classroom(hall6, "west")
hall5.set_link_classroom(hall4, "east")
hall5.set_link_classroom(hsie, "southeast")

# ---------------- Hall 6 ----------------

hall6.set_link_classroom(hall5, "east")
hall6.set_link_classroom(biology, "north")
hall6.set_link_classroom(computer_lab, "northwest")
hall6.set_link_classroom(physics, "northeast")
hall6.set_link_classroom(library, "west")
hall6.set_link_classroom(canteen, "south")
hall6.set_link_classroom(pe1, "southwest")

# ---------------- Maths ----------------

math_classroom.set_link_classroom(hall1, "south")
math_classroom.set_link_classroom(math_faculty, "north")

math_faculty.set_link_classroom(math_classroom, "south")

# ---------------- English ----------------

english_classroom.set_link_classroom(hall1, "north")
english_classroom.set_link_classroom(hall2, "west")
english_classroom.set_link_classroom(english_office, "south")

english_office.set_link_classroom(english_classroom, "north")
english_office.set_link_classroom(hall2, "northwest")

# ---------------- Science ----------------

chemistry.set_link_classroom(hall4, "south")
chemistry.set_link_classroom(physics, "west")
chemistry.set_link_classroom(hall5, "southwest")

physics.set_link_classroom(chemistry, "east")
physics.set_link_classroom(hall5, "south")
physics.set_link_classroom(hall6, "southwest")
physics.set_link_classroom(biology, "west")

biology.set_link_classroom(computer_lab, "west")
biology.set_link_classroom(physics, "east")
biology.set_link_classroom(hall6, "south")
biology.set_link_classroom(library, "southwest")

computer_lab.set_link_classroom(biology, "east")

# ---------------- HSIE / PE ----------------

hsie.set_link_classroom(pe1, "west")
hsie.set_link_classroom(hall4, "north")
hsie.set_link_classroom(hall5, "northwest")
hsie.set_link_classroom(hall2, "east")

pe1.set_link_classroom(hsie, "east")
pe1.set_link_classroom(canteen, "west")
pe1.set_link_classroom(oval, "south")
pe1.set_link_classroom(hall5, "north")
pe1.set_link_classroom(hall6, "northwest")

# =========================================================
# FRIENDLY STUDENTS
# =========================================================

ryan = Character(
    "Ryan",
    "A sleepy Year 11 student carrying far too many maths books."
)
ryan.set_conversation(
    "Mr Algebra never goes anywhere without talking about calculus..."
)
hall3.set_character(ryan)


emily = Character(
    "Emily",
    "A friendly student reading a fantasy novel."
)
emily.set_conversation(
    "I left my favourite fantasy book in the Biology lab."
)
hall6.set_character(emily)


liam = Character(
    "Liam",
    "A nervous Year 11 student."
)
liam.set_conversation(
    "I heard Ms Grammar hates dictionaries..."
)
hall2.set_character(liam)


ava = Character(
    "Ava",
    "She's eating lunch before her next class."
)
ava.set_conversation(
    "The Computer teacher can't stand clean code."
)
canteen.set_character(ava)

# =========================================================
# EVIL TEACHERS
# =========================================================

principal = EvilTeacher(
    "Prin C. Pal",
    "The terrifying principal."
)
principal.set_conversation(
    "You aren't leaving this school so easily..."
)
principal.set_weakness("school key")
principal_office.set_character(principal)


evil_math = EvilTeacher(
    "Mr Algebra",
    "A furious maths teacher covered in equations."
)
evil_math.set_conversation(
    "Show me your working!"
)
evil_math.set_weakness("calculator")
math_classroom.set_character(evil_math)


evil_english = EvilTeacher(
    "Ms Grammar",
    "She corrects every sentence you say."
)
evil_english.set_conversation(
    "Your grammar is atrocious!"
)
evil_english.set_weakness("dictionary")
english_office.set_character(evil_english)


evil_computer = EvilTeacher(
    "Mr Brooks",
    "He throws keyboards when code doesn't compile."
)
evil_computer.set_conversation(
    "Your code has bugs!"
)
evil_computer.set_weakness("pylint")
computer_lab.set_character(evil_computer)


evil_science = EvilTeacher(
    "Dr Atom",
    "A science teacher with dangerous experiments."
)
evil_science.set_conversation(
    "Prepare for explosive chemistry!"
)
evil_science.set_weakness("fantasy book")
physics.set_character(evil_science)

# =========================================================
# PLAYER
# =========================================================

player = Student(
    "Shivansh",
    "A stressed Year 11 student trying to escape school."
)

current_cave = entrance

# =========================================================
# NAVIGATION
# =========================================================

valid_directions = [
    "north",
    "south",
    "east",
    "west",
    "northeast",
    "northwest",
    "southeast",
    "southwest"
]

direction_aliases = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "ne": "northeast",
    "nw": "northwest",
    "se": "southeast",
    "sw": "southwest"
}

# =========================================================
# GAME INTRODUCTION
# =========================================================

print("=" * 55)
print("      ESCAPE FROM QUAKERS HILL HIGH SCHOOL")
print("=" * 55)
print("Collect items, defeat evil teachers,")
print("and escape through the exit!")
print()
print("Type 'help' to see the available commands.")
print("=" * 55)

# =========================================================
# MAIN GAME LOOP
# =========================================================

while not dead:

    print()
    current_cave.describe()

    inhabitant = current_cave.get_character()

    if inhabitant:
        inhabitant.describe()

    command = input("\n> ").lower().strip()

    # ----------------------------
    # Direction shortcuts
    # ----------------------------

    if command in direction_aliases:
        command = direction_aliases[command]

    # ----------------------------
    # Movement
    # ----------------------------

    if command in valid_directions:
        current_cave = current_cave.move(command)

    # ----------------------------
    # Talk
    # ----------------------------

    elif command == "talk":

        if inhabitant:

            inhabitant.talk()

            # Ryan gives calculator
            if inhabitant == ryan:

                if not player.has_item("calculator"):

                    print("Ryan gives you his calculator.")
                    player.add_item(calculator)

            # Emily gives fantasy book hint

            elif inhabitant == emily:

                print("Emily smiles.")
                print("'The Biology lab has something useful.'")

            # Liam gives dictionary

            elif inhabitant == liam:

                if not player.has_item("dictionary"):

                    print("Liam hands you a dictionary.")
                    player.add_item(dictionary)

        else:
            print("There is nobody here.")

    # ----------------------------
    # Take item
    # ----------------------------

    elif command == "take":

        item = current_cave.get_item()

        if item:

            player.add_item(item)
            current_cave.set_item(None)

        else:

            print("There is nothing to take.")

    # ----------------------------
    # Inventory
    # ----------------------------

    elif command == "inventory":

        player.show_inventory()

    # ----------------------------
    # Study
    # ----------------------------

    elif command == "study":

        player.study()

    # ----------------------------
    # Fight
    # ----------------------------

    elif command == "fight":

        if inhabitant and isinstance(inhabitant, Teacher):

            fight_with = input("Fight with: ").lower()

            if not player.has_item(fight_with):

                print("You don't have that item.")

            elif inhabitant.fight(fight_with):

                print("You defeated", inhabitant.name)

                current_cave.set_character(None)

                if inhabitant == principal:

                    print()
                    print("Congratulations!")
                    print("You defeated the Principal.")
                    print("You escaped Quakers Hill High School!")
                    dead = True

            else:

                print()
                print("GAME OVER")
                dead = True

        else:

            print("There is nobody to fight.")

    # ----------------------------
    # Help
    # ----------------------------

    elif command == "help":

        print("""
================ COMMANDS ================

Movement
--------
north
south
east
west
northeast
northwest
southeast
southwest

or

n s e w ne nw se sw

Actions
-------
talk
fight
take
inventory
study
help
quit

==========================================
""")

    # ----------------------------
    # Quit
    # ----------------------------

    elif command == "quit":

        print("Goodbye!")
        dead = True

    # ----------------------------
    # Invalid command
    # ----------------------------

    else:

        print("Invalid command.")