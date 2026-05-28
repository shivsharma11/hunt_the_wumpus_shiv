"""CHARACTER CLASS"""
class Character():
    '''defines thre character class'''
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def set_conversation(self, conversation):
        '''character dialouge'''
        self.conversation = conversation

    def describe(self):
        '''outputs description of the character'''
        print(self.name + " is here!")
        print(self.description)

    def talk(self):
        '''manages talking to the character'''
        if self.conversation is not None:
            print("[" + self.name + " says] : " + self.conversation)
        else:
            print(self.name + " doesnt want to talk to you.")


    def fight(self):
        '''manages fighting with the character'''
        print(self.name + " doesn't want to engage in combat.")
