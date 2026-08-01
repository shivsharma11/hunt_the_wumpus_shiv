# =========================================================
# imports
# =========================================================

from character import Character, Student, Teacher, EvilTeacher
from cave import Classroom
from item import Item

dead = False

# =========================================================
# create all of the items
# =========================================================

calculator = Item(
    "calculator",
    "A scientific calculator. Perfect for defeating maths teachers."
)

dictionary = Item(
    "dictionary",
    "A heavy Oxford dictionary."
)

fantasy_book = Item(
    "fantasy book",
    "A fantasy novel full of dragons and magic."
)

pylint = Item(
    "pylint",
    "A program that removes bugs from code."
)

school_key = Item(
    "school key",
    "A rusty key that unlocks the principal's office."
)

# =========================================================
# create every room
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
# place items around the school
# =========================================================

canteen.set_item(calculator)

library.set_item(dictionary)

biology.set_item(fantasy_book)

computer_lab.set_item(pylint)

principal_office.set_item(school_key)

# =========================================================
# describe every room
# =========================================================

entrance.set_description(
    "The front gates of Quakers Hill High School. Once you enter, there's no turning back."
)

hall1.set_description(
    "Students rush past as they try not to be late for class."
)

hall2.set_description(
    "Rows of blue lockers line the walls."
)

hall3.set_description(
    "A surprisingly quiet hallway."
)

hall4.set_description(
    "You can hear strange noises coming from the science rooms."
)

hall5.set_description(
    "The smell of lunch fills the hallway."
)

hall6.set_description(
    "A peaceful hallway beside the library."
)

hall7.set_description(
    "This hallway is almost completely empty."
)

hall8.set_description(
    "School trophies fill a large display cabinet."
)

hall9.set_description(
    "The hallway leading towards freedom."
)

principal_office.set_description(
    "The principal's office. His intimidating aura fills the room."
)

exit_room.set_description(
    "Fresh air. You've finally escaped the school."
)

cafe.set_description(
    "A small café where students buy snacks."
)

canteen.set_description(
    "The school canteen is packed with hungry students."
)

library.set_description(
    "Bookshelves stretch from floor to ceiling."
)

oval.set_description(
    "A huge grassy oval used for sport."
)

detention.set_description(
    "A silent room filled with lonely desks."
)

computer_lab.set_description(
    "Rows of glowing computers wait for students."
)

biology.set_description(
    "Skeletons and preserved specimens cover the room."
)

physics.set_description(
    "Physics equipment sits on every bench."
)

chemistry.set_description(
    "Chemicals bubble away inside glass beakers."
)

math_classroom.set_description(
    "Whiteboards covered with difficult equations."
)

math_faculty.set_description(
    "The maths teachers are busy making exams."
)

english_classroom.set_description(
    "Students quietly analyse Shakespeare."
)

english_office.set_description(
    "Stacks of essays cover every desk."
)

hsie.set_description(
    "Maps and history posters decorate the walls."
)

pe1.set_description(
    "Sports equipment is scattered around the room."
)

pe2.set_description(
    "An indoor sports court echoes with bouncing basketballs."
)

# =========================================================
# link every room together
# =========================================================

# ---------------- entrance ----------------

entrance.set_link_classroom(hall1, "west")

# ---------------- hall 1 ----------------

hall1.set_link_classroom(entrance, "east")
hall1.set_link_classroom(math_classroom, "north")
hall1.set_link_classroom(english_classroom, "south")
hall1.set_link_classroom(hall2, "southwest")

# ---------------- hall 2 ----------------

hall2.set_link_classroom(hall1, "northeast")
hall2.set_link_classroom(hall3, "north")
hall2.set_link_classroom(hall4, "northwest")
hall2.set_link_classroom(hsie, "west")
hall2.set_link_classroom(english_office, "east")
hall2.set_link_classroom(oval, "south")
hall2.set_link_classroom(cafe, "southeast")

# ---------------- hall 3 ----------------

hall3.set_link_classroom(hall2, "south")
hall3.set_link_classroom(hall4, "west")
hall3.set_link_classroom(hall1, "east")

# ---------------- hall 4 ----------------

