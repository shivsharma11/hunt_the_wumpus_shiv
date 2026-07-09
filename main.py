from character import Character, Teacher, EvilTeacher, Student
from item import Item
from cave import Classroom

dead = False

#ITEMS

calculator = Item("calculator", "A scientific calculator.")

dictionary = Item("dictionary", "A giant Oxford dictionary.")

fantasy_book = Item("fantasy book", "A magical fantasy novel.")

pylint = Item("pylint", "A code analysis program.")

# ---------------------------------------------------------
# ROOM CREATION 
# ---------------------------------------------------------

entrance = Classroom("Entrance")

hall1 = Classroom("Hall")
hall2 = Classroom("Hall")
hall3 = Classroom("Hall")
hall4 = Classroom("Hall")
hall5 = Classroom("Hall")
hall6 = Classroom("Hall")
hall7 = Classroom("Hall")
hall8 = Classroom("Hall")
hall9 = Classroom("Hall")

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
m_faculty1 = Classroom("M. Faculty 1")
m_faculty2 = Classroom("M. Faculty 2")

english_classroom = Classroom("English")
hsie = Classroom("HSIE")
pe1 = Classroom("PE 1")
pe2 = Classroom("PE 2")

evil_english1 = Classroom("English")

library.set_item(dictionary)

canteen.set_item(calculator)

biology.set_item(fantasy_book)

computer_lab.set_item(pylint)

# ---------------------------------------------------------
# ROOM DESCRIPTIONS
# ---------------------------------------------------------

entrance.set_description("...enter at your own risk")
hall1.set_description("A busy hall full of students.")
hall2.set_description("A busy hall full of students.")
hall3.set_description("A busy hall full of students.")
hall4.set_description("A busy hall full of students.")
hall5.set_description("A busy hall full of students.")
hall6.set_description("A busy hall full of students.")
hall7.set_description("A busy hall full of students.")
hall8.set_description("A busy hall full of students.")
hall9.set_description("A busy hall full of students.")

principal_office.set_description("The principal's office. You are intimidated by his aura.")
exit_room.set_description("FREEDOM. You have escaped the horrors of this highschool.")

cafe.set_description("A cozy cafe with snacks.")
canteen.set_description("A noisy canteen full of chatter.")
library.set_description("A quiet library full of books.")
oval.set_description("A large oval outside.")
detention.set_description("A dark room for troublemakers.")

computer_lab.set_description("A glowing room full of computers.")
biology.set_description("Biology lab with specimens.")
physics.set_description("Physics lab with equipment.")
chemistry.set_description("Chemistry lab with chemicals.")

math_classroom.set_description("The main mathematics classroom.")
m_faculty1.set_description("Math Faculty Office 1.")
m_faculty2.set_description("Math Faculty Office 2.")

english_classroom.set_description("The main English classroom.")
hsie.set_description("Human Society and Its Environment.")
pe1.set_description("Physical Education Area 1.")
pe2.set_description("Physical Education Area 2.")

# ---------------------------------------------------------
# ROOM LINKS 
# ---------------------------------------------------------

#entering the school (initial spawnpoint) 
entrance.set_link_classroom(hall1, "west")

# Hall main connections

#HALL 1
hall1.set_link_classroom(math_classroom, "north")
hall1.set_link_classroom(english_classroom, "south")
hall1.set_link_classroom(hall2, "southwest")
hall1.set_link_classroom(entrance, "east")

#HALL 2
hall2.set_link_classroom(hsie, "west")
hall2.set_link_classroom(evil_english1, "east")
hall2.set_link_classroom(oval, "south")
hall2.set_link_classroom(oval, "southwest")
hall2.set_link_classroom(hall1, "northeast")
hall2.set_link_classroom(hall3, "north")
hall2.set_link_classroom(hall4, "northwest")

#HALL3
hall3.set_link_classroom(hall1, "east")
hall3.set_link_classroom(hall2, "south")
hall3.set_link_classroom (hall4, "west")

#HALL 4
hall4.set_link_classroom(chemistry, "north")
hall4.set_link_classroom(hsie, "south")
hall4.set_link_classroom(pe1, "southwest")
hall4.set_link_classroom(physics, "northwest")
hall4.set_link_classroom(hall5, "west")
hall4.set_link_classroom(hall2, "southeast")

#HALL 5
hall5.set_link_classroom(physics, "north")
hall5.set_link_classroom(biology, "northwest")
hall5.set_link_classroom(canteen, "southwest")
hall5.set_link_classroom(pe1, "south")
hall5.set_link_classroom(hall6, "west")
hall5.set_link_classroom(hall4, "east")
hall5.set_link_classroom(hsie, "southeast")

#HALL 6
hall6.set_link_classroom(hall5, "east")
hall6.set_link_classroom(biology, "north")
hall6.set_link_classroom(library, "west")
hall6.set_link_classroom(computer_lab, "northwest")
hall6.set_link_classroom(physics, "northeast")
hall6.set_link_classroom(canteen, "south")
hall6.set_link_classroom(pe1, "southwest")


