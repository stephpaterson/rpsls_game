import unittest

from models.game import Game
from models.player import Player


class TestGame(unittest.TestCase):


    def setUp(self):
        self.player_1 = Player("Steph", "scissors")
        self.player_2 = Player("Greg", "lizard")
        self.game = Game(self.player_1, self.player_2)

    # @unittest.skip
    def test_player_has_choice(self):
        self.assertEqual("scissors", self.player_1.choice)

    # @unittest.skip
    def test_scissors_beats_lizard(self):
        self.assertEqual("player 1 wins", self.game.result())

    def test_lizard_loses_rock(self):
        self.player_3 = Player("Dex", "lizard")
        self.player_4 = Player("Iris", "rock")
        self.game = Game(self.player_3, self.player_4)
        self.assertEqual("player 2 wins", self.game.result())

    def test_draw(self):
        self.player_3 = Player("Dex", "lizard")
        self.player_2 = Player("Greg", "lizard")
        self.game = Game(self.player_3, self.player_2)
        self.assertEqual("it's a draw", self.game.result())