hall4.set_link_classroom(chemistry, "north")
hall4.set_link_classroom(physics, "northwest")
hall4.set_link_classroom(hall5, "west")
hall4.set_link_classroom(hall2, "southeast")
hall4.set_link_classroom(hsie, "south")
hall4.set_link_classroom(pe1, "southwest")

# ---------------- hall 5 ----------------

hall5.set_link_classroom(physics, "north")
hall5.set_link_classroom(biology, "northwest")
hall5.set_link_classroom(canteen, "southwest")
hall5.set_link_classroom(pe1, "south")
hall5.set_link_classroom(hall6, "west")
hall5.set_link_classroom(hall4, "east")
hall5.set_link_classroom(hsie, "southeast")

# ---------------- hall 6 ----------------

hall6.set_link_classroom(hall5, "east")
hall6.set_link_classroom(biology, "north")
hall6.set_link_classroom(computer_lab, "northwest")
hall6.set_link_classroom(physics, "northeast")
hall6.set_link_classroom(library, "west")
hall6.set_link_classroom(canteen, "south")
hall6.set_link_classroom(pe1, "southwest")
hall6.set_link_classroom(hall7, "north")

# ---------------- hall 7 ----------------

hall7.set_link_classroom(hall6, "south")
hall7.set_link_classroom(hall8, "west")
hall7.set_link_classroom(detention, "east")

# ---------------- hall 8 ----------------

hall8.set_link_classroom(hall7, "east")
hall8.set_link_classroom(hall9, "west")
hall8.set_link_classroom(principal_office, "north")

# ---------------- hall 9 ----------------

hall9.set_link_classroom(hall8, "east")
hall9.set_link_classroom(exit_room, "west")

# =========================================================
# maths wing
# =========================================================

math_classroom.set_link_classroom(hall1, "south")
math_classroom.set_link_classroom(math_faculty, "north")

math_faculty.set_link_classroom(math_classroom, "south")

# =========================================================
# english wing
# =========================================================

english_classroom.set_link_classroom(hall1, "north")
english_classroom.set_link_classroom(english_office, "south")

english_office.set_link_classroom(english_classroom, "north")
english_office.set_link_classroom(hall2, "west")

# =========================================================
# science wing
# =========================================================

chemistry.set_link_classroom(hall4, "south")
chemistry.set_link_classroom(physics, "west")

physics.set_link_classroom(chemistry, "east")
physics.set_link_classroom(biology, "west")
physics.set_link_classroom(hall5, "south")

biology.set_link_classroom(physics, "east")
biology.set_link_classroom(computer_lab, "west")
biology.set_link_classroom(hall6, "south")
biology.set_link_classroom(library, "southwest")

computer_lab.set_link_classroom(biology, "east")

# =========================================================
# hsie / pe wing
# =========================================================

hsie.set_link_classroom(hall2, "east")
hsie.set_link_classroom(hall4, "north")
hsie.set_link_classroom(hall5, "northwest")
hsie.set_link_classroom(pe1, "west")

pe1.set_link_classroom(hsie, "east")
pe1.set_link_classroom(canteen, "west")
pe1.set_link_classroom(oval, "south")
pe1.set_link_classroom(hall5, "north")
pe1.set_link_classroom(hall6, "northwest")
pe1.set_link_classroom(pe2, "west")

pe2.set_link_classroom(pe1, "east")

# =========================================================
# library / canteen / cafe
# =========================================================

library.set_link_classroom(hall6, "east")
library.set_link_classroom(biology, "northeast")

canteen.set_link_classroom(hall5, "northeast")
canteen.set_link_classroom(hall6, "north")
canteen.set_link_classroom(pe1, "east")
canteen.set_link_classroom(cafe, "south")

cafe.set_link_classroom(canteen, "north")
cafe.set_link_classroom(hall2, "northwest")

# =========================================================
# detention / principal / exit
# =========================================================

detention.set_link_classroom(hall7, "west")

principal_office.set_link_classroom(hall8, "south")

exit_room.set_link_classroom(hall9, "east")

# =========================================================
# create friendly students
# =========================================================

# these students give hints about where useful items are

ryan = Character(
    "Ryan",
    "A tired Year 11 student carrying several maths textbooks."
)

ryan.set_conversation(
    "I heard Mr Algebra is terrified of calculators. "
    "You might find one somewhere near the canteen."
)

hall3.set_character(ryan)


