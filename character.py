"""CHARACTER CLASSES"""


class Character:
    """Base character class."""

    def __init__(self, char_name, char_description):

        self.name = char_name
        self.description = char_description
        self.conversation = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def describe(self):

        print(self.name + " is here!")
        print(self.description)

    def talk(self):

        if self.conversation:
            print("[" + self.name + " says]: " + self.conversation)

        else:
            print(self.name + " doesn't want to talk.")

    def fight(self):
        print(self.name + " doesn't want to fight.")
        return False


# =========================================================


class Student(Character):
    """Player class."""

    def __init__(self,
                 char_name,
                 char_description,
                 strength=1,
                 weakness=1,
                 intelligence=1):

        super().__init__(char_name, char_description)

        self.strength = strength
        self.weakness = weakness
        self.intelligence = intelligence

        self.maths = 0
        self.english = 0
        self.coding = 0
        self.science = 0

        self.inventory = []

    # ---------------- Inventory ----------------

    def add_item(self, item):

        self.inventory.append(item)

        print("Picked up", item.get_name())

    def has_item(self, item_name):

        for item in self.inventory:

            if item.get_name().lower() == item_name.lower():
                return True

        return False

    def show_inventory(self):

        print("\nInventory")
        print("---------")

        if len(self.inventory) == 0:
            print("Empty")
            return

        for item in self.inventory:
            print("-", item.get_name())

    # ---------------- Study ----------------

    def study(self):

        print("\nSubjects")
        print("1. maths")
        print("2. english")
        print("3. coding")
        print("4. science")

        choice = input("Choose a subject: ").lower()

        if choice == "maths":

            self.maths += 10
            self.intelligence += 2
            print("You studied Maths.")

        elif choice == "english":

            self.english += 10
            self.intelligence += 1
            print("You studied English.")

        elif choice == "coding":

            self.coding += 15
            self.intelligence += 3
            print("You studied Coding.")

        elif choice == "science":

            self.science += 12
            self.intelligence += 2
            print("You studied Science.")

        else:

            print("Invalid subject.")
            return

        self.show_progress()

    def show_progress(self):

        total = (
            self.maths +
            self.english +
            self.coding +
            self.science
        )

        print("\nStudy Progress")
        print("----------------")
        print("Maths:", self.maths)
        print("English:", self.english)
        print("Coding:", self.coding)
        print("Science:", self.science)
        print("Total:", total)
        print("Intelligence:", self.intelligence)

        if total >= 50:
            self.strength += 1
            print("Level Up! +1 Strength")


# =========================================================


class Teacher(Character):
    """Teacher enemy."""

    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)

        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):

        if combat_item == self.weakness:

            print("You defeated", self.name)
            return True

        print(self.name + " gave you detention.")
        return False


# =========================================================


class EvilTeacher(Teacher):
    """Special boss teacher."""

    def talk(self):

        print("[" + self.name + " snarls]: " + self.conversation)

    def fight(self, combat_item):

        if combat_item == self.weakness:

            print("You defeated the evil", self.name)
            return True

        print(self.name + " unleashes evil homework magic!")
        return False