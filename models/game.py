class Game:
    
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result_lookup = {
            "scissors" : ["paper", "lizard"],
            "paper" : ["rock", "spock"],
            "rock" : ["lizard", "scissors"],
            "lizard" : ["spock", "paper"],
            "spock" : ["scissors", "rock"]
        }

    def result(self):
        if self.player_1.choice == self.player_2.choice:
            return "it's a draw"
        loser = self.result_lookup[self.player_1.choice]
        if self.player_2.choice in loser:
            return f"{self.player_1.name} wins!"
        else:
            return f"{self.player_2.name} wins!"