liam = Character(
    "Liam",
    "A nervous student trying to finish his English homework."
)

liam.set_conversation(
    "Ms Grammar absolutely hates dictionaries. "
    "I think I saw one in the library."
)

hall2.set_character(liam)


emily = Character(
    "Emily",
    "A student reading fantasy novels."
)

emily.set_conversation(
    "I accidentally left my favourite fantasy book in the Biology lab."
)

library.set_character(emily)


ava = Character(
    "Ava",
    "She's eating lunch with her friends."
)

ava.set_conversation(
    "Mr Brooks always complains when students don't use pylint."
)

canteen.set_character(ava)


ethan = Character(
    "Ethan",
    "A Year 12 student who knows the school well."
)

ethan.set_conversation(
    "The Principal never lets anyone leave without challenging them."
)

hall8.set_character(ethan)

# =========================================================
# create the evil teachers
# =========================================================

evil_math = EvilTeacher(
    "Mr Algebra",
    "The terrifying maths teacher."
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
    "Your grammar is unacceptable!"
)

evil_english.set_weakness("dictionary")

english_office.set_character(evil_english)


evil_science = EvilTeacher(
    "Dr Atom",
    "He enjoys dangerous chemistry experiments."
)

evil_science.set_conversation(
    "Prepare for explosive science!"
)

evil_science.set_weakness("fantasy book")

physics.set_character(evil_science)


evil_computer = EvilTeacher(
    "Mr Brooks",
    "He can spot bugs in code instantly."
)

evil_computer.set_conversation(
    "Your code won't even compile!"
)

evil_computer.set_weakness("pylint")

computer_lab.set_character(evil_computer)


principal = EvilTeacher(
    "Prin C. Pal",
    "The Principal himself."
)

principal.set_conversation(
    "So... you've made it this far."
)

principal.set_weakness("school key")

principal_office.set_character(principal)

# =========================================================
# create the player
# =========================================================

player = Student(
    "Shivansh",
    "A stressed Year 11 student trying to escape school."
)

# the player starts at the entrance

current_cave = entrance

# =========================================================
# movement commands
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
# welcome message
# =========================================================

print("=" * 55)
print("          escape from quakers hill high")
print("=" * 55)
print()
print("collect useful items around the school.")
print("defeat every evil teacher.")
print("beat the principal.")
print("escape through the exit.")
print()
print("type 'help' if you get stuck.")
print("=" * 55)

# =========================================================
# main game loop
# =========================================================

