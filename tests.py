import os


if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

import unittest
from tkinter import *
from unittest.mock import MagicMock
import celebration

class TestRPSGame(unittest.TestCase):
    def setUp(self):
        self.root = Tk()  # Create a Tkinter root window
        self.game = celebration.RPSGame(self.root)

    def tearDown(self):
        self.root.destroy()  # Destroy the Tkinter root window after each test

    def test_ui_elements(self):
        self.assertIsInstance(self.game.label_bot, Label)
        self.assertIsInstance(self.game.label_player, Label)
        self.assertIsInstance(self.game.button_rock, Button)
        self.assertIsInstance(self.game.button_paper, Button)
        self.assertIsInstance(self.game.button_scissors, Button)
        # Add more assertions for other UI elements if needed

    def test_winner_check_player_wins(self):
        self.game.msg_updation = MagicMock()
        self.game.player_update = MagicMock()
        self.game.bot_update = MagicMock()
        self.game.tie_update = MagicMock()
        self.game.winner_check("rock", "scissors")
        self.game.msg_updation.assert_called_with("Player Wins")
        self.game.player_update.assert_called()
        self.game.bot_update.assert_not_called()
        self.game.tie_update.assert_not_called()

    def test_winner_check_bot_wins(self):
        self.game.msg_updation = MagicMock()
        self.game.player_update = MagicMock()
        self.game.bot_update = MagicMock()
        self.game.tie_update = MagicMock()
        self.game.winner_check("rock", "paper")
        self.game.msg_updation.assert_called_with("Bot Wins")
        self.game.player_update.assert_not_called()
        self.game.bot_update.assert_called()
        self.game.tie_update.assert_not_called()

    def test_winner_check_tie(self):
        self.game.msg_updation = MagicMock()
        self.game.player_update = MagicMock()
        self.game.bot_update = MagicMock()
        self.game.tie_update = MagicMock()
        self.game.winner_check("rock", "rock")
        self.game.msg_updation.assert_called_with("It's a tie!!")
        self.game.player_update.assert_not_called()
        self.game.bot_update.assert_not_called()
        self.game.tie_update.assert_called()

if __name__ == '__main__':
    unittest.main()