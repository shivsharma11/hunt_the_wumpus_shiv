"""character class"""

class Character:
    '''base character class'''

    def __init__(self, char_name, char_description):
        # basic character attributes
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def set_conversation(self, conversation):
        '''sets dialogue'''
        self.conversation = conversation

    def describe(self):
        '''prints character description'''
        print(self.name + " is here!")
        print(self.description)

    def talk(self):
        '''handles dialogue'''
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk.")

    def fight(self):
        '''default combat behaviour'''
        print(self.name + " doesn't want to engage in combat.")
        return False


class Student(Character):
    '''student class'''

    def __init__(self, char_name, char_description,
                 strength=1, weakness=1, intelligence=1):

        super().__init__(char_name, char_description)

        # student stats
        self.strength = strength
        self.weakness = weakness
        self.intelligence = intelligence

        # subject points
        self.maths = 0
        self.english = 0
        self.coding = 0
        self.science = 0

    def study(self):
        '''allows the player to study subjects'''

        print("\nsubjects:")
        print("1. maths")
        print("2. english")
        print("3. coding")
        print("4. science")

        choice = input("choose a subject: ").lower()

        if choice == "maths":
            self.maths += 10
            self.intelligence += 2
            print("you studied maths (+10 points)")

        elif choice == "english":
            self.english += 10
            self.intelligence += 1
            print("you studied english (+10 points)")

        elif choice == "coding":
            self.coding += 15
            self.intelligence += 3
            print("you studied coding (+15 points)")

        elif choice == "science":
            self.science += 12
            self.intelligence += 2
            print("you studied science (+12 points)")

        else:
            print("invalid subject")
            return

        # display updated stats
        self.show_progress()
    def show_progress(self):
        '''shows current study progress'''
        print("\nstudy progress")
        print("----------------")
        print("maths:", self.maths)
        print("english:", self.english)
        print("coding:", self.coding)
        print("science:", self.science)
        total = (
            self.maths
            + self.english
            + self.coding
            + self.science
        )
        print("total points:", total)
        print("intelligence:", self.intelligence)

        # bonus rewards

        if total >= 50:
            self.strength += 1
            print("level up! +1 strength")


class Teacher(Character):
    '''teacher enemy class'''
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(
                "you defeated "
                + self.name
                + " using "
                + combat_item
            )
            return True

        else:
            print(
                self.name
                + " gave you detention. you lose."
            )
            return False


class EvilTeacher(Teacher):
    '''special teacher subclass'''
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)