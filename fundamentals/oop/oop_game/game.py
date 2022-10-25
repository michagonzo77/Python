from game_classes.pirate import Pirate
from game_classes.ninja import Ninja
import random

player_1 = Ninja("John Wick")
enemy = Pirate("Jack Sparrow")

print("Welcome to the game!")
while( player_1.health > 0 and enemy.health > 0):
    response = ""
    while not response == "1" and not response == "2":
        print("You are the ninja, will you \n 1)Attack \n 2)Heal")
        response = input(">>>")
        if response == "1":
            if random.randint(1,10) <= 6:
                player_1.attack(enemy)
            else:
                enemy.parry()
        elif response == "2":
            player_1.heal()
        else:
            print("please select a valid option")
    enemy_action = random.randint(1,3)
    if enemy.health <= 0:
        break
    if enemy_action == 1:
        if random.randint(1,10) <= 8:
            enemy.attack(player_1)
        else:
            player_1.dodge()
    if enemy_action == 2:
        enemy.chug_rum()
    if enemy_action == 3:
        enemy.heal()

if enemy.health <= 0:
    print(f"You have defeated {enemy.name}")
else:
    print(f"The mighty ninja has fallen")