#CLASSROOMS & MISC. 

#MATH WING
math_classroom.set_link_classroom(m_faculty1, "north")
math_classroom.set_link_classroom(hall1, "south")
m_faculty1.set_link_classroom(math_classroom, "south")

#ENGLISH WING
english_classroom.set_link_classroom(hall1, "north")
english_classroom.set_link_classroom(hall2, "west")
english_classroom.set_link_classroom(evil_english1, "south")
evil_english1.set_link_classroom(english_classroom, "north")
evil_english1.set_link_classroom(hall2, "northwest")

#SCIENCE WING
chemistry.set_link_classroom(hall4, "south")
chemistry.set_link_classroom(physics, "west")
chemistry.set_link_classroom(hall5, "southwest")
chemistry.set_link_classroom(hall3, "southeast")

physics.set_link_classroom(chemistry, "east")
physics.set_link_classroom(hall4, "southeast")
physics.set_link_classroom(hall5, "south")
physics.set_link_classroom(hall6, "southwest")
physics.set_link_classroom(biology, "west")

biology.set_link_classroom(computer_lab, "west")
biology.set_link_classroom(library, "southwest")
biology.set_link_classroom(physics, "east")
biology.set_link_classroom(hall6, "south")
biology.set_link_classroom(hall5, "southeast")


#HSIE AND PE WING
hsie.set_link_classroom(pe1, "west")
hsie.set_link_classroom(hall4, "north")
hsie.set_link_classroom(hall5, "northwest")
hsie.set_link_classroom(hall3, "northeast")
hsie.set_link_classroom(hall2, "east")

pe1.set_link_classroom(hsie, "east")
pe1.set_link_classroom(oval, "south")
pe1.set_link_classroom(canteen, "west")
pe1.set_link_classroom(hall6, "northwest")
pe1.set_link_classroom(hall5, "north")
pe1.set_link_classroom(hall4, "northeast")

#OFFICE WING
#add the links if you can't think of a way to add a maze/tool finding quest thing


# ---------------------------------------------------------
# TEACHERS (evil + normal)
# ---------------------------------------------------------


player = Student("Shivansh", "A stressed Year 11 student.")
current_cave = entrance
player.add_item("calculator")
player.add_item("dictionary")

# Principal (evil)
principal = EvilTeacher("Prin C. Pal", "The principal of the school")
principal.set_conversation("You dare enter my domain?")
principal.set_weakness("aura")
principal_office.set_character(principal)

# Evil Math Teacher 
evil_math = EvilTeacher("Mr. Algebra", "A furious math teacher.")
evil_math.set_conversation("Your equations are WRONG!")
evil_math.set_weakness("calculator")
math_classroom.set_character(evil_math)

# English Wing (ALL evil)
evil_english1 = EvilTeacher("Ms. Grammar", "She corrects your speech aggressively.")
evil_english1.set_conversation("Your grammar is atrocious!")
evil_english1.set_weakness("dictionary")
english_classroom.set_character(evil_english1)

# Computer Lab (evil)
evil_computer = EvilTeacher("Mr. Brooks", "He throws keyboards at you.")
evil_computer.set_conversation("Your code is full of bugs!")
evil_computer.set_weakness("pylint")
computer_lab.set_character(evil_computer)

# Science Wing (normal)
science_teacher = EvilTeacher("Dr. Atom", "A calm science teacher.")
science_teacher.set_conversation("I will split YOUR atoms!")
science_teacher.set_weakness("fantasy book")
physics.set_character(science_teacher)

# ---------------------------------------------------------
# STARTING ROOM
# ---------------------------------------------------------

current_cave = entrance


# Navigation
valid_directions = [
    "north", "south", "east", "west",
    "northeast", "northwest",
    "southeast", "southwest"
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

while not dead:

    print()
    current_cave.describe()

    inhabitant = current_cave.get_character()

    if inhabitant:
        inhabitant.describe()

    command = input("> ").lower()

    if command in direction_aliases:
        command = direction_aliases[command]

    if command in valid_directions:
        current_cave = current_cave.move(command)

    elif command == "talk":
        if inhabitant:
            inhabitant.talk()
    
        else:
            print("There is nobody here.")
    
    elif command == "inventory":
        player.show_inventory()

    elif command == "fight":
        if inhabitant and isinstance(inhabitant, EvilTeacher):
            fight_with = input("Fight with: ").lower()

            if not player.has_item(fight_with):
                print("You don't have that item!")
            elif inhabitant.fight(fight_with):
                print("You won!")
                current_cave.set_character(None)
            else:
                print("Game over")
                dead = True

        else:
            print("There is nobody to fight.")

    else: 
        print("Invalid Command.")
    





