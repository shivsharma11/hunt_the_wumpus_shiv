# =========================================================
# Escape from Quakers Hill High School - Shivansh Sharma Year 11 Software Engineering
# =========================================================

import os
import time
import random
from colorama import init, Fore, Style

from character import Character, Student, Teacher, EvilTeacher
from cave import Classroom
from item import Item

init(autoreset=True)

dead = False

# =========================================================
# helper functions
# =========================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def ascii_loading(message="loading"):
    print(Fore.CYAN + "\n" + message, end="", flush=True)
    for dot in "...":
        time.sleep(0.25)
        print(dot, end="", flush=True)
    print()


def ascii_title():
    clear_screen()
    print(Fore.YELLOW + "=" * 60)
    print(Fore.GREEN + "      ESCAPE FROM QUAKERS HILL HIGH SCHOOL")
    print(Fore.YELLOW + "=" * 60)
    print(Fore.MAGENTA + r"""
  ░██████████   ░██████     ░██████     ░███    ░█████████  ░██████████    
░██          ░██   ░██   ░██   ░██   ░██░██   ░██     ░██ ░██            
░██         ░██         ░██         ░██  ░██  ░██     ░██ ░██            
░█████████   ░████████  ░██        ░█████████ ░█████████  ░█████████     
░██                 ░██ ░██        ░██    ░██ ░██         ░██            
░██          ░██   ░██   ░██   ░██ ░██    ░██ ░██         ░██            
░██████████   ░██████     ░██████  ░██    ░██ ░██         ░██████████    
                                                                         

    """)
    ascii_loading("entering the school")


def ascii_detention():
    clear_screen()
    print(Fore.RED + "\n" + "=" * 40)
    print("   YOU HAVE BEEN SENT TO DETENTION")
    print("=" * 40)
    print(Fore.RED + r"""
   ________________________
  |                        |
  |        DETENTION       |
  |________________________|
    """)
    ascii_loading("serving your time")
    for i in range(5, 0, -1):
        print(Fore.YELLOW + f"\nyou will be released in {i} seconds...")
        time.sleep(1)
    print(Fore.GREEN + "\n...time served. you may return to class.")


def ascii_victory():
    print(Fore.GREEN + "\n" + "=" * 40)
    print("          VICTORY!")
    print("=" * 40)
    print(Fore.GREEN + r"""
      \o/   \o/   \o/
       |     |     |
      / \   / \   / \
    """)
    ascii_loading("celebrating")


def ascii_fight_intro():
    print(Fore.RED + r"""
                                                                  
                                                            ▄▄ 
████▄     ████▄    ▄██     ██████ ██  ▄████  ██  ██ ██████  ██ 
 ▄▄██      ▄██▀     ██     ██▄▄   ██ ██  ̶̶̶▄▄ ██████   ██    ██ 
▄▄▄█▀ ▄ ▄ ███▄▄ ▄ ▄ ██ ▄ ▄ ██     ██  ̶̶̶███▀  ██  ██   ██    ̶̶ 
                                                               
    """)


# display all available commands
def show_commands():

    print(Fore.YELLOW + "\n" + "=" * 50)
    print("available commands")
    print("=" * 50)

    print(Fore.CYAN + "\nmovement")
    print("--------")
    print("north south east west")
    print("northeast northwest southeast southwest")
    print("or")
    print("n s e w ne nw se sw")

    print(Fore.CYAN + "\nactions")
    print("-------")
    print("talk")
    print("fight")
    print("take")
    print("inventory")
    print("study")
    print("look")
    print("help")
    print("quit")


# display a simple welcome screen
def introduction():
    ascii_title()

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
detention = Classroom("Detention")

computer_lab = Classroom("Computer Lab")
biology = Classroom("Biology")
physics = Classroom("Physics")
chemistry = Classroom("Chemistry")

math_classroom = Classroom("Mathematics")
math_faculty = Classroom("Math Faculty")

