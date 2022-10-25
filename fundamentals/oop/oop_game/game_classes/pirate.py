from game_classes.human import Human

class Pirate(Human):
    def __init__(self,name):
        super().__init__()
        self.mana = 1
        self.strength = 12
        self.name = name
        self.rum = "bottle of rum"

    def parry(self):
        print(f"{self.name} has parried the attack")

    def chug_rum(self):
        super().heal()
        print(f"The Pirate chugs their {self.rum} and it fills them with brute force (Strength +4)")
        self.strength += 4

    def heal(self):
        super().heal()
        print(f"The healing cost {self.name} one point of armor")
        self.armor-= 1