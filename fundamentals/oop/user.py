class user:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
        else:
            print("User already a member.")
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print(f"Sorry {self.first_name}, you don't have enough points for that.")
        return self

user_1 = user("michael", "gonzalez", "michael@gmail.com", 32)
user_2 = user("ciara", "white", "ciara@gmail.com", 28)
user_3 = user("luna", "lovegood", "luna@gmail.com", 8)



user_1.spend_points(50)
user_2.enroll()
user_2.spend_points(80)

user_1.display_info()
user_2.display_info()
user_3.display_info()

user_2.enroll()