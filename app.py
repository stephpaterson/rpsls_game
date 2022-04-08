# run this file in the terminal
from computer_player import ComputerPlayer
from player import Player
from game import Game

player_name = input("What's your name? ")
player_choice = input("What would you like to choose? ")

player_1 = Player(player_name, player_choice)
computer = ComputerPlayer()
computer.choice_randomiser()
game = Game(player_1, computer)

print(game.result())

