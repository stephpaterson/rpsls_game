# run this file in the terminal
from xml.etree.ElementTree import tostring
from computer_player import ComputerPlayer
from player import Player
from game import Game

choices = ["scissors", "paper", "rock", "lizard", "spock"]

def display_choices(choices):
    for index, choice in enumerate(choices):
        print(f"{index + 1} - {choice}")

def find_by_index(choices, player_str):
    player_num = int(player_str)
    return choices[(player_num-1)]


player_name = input("What's your name? ")
print("Choose your hand...")
display_choices(choices)

player_str = input("What's the number of your choice? ")
player_choice = find_by_index(choices, player_str)

player_1 = Player(player_name, player_choice)
computer = ComputerPlayer()
computer.choice_randomiser()
game = Game(player_1, computer)

print(f"The computer chose {computer.choice} and {player_1.name} chose {player_1.choice}")
print(game.result())

