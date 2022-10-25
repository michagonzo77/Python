class Pet:

    def __init__(self):
        self.health = 100
        self.energy = 100

    def sleep(self):
        print("zzzzzzz")
        self.energy += 25
        return self

    def eat(self):
        print("munch munch munch")
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def make_noise(self):
        print(self.noise)
        return self

    def __repr__(self):
        return (self.name) 
