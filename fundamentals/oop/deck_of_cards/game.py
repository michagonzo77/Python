from classes.deck import Deck

bicycle = Deck()

# bicycle.show_cards()

# bicycle.pick_cards()

# player.hand.append(deck.pick_card())


response = ""
while not response == "1" and not response == "2":
    print("Would you like to hit? \n 1)Hit \n 2)Stay")
    response = input(">>>")
    if response == "1":
        bicycle.pick_cards()
    else:
        print("testing")
