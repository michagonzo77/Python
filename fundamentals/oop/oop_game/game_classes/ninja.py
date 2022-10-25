from game_classes.human import Human

class Ninja(Human):
    def __init__(self,name):
        super().__init__() #super() is a reference to the parent class
        self.mana = 2
        self.name = name

    def dodge(self):
        super().heal()
        print(f"{self.name} has gone invisible and bandaged his wounds and gained {self.mana} HP")

    def heal(self):
        super().heal()
        print(f"The healing cost {self.name} one point of armor")
        self.armor-= 1