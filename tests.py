import unittest
import io
import sys
import contextlib
from unittest.mock import patch, MagicMock

import pygame
import tkinter as tk
from PIL import Image, ImageTk

# Replace the following import with the actual file path if needed
import celebration  # noqa: F401


class TestRPSGameV2(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self.game = celebration.RPSGame(self.window)
        self.window.update()

    def tearDown(self):
        self.window.destroy()

    @patch('pygame.mixer.Sound.play')
    def test_sound_click(self, mock_sound_play):
        self.game.sound_click.play = mock_sound_play
        self.game.on_button_click("rock")
        mock_sound_play.assert_called_once()

    @patch('pygame.mixer.Sound.play')
    def test_sound_player_win(self, mock_sound_play):
        self.game.sound_player_win.play = mock_sound_play
        self.game.winner_check("rock", "scissors")
        mock_sound_play.assert_called_once()

    @patch('pygame.mixer.Sound.play')
    def test_sound_bot_win(self, mock_sound_play):
        self.game.sound_bot_win.play = mock_sound_play
        self.game.winner_check("paper", "rock")
        mock_sound_play.assert_called_once()

    def test_update_choice(self):
        self.game.update_choice("rock")
        self.assertEqual(self.game.label_player.cget("image"), self.game.image_loader.image_RU)

    def test_winner_check_tie(self):
        self.game.winner_check("rock", "rock")
        self.assertEqual(self.game.final_message.cget("text"), "It's a tie!!")

    def test_winner_check_player_win(self):
        self.game.winner_check("rock", "scissors")
        self.assertEqual(self.game.final_message.cget("text"), "Player Wins")

    def test_winner_check_bot_win(self):
        self.game.winner_check("paper", "rock")
        self.assertEqual(self.game.final_message.cget("text"), "Bot Wins")

    def test_bot_update(self):
        self.game.bot_update()
        self.assertEqual(self.game.bot_score, 1)

    def test_player_update(self):
        self.game.player_update()
        self.assertEqual(self.game.player_score, 1)

if __name__ == "__main__":
    unittest.main(argv=['first_arg_is_ignored'], exit=False)