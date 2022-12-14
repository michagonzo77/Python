class Human:
    def __init__(self):
        self.health = 100
        self.armor = 4
        self.strength = 10
        self.mana = 5
        self.name = "Generic Human"

    def attack(self, target):
        print(f"{self.name} attacks {target.name}")
        target.defend(self.strength)

    def defend(self,damage):
        adjusted_damage = damage - self.armor
        self.health -= adjusted_damage
        print(f"{self.name} takes {adjusted_damage} damage, they now have {self.health} HP")

    def heal(self):
        self.health += self.mana
        print(f"{self.name} heals for {self.mana} they now have {self.health} HP")