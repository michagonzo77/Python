class Player:

# Challenge 1
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    def __repr__(self):
        return f"Name: {self.name} \n Age: {self.age} \n Position: {self.position} \n Team: {self.team}"

# Ninja Bonus
    # @classmethod
    # def get_team(cls, player_dict):
    #     new_team = []
    #     for dict in player_dict:
    #         new_team.append(cls(dict))
    #     print(new_team)
    #     return new_team

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            new_team.append(Player(player))
        print(new_team)
        return new_team

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
    }
]

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Challenge 2
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


Player.get_team(players)


# Challenge 3

nuevo_team = []
for player_dict in players:
    nuevo_team.append(Player(player_dict))

print(nuevo_team)