while not dead:

    print()
    current_cave.describe()

    inhabitant = current_cave.get_character()

    # -----------------------------------------------------
    # if there is a character in the room
    # -----------------------------------------------------

    if inhabitant:

        print()
        inhabitant.describe()

        # automatically interact with teachers

        if isinstance(inhabitant, Teacher):

            print("\n" + "=" * 50)
            print("you have encountered", inhabitant.name + "!")
            print("=" * 50)

            inhabitant.talk()

            teacher_defeated = False

            while not teacher_defeated and not dead:

                print("\ncommands")
                print("fight")
                print("run")

                action = input("> ").strip().lower()

                # ---------------- fight ----------------

                if action == "fight":

                    player.show_inventory()

                    fight_with = input(
                        "\nwhat item will you use? "
                    ).strip().lower()

                    if not player.has_item(fight_with):

                        print("\nyou don't have that item.")

                    elif inhabitant.fight(fight_with):

                        print("\nyou defeated", inhabitant.name)

                        current_cave.set_character(None)
                        inhabitant = None

                        teacher_defeated = True

                        # if the principal is defeated,
                        # unlock the exit

                        if inhabitant == principal:

                            print()
                            print("the principal drops the exit key!")

                    else:

                        print()
                        print("you were defeated.")
                        print("game over.")

                        dead = True

                # ---------------- run ----------------

                elif action == "run":

                    print(
                        "\nyou quickly leave before the teacher catches you."
                    )

                    teacher_defeated = True

                else:

                    print("invalid command.")

        else:

            print("\ncommands")
            print("talk")
            print("move")
            print("take")
            print("inventory")
            print("study")
            print("help")
            print("quit")

    # -----------------------------------------------------
    # no character in the room
    # -----------------------------------------------------

    else:

        print("\ncommands")
        print("move")
        print("take")
        print("inventory")
        print("study")
        print("look")
        print("help")
        print("quit")

    # -----------------------------------------------------
    # get player command
    # -----------------------------------------------------

    command = input("\n> ").strip().lower()

    # allow movement shortcuts

    if command in direction_aliases:
        command = direction_aliases[command]

    # allow "go north" or "move north"

    words = command.split()

    if len(words) == 2:

        if words[0] in ["go", "move", "walk"]:

            command = words[1]

    # -----------------------------------------------------
    # movement
    # -----------------------------------------------------

    if command in valid_directions:

        current_cave = current_cave.move(command)

    # -----------------------------------------------------
    # talk
    # -----------------------------------------------------

    elif command == "talk":

        if inhabitant:

            inhabitant.talk()

        else:

            print("there is nobody here.")

    # -----------------------------------------------------
    # take item
    # -----------------------------------------------------

    elif command == "take":

        item = current_cave.get_item()

        if item:

            player.add_item(item)

            current_cave.set_item(None)

        else:

            print("there is nothing to take.")

    # -----------------------------------------------------
    # inventory
    # -----------------------------------------------------

    elif command == "inventory":

        player.show_inventory()

    # -----------------------------------------------------
    # study
    # -----------------------------------------------------

    elif command == "study":

        player.study()

    # -----------------------------------------------------
    # look around
    # -----------------------------------------------------

    elif command == "look":

        current_cave.describe()

        if current_cave.get_character():

            current_cave.get_character().describe()

    # -----------------------------------------------------
    # help
    # -----------------------------------------------------

    elif command == "help":

        print("""
================== commands ==================

movement
--------
north
south
east
west
northeast
northwest
southeast
southwest

shortcuts
---------
n
s
e
w
ne
nw
se
sw

you can also type:
go north
move west
walk east

actions
-------
talk
take
inventory
study
look
help
quit

==============================================
""")

    # -----------------------------------------------------
    # quit game
    # -----------------------------------------------------

    elif command == "quit":

        print("thanks for playing!")

        dead = True

    # -----------------------------------------------------
    # invalid command
    # -----------------------------------------------------

    else:

        print("invalid command.")

# -----------------------------------------------------
# automatically interact with teachers
# -----------------------------------------------------

if isinstance(inhabitant, Teacher):

    print("\n" + "=" * 50)
    print("you encountered", inhabitant.name + "!")
    print("=" * 50)

    inhabitant.talk()

    player_health = 3
    attempts = 0

    while True:

        print("\nhealth:", "❤️" * player_health)

        print("\ncommands")
        print("- fight")
        print("- run")
        print("- inventory")

        action = input("> ").strip().lower()

        # ---------------- inventory ----------------

        if action == "inventory":

            player.show_inventory()

        # ---------------- run ----------------

        elif action == "run":

            print("you escaped!")

            break

        # ---------------- fight ----------------

        elif action == "fight":

            player.show_inventory()

            weapon = input(
                "\nwhat will you use? "
            ).strip().lower()

            if not player.has_item(weapon):

                print("\nyou don't own that item.")
                continue

            if inhabitant.fight(weapon):

                print("\nyou defeated", inhabitant.name)

                current_cave.set_character(None)

                if inhabitant == principal:

                    print()
                    print("you defeated the principal!")
                    print("you escaped quakers hill high!")
                    dead = True

                break

            attempts += 1
            player_health -= 1

            print("\nthat didn't work!")

            if attempts == 2:

                print()
                print(
                    inhabitant.name,
                    "laughs."
                )

                print(
                    "'maybe try something related to'",
                    inhabitant.get_weakness() + "...'"
                )

            if player_health <= 0:

                print()
                print("you were defeated.")
                print("game over.")

                dead = True
                break

        else:

            print("invalid command.")

elif command.startswith("examine"):

    words = command.split(maxsplit=1)

    if len(words) < 2:

        print("examine what?")

    else:

        name = words[1]

        found = False

        for item in player.inventory:

            if item.get_name().lower() == name:

                item.describe()
                found = True
                break

        if not found:

            print("you don't have that item.")

# =========================================================
# helper functions
# =========================================================

# display all available commands
def show_commands():

    print("\n" + "=" * 50)
    print("available commands")
    print("=" * 50)

    print("\nmovement")
    print("--------")
    print("north south east west")
    print("northeast northwest southeast southwest")
    print("or")
    print("n s e w ne nw se sw")

    print("\nactions")
    print("-------")
    print("talk")
    print("take")
    print("inventory")
    print("study")
    print("look")
    print("help")
    print("quit")


# display a simple welcome screen
def introduction():

    print("=" * 60)
    print("      escape from quakers hill high school")
    print("=" * 60)
    print()
    print("your goal is to escape the school.")
    print("collect useful items.")
    print("defeat the evil teachers.")
    print("finally defeat the principal.")
    print()
    print("good luck!")
    print("=" * 60)


# start the game
introduction()

# =========================================================
# main game loop
# =========================================================

while not dead:

    print()

    current_cave.describe()

    inhabitant = current_cave.get_character()

    # show the character if there is one

    if inhabitant:

        inhabitant.describe()

    # always show available commands

    show_commands()

    command = input("\n> ").strip().lower()

    # convert shortcuts into full directions

    if command in direction_aliases:

        command = direction_aliases[command]

    # --------------------------------------------------
    # movement
    # --------------------------------------------------

    if command in valid_directions:

        current_cave = current_cave.move(command)

        continue

    # --------------------------------------------------
    # talk
    # --------------------------------------------------

    elif command == "talk":

        if inhabitant:

            inhabitant.talk()

        else:

            print("there is nobody here.")

    # --------------------------------------------------
    # take an item
    # --------------------------------------------------

    elif command == "take":

        item = current_cave.get_item()

        if item:

            player.add_item(item)

            current_cave.set_item(None)

        else:

            print("there is nothing here.")

    # --------------------------------------------------
    # show inventory
    # --------------------------------------------------

    elif command == "inventory":

        player.show_inventory()

    # --------------------------------------------------
    # study
    # --------------------------------------------------

    elif command == "study":

        player.study()

    # --------------------------------------------------
    # look around the room again
    # --------------------------------------------------

    elif command == "look":

        current_cave.describe()

        if inhabitant:

            inhabitant.describe()

    # --------------------------------------------------
    # fight
    # --------------------------------------------------

    elif command == "fight":

        if inhabitant and isinstance(inhabitant, Teacher):

            print("\nprepare for battle!")

            player.show_inventory()

            fight_with = input(
                "\nwhat will you fight with? "
            ).strip().lower()

            # make sure the player actually has the item

            if not player.has_item(fight_with):

                print("\nyou don't have that item!")

            else:

                if inhabitant.fight(fight_with):

                    print("\nyou defeated", inhabitant.name + "!")

                    # remove the teacher after defeating them

                    current_cave.set_character(None)

                    # check if it was the principal

                    if inhabitant == principal:

                        print("\n" + "=" * 50)
                        print("congratulations!")
                        print("you defeated the principal!")
                        print("you escaped quakers hill high!")
                        print("=" * 50)

                        dead = True

                else:

                    print("\nyou were defeated...")
                    print("game over.")

                    dead = True

        else:

            print("there is nobody here to fight.")

    # --------------------------------------------------
    # help menu
    # --------------------------------------------------

    elif command == "help":

        print("\n" + "=" * 50)
        print("help menu")
        print("=" * 50)

        print("\nmovement")
        print("north")
        print("south")
        print("east")
        print("west")
        print("northeast")
        print("northwest")
        print("southeast")
        print("southwest")

        print("\nshortcuts")
        print("n s e w ne nw se sw")

        print("\nactions")
        print("talk")
        print("fight")
        print("take")
        print("inventory")
        print("study")
        print("look")
        print("help")
        print("quit")

        print("\ngoal")
        print("collect useful items and defeat every teacher.")
        print("finally defeat the principal to escape.")

    # --------------------------------------------------
    # quit the game
    # --------------------------------------------------

    elif command == "quit":

        answer = input(
            "are you sure you want to quit? (y/n): "
        ).lower()

        if answer == "y":

            print("\nthanks for playing!")

            dead = True

    # --------------------------------------------------
    # invalid command
    # --------------------------------------------------

    else:

        print("invalid command.")

# =========================================================
# end of game
# =========================================================

print("\n" + "=" * 50)

if dead:

    print("game ended.")

print("=" * 50)