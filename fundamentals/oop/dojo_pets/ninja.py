from pet import Pet
from pet_classes.dog import Dog

class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} take's {self.pet} for a walk")
        self.pet.play()
        return self

    def feed(self):
        print(f"Feed {self.pet} some {self.pet_food}")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"It's time for {self.pet}'s bath.")
        self.pet.make_noise()
        return self

