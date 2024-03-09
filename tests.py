import unittest
import celebration
from tkinter import *

class TestRPSImageLoader(unittest.TestCase):
    def setUp(self):
        self.loader = celebration.RPSImageLoader()

    def test_images_loaded(self):
        self.assertIsNotNone(self.loader.image_rock)
        self.assertIsNotNone(self.loader.image_paper)
        self.assertIsNotNone(self.loader.image_scissors)
        self.assertIsNotNone(self.loader.image_YouDefault)
        self.assertIsNotNone(self.loader.image_BotDefault)
        # Add more assertions for other images if needed

class TestRPSGame(unittest.TestCase):
    def setUp(self):
        self.window = Tk()
        self.game = celebration.RPSGame(self.window)

    def test_ui_elements(self):
        self.assertIsInstance(self.game.label_bot, Label)
        self.assertIsInstance(self.game.label_player, Label)
        self.assertIsInstance(self.game.button_rock, Button)
        self.assertIsInstance(self.game.button_paper, Button)
        self.assertIsInstance(self.game.button_scissors, Button)
        # Add more assertions for other UI elements if needed

class TestWinnerCheck(unittest.TestCase):
    def setUp(self):
        self.window = Tk()
        self.game = celebration.RPSGame(self.window)

    def test_player_wins(self):
        player_choice = "rock"
        bot_choice = "scissors"
        self.game.winner_check(player_choice, bot_choice)
        self.assertEqual(self.game.final_message["text"], "Player Wins")

    def test_bot_wins(self):
        player_choice = "paper"
        bot_choice = "scissors"
        self.game.winner_check(player_choice, bot_choice)
        self.assertEqual(self.game.final_message["text"], "Bot Wins")

    def test_tie(self):
        player_choice = "rock"
        bot_choice = "rock"
        self.game.winner_check(player_choice, bot_choice)
        self.assertEqual(self.game.final_message["text"], "It's a tie!!")

if __name__ == '__main__':
    unittest.main()