english_classroom = Classroom("English")
english_office = Classroom("English Office")

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
    "A small cafe where students buy snacks."
)

canteen.set_description(
    "The school canteen is packed with hungry students."
)

library.set_description(
    "Bookshelves stretch from floor to ceiling."
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
hall2.set_link_classroom(english_office, "east")
hall2.set_link_classroom(cafe, "southeast")
hall2.set_link_classroom(hall5, "south")  

# ---------------- hall 3 ----------------

hall3.set_link_classroom(hall2, "south")
hall3.set_link_classroom(hall4, "west")
hall3.set_link_classroom(hall1, "east")

# ---------------- hall 4 ----------------

hall4.set_link_classroom(chemistry, "north")
hall4.set_link_classroom(physics, "northwest")
hall4.set_link_classroom(hall5, "west")
hall4.set_link_classroom(hall2, "southeast")
hall4.set_link_classroom(pe1, "southwest")

# ---------------- hall 5 ----------------

hall5.set_link_classroom(physics, "north")
hall5.set_link_classroom(biology, "northwest")
hall5.set_link_classroom(canteen, "southwest")
hall5.set_link_classroom(pe1, "south")
hall5.set_link_classroom(hall6, "west")
hall5.set_link_classroom(hall4, "east")

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
# pe wing
# =========================================================

pe1.set_link_classroom(hall5, "north")
pe1.set_link_classroom(canteen, "west")
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

ryan = Character(
    "Ryan",
    "A tired Year 11 student carrying several maths textbooks."
)

ryan.set_conversation(
    "Bro I’ve been doing maths since 7am...\n"
    "Daghel is actually scared of calculators.\n"
    "If you’re gonna fight him, make sure you’ve got one."
)

hall3.set_character(ryan)


sach = Character(
    "Sach",
    "A studious Extension 2 Student, studying hard for his maths test."
)

sach.set_conversation(
    "I'm really not in the mood to talk to people who get less than me in maths right now.\n"
    "Bring a dictionary to Pecora though- he needs to learn how to spell 'flibbertigibbet' \n"
)

hall2.set_character(sach)


jesh = Character(
    "Jesh",
    "A student preparing for his swim competition"
)

jesh.set_conversation(
    "*groans* I  left my fiction book in the Biology lab.\n"
    "The science faculty hates imagination — maybe itll confuse all them?"
)

library.set_character(jesh)


sid = Character(
    "Sid",
    "Often found near the canteen"
)

sid.set_conversation(
    "Mr Brooks is allergic to bad code.\n"
    "If you bring pylint, he’ll probably explode. \n"
    "Now shoo, I'm trying to enjoy my meal."
)

canteen.set_character(sid)


bhav = Character(
    "Bhavjot",
    "Security, he knows the school well."
)

bhav.set_conversation(
    "You’re nearly at the principal.\n"
    "He won’t let you leave unless you prove yourself.\n"
    "Rumour says a key unlocks his weakness."
)

hall8.set_character(bhav)

# =========================================================
# create the evil teachers
# =========================================================

# Daghel - Maths
evil_math = EvilTeacher(
    "Daghel",
    "The terrifying maths teacher."
)

evil_math.set_conversation(
    "I said to use working out..."
)

evil_math.set_weakness("calculator")

math_classroom.set_character(evil_math)

# ANTHONY JAMES PECORA - English
evil_english = EvilTeacher(
    "ANTHONY JAMES PECORA",
    "He corrects every sentence you say."
)

evil_english.set_conversation(
    "TWENTY ONE OUT OF THIRTY!!!\n"
    "YOUR ESSAY IS A DISGRACE!!!"
)

evil_english.set_weakness("dictionary")

english_office.set_character(evil_english)

# Maharaj - Chemistry (she)
evil_chem = EvilTeacher(
    "Maharaj",
    "She enjoys dangerous chemistry experiments."
)

evil_chem.set_conversation(
    "I'm going to titrate you."
)

evil_chem.set_weakness("fantasy book")

chemistry.set_character(evil_chem)

# Kumar - Physics
evil_physics = EvilTeacher(
    "Kumar",
    "The physics master who sees all."
)

evil_physics.set_conversation(
    "IT IS NOT AN EASY SUBJECT."
)

evil_physics.set_weakness("fantasy book")

physics.set_character(evil_physics)

# Mr Brooks - Computer (the GOAT)
evil_computer = EvilTeacher(
    "Mr Brooks",
    "He can spot bugs in code instantly (because he's so awesome)"
)

evil_computer.set_conversation(
    "Open up Thonny young man. \n"
    "Let's see if you remember what PWM is..."
)

evil_computer.set_weakness("pylint")

computer_lab.set_character(evil_computer)

# Principal
principal = EvilTeacher(
    "Mr. ???",
    "The Principal himself."
)

principal.set_conversation(
    "You've made it this far. \n"
    "Shame it all ends here though..."
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

# Add study points and N-awards tracking to the player instance
# Subjects: math, english, chemistry, physics, computer
player.study_points = {
    "math": 0,
    "english": 0,
    "chemistry": 0,
    "physics": 0,
    "computer": 0
}
# Number of 'N' awards received when failing while using study points
player.n_awards = 0

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
# start the game
# =========================================================

introduction()

# =========================================================
# main game loop
# =========================================================

# skip_clear controls whether the next loop iteration should skip clearing the screen.
# When True, the loop will not call clear_screen() so the player can read the previous output.
skip_clear = False

# helper: map teacher name to subject key for study usage
teacher_subject_map = {
    "Daghel": "math",
    "ANTHONY JAMES PECORA": "english",
    "Maharaj": "chemistry",
    "Dr Kumar": "physics",
    "Mr Brooks": "computer"
    # Principal is not included; principal requires the school key
}

def show_player_study_status():
    print(Fore.MAGENTA + "\nStudy points:")
    for subj, pts in player.study_points.items():
        print(Fore.MAGENTA + f" - {subj.capitalize()}: {pts}")
    print(Fore.MAGENTA + f"N-awards: {player.n_awards}/3")

while not dead:

    if not skip_clear:
        clear_screen()
    else:
        # reset for next iteration so subsequent turns clear normally
        skip_clear = False

    print()
    current_cave.describe()

    inhabitant = current_cave.get_character()

    if inhabitant:
        inhabitant.describe()

    show_commands()

    # show study status briefly
    show_player_study_status()

    command = input(Fore.YELLOW + "\n> ").strip().lower()

    # convert shortcuts into full directions

    if command in direction_aliases:
        command = direction_aliases[command]

    # allow "go north" or "move north" or "walk north"

    words = command.split()

    if len(words) == 2 and words[0] in ["go", "move", "walk"]:
        command = words[1]

    # --------------------------------------------------
    # movement
    # --------------------------------------------------

    if command in valid_directions:

        # ensure we clear on movement
        skip_clear = False
        ascii_loading("walking")
        current_cave = current_cave.move(command)
        continue

    # --------------------------------------------------
    # talk
    # --------------------------------------------------

    elif command == "talk":

        if inhabitant:
            print(Fore.GREEN)
            inhabitant.talk()
            # prevent the next loop from clearing immediately so player can read
            skip_clear = True
            input(Fore.CYAN + "\n(press ENTER to continue)")
        else:
            print(Fore.RED + "there is nobody here.")
            skip_clear = True
            input(Fore.CYAN + "\n(press ENTER to continue)")

    # --------------------------------------------------
    # take an item
    # --------------------------------------------------

    elif command == "take":

        item = current_cave.get_item()

        if item:

            print(Fore.GREEN + f"\nyou picked up {item.name}!")
            player.add_item(item)
            current_cave.set_item(None)

        else:

            print(Fore.RED + "there is nothing here.")

        skip_clear = True
        input(Fore.CYAN + "\n(press ENTER to continue)")

    # --------------------------------------------------
    # show inventory
    # --------------------------------------------------

    elif command == "inventory":

        print(Fore.GREEN)
        player.show_inventory()
        skip_clear = True
        input(Fore.CYAN + "\n(press ENTER to continue)")

    # --------------------------------------------------
    # study
    # --------------------------------------------------

    elif command == "study":
        # Make study useful: choose a subject, gain study points
        print(Fore.CYAN + "\nWhich subject do you want to study?")
        print("Options: math, english, chemistry, physics, computer")
        subj = input(Fore.YELLOW + "\n> ").strip().lower()

        if subj not in player.study_points:
            print(Fore.RED + "\nThat's not a valid subject.")
            skip_clear = True
            input(Fore.CYAN + "\n(press ENTER to continue)")
        else:
            # simulate studying: gain between 10 and 30 points (sometimes study sessions are good, sometimes they're bad)
            # also adds gambling to the game which is necessary (for educational purposes)
            gained = random.randint(10, 30)
            player.study_points[subj] += gained
            # cap at 200 for sanity
            if player.study_points[subj] > 200:
                player.study_points[subj] = 200
            print(Fore.GREEN + f"\nYou studied {subj}. You gained {gained} study points.")
            print(Fore.MAGENTA + f"Total {subj.capitalize()} study points: {player.study_points[subj]}")
            skip_clear = True
            input(Fore.CYAN + "\n(press ENTER to continue)")

    # --------------------------------------------------
    # look around the room again
    # --------------------------------------------------

    elif command == "look":

        # show the room again but don't clear immediately afterwards
        clear_screen()
        print()
        current_cave.describe()

        inhabitant = current_cave.get_character()

        if inhabitant:
            inhabitant.describe()

        skip_clear = True
        input(Fore.CYAN + "\n(press ENTER to continue)")

    # --------------------------------------------------
    # fight
    # --------------------------------------------------

    elif command == "fight":

        if inhabitant and isinstance(inhabitant, Teacher):

            ascii_fight_intro()
            print(Fore.RED + "\nprepare for battle!")
            ascii_loading("getting ready")

            print(Fore.GREEN)
            player.show_inventory()

            # Offer choice: use item or use study points (if applicable)
            teacher_name = inhabitant.name
            can_use_study = teacher_name in teacher_subject_map
            study_subj = teacher_subject_map.get(teacher_name, None)

            print(Fore.CYAN + "\nChoose your attack method:")
            print("1. Use an item from your inventory")
            if can_use_study:
                print("2. Use study points (" + study_subj + ") - requires at least 50 points per attack")
            print("Enter 1 or 2:")

            choice = input(Fore.YELLOW + "\n> ").strip()

            if choice == "2" and can_use_study:
                # Attempt to use study points
                subj = study_subj
                if player.study_points.get(subj, 0) < 50:
                    print(Fore.RED + f"\nYou don't have enough {subj} study points (need 50).")
                    print(Fore.RED + "The teacher is unimpressed and sends you to detention.")
                    ascii_detention()
                    current_cave = detention
                    skip_clear = False
                    continue

                # consume points for this attack
                player.study_points[subj] -= 50
                print(Fore.MAGENTA + f"\nYou use 50 {subj} study points to attack {teacher_name}!")
                # Determine success chance when using study points
                #make reliable to kinda encourage the player to move around and collect objs
                success_chance = 0.65  # 65% base success
                # Slightly increase chance if you have a lot of points
                extra = min(player.study_points[subj] / 200.0, 0.20)  # up to +20%
                final_chance = success_chance + extra
                roll = random.random()
                if roll < final_chance:
                    # success
                    print(Fore.GREEN + f"\nYour study attack succeeded! You defeated {teacher_name}!")
                    ascii_victory()
                    current_cave.set_character(None)
                    # If it was the principal, check separately (principal not in teacher_subject_map)
                    if inhabitant == principal:
                        print(Fore.GREEN + "\n" + "=" * 50)
                        print("congratulations!")
                        print("you defeated the principal!")
                        print("you escaped quakers hill high!")
                        print("=" * 50)
                        dead = True
                    else:
                        skip_clear = True
                        input(Fore.CYAN + "\n(press ENTER to continue)")
                else:
                    # failure while using study points -> grant an N-award
                    player.n_awards += 1
                    print(Fore.RED + f"\nYour study attack failed! You receive an 'N' award. ({player.n_awards}/3)")
                    if player.n_awards >= 3:
                        print(Fore.RED + "\nYou have received 3 N-awards. The school expels you. Game over.")
                        dead = True
                        break
                    else:
                        print(Fore.RED + "The teacher sends you to detention for a minute!")
                        ascii_detention()
                        current_cave = detention
                        skip_clear = False
                continue

            # default: use item
            fight_with = input(
                Fore.YELLOW + "\nwhat will you fight with? "
            ).strip().lower()

            # make sure the player actually has the item

            if not player.has_item(fight_with):

                print(Fore.RED + "\nyou don't have that item!")
                print(Fore.RED + "the teacher sends you to detention for a minute!")
                ascii_detention()
                current_cave = detention
                skip_clear = False

            else:

                if inhabitant.fight(fight_with):

                    print(Fore.GREEN + f"\nyou defeated {inhabitant.name}!")
                    ascii_victory()

                    # remove the teacher after defeating them

                    current_cave.set_character(None)

                    # check if it was the principal

                    if inhabitant == principal:

                        print(Fore.GREEN + "\n" + "=" * 50)
                        print("congratulations!")
                        print("you defeated the principal!")
                        print("you escaped quakers hill high!")
                        print("=" * 50)

                        dead = True

                    else:
                        skip_clear = True
                        input(Fore.CYAN + "\n(press ENTER to continue)")

                else:

                    print(Fore.RED + "\nthat was the wrong item!")
                    print(Fore.RED + "the teacher sends you to detention for 5 seconds!")
                    ascii_detention()
                    current_cave = detention
                    skip_clear = False

        else:

            print(Fore.RED + "there is nobody here to fight.")
            skip_clear = True
            input(Fore.CYAN + "\n(press ENTER to continue)")

    # --------------------------------------------------
    # help menu
    # --------------------------------------------------

    elif command == "help":

        print(Fore.YELLOW + "\n" + "=" * 50)
        print("help menu")
        print("=" * 50)

        print(Fore.CYAN + "\nmovement")
        print("north")
        print("south")
        print("east")
        print("west")
        print("northeast")
        print("northwest")
        print("southeast")
        print("southwest")

        print(Fore.CYAN + "\nshortcuts")
        print("n s e w ne nw se sw")

        print(Fore.CYAN + "\nactions")
        print("talk")
        print("fight")
        print("take")
        print("inventory")
        print("study")
        print("look")
        print("help")
        print("quit")

        print(Fore.CYAN + "\ngoal")
        print("collect useful items and defeat every teacher.")
        print("finally defeat the principal to escape.")

        skip_clear = True
        input(Fore.CYAN + "\n(press ENTER to continue)")

    # --------------------------------------------------
    # quit the game
    # --------------------------------------------------

    elif command == "quit":

        answer = input(
            Fore.YELLOW + "are you sure you want to quit? (y/n): "
        ).lower()

        if answer == "y":

            print(Fore.GREEN + "\nthanks for playing!")
            dead = True

        else:

            print(Fore.CYAN + "\nok, keep going!")
            skip_clear = True
            time.sleep(1)

    # --------------------------------------------------
    # invalid command
    # --------------------------------------------------

    else:

        print(Fore.RED + "invalid command.")
        skip_clear = True
        input(Fore.CYAN + "\n(press ENTER to continue)")

# =========================================================
# end of game
# =========================================================

print(Fore.YELLOW + "\n" + "=" * 50)
print("game ended.")
print("=" * 50)
