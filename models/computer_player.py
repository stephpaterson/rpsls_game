import random

class ComputerPlayer:
    
    def __init__(self):
        self.name = "computer"
        self.choice = None
    
    def choice_randomiser(self):
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        self.choice =random.choice(choices)
