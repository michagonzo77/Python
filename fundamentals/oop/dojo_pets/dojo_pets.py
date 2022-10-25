from ninja import Ninja
from pet import Pet
from pet_classes.dog import Dog

luna = Dog("luna", "dog", "roll over", "bark")
michael = Ninja("Michael", "Gonzalez", 25, "kibble", luna)
# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

# luna = Pet("luna", "dog", "sit", 100, 100)
# michael = Ninja("Michael", "Gonzalez", 25, "kibble", "luna")
michael.walk()
michael.feed()

print(isinstance(luna, Dog))
michael.bathe()