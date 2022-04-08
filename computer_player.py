import random

class ComputerPlayer:
    
    def __init__(self, choice):
        self.name = "computer"
        self.choice = choice
    
    def choice_randomiser():
        choices = ["rock", "paper", "scissors", "lizard", "spock"]
        return random.choice(choices)
