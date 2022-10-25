from pet import Pet

class Dog(Pet):
    def __init__(self, name, type_pet, tricks, noise):
        super().__init__()
        self.type_pet = type_pet
        self.tricks = tricks
        self.name = name
        self.noise = noise

    # def make_noise(self):
    #     print(self.noise)
    #     return self