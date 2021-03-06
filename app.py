from models.computer_player import ComputerPlayer
from models.player import Player
from models.game import Game

choices = ["scissors", "paper", "rock", "lizard", "spock"]

def display_choices(choices):
    for index, choice in enumerate(choices):
        print(f"{index + 1} - {choice}")

def find_by_index(choices, player_str):
    player_num = int(player_str)
    return choices[(player_num-1)]


player_name = input("What's your name? ")

while True:
    
    print("Choose your hand...")
    display_choices(choices)
    player_input = int(input("What's the number of your choice? "))
    if player_input not in range(1,6):
        print("-----------")
        print("Sorry you need to pick a number bewteen 1 and 5")
        print("-----------")
    else:
        player_choice = find_by_index(choices, player_input)

        player_1 = Player(player_name, player_choice)
        computer = ComputerPlayer()
        computer.choice_randomiser()
        game = Game(player_1, computer)

        print(f"The computer chose {computer.choice} and {player_1.name} chose {player_1.choice}")
        print(game.result())
        play_again = input("would you like to play again? (y/n)")
        if play_again.lower() == "n":
            break

