import unittest
import pygame
import celebration

class TestRPSGame(unittest.TestCase):
    def test_game_window(self):
        self.assertEqual(self.window.title(), "Rock, Paper & Scissors")
        self.assertEqual(self.window.geometry(), '1500x850')
        self.assertEqual(self.window.winfo_bg(), 'white')

    def test_background_music(self):
        pygame.mixer.init()
        self.assertEqual(pygame.mixer.get_busy(), True)

    def test_default_images(self):
        self.assertEqual(self.game.label_bot.cget('image'), self.game.image_loader.image_BotDefault)
        self.assertEqual(self.game.label_player.cget('image'), self.game.image_loader.image_YouDefault)

    def test_button_click(self):
        self.button_rock = self.game.button_rock
        self.button_rock.invoke()
        self.assertEqual(self.game.label_player.cget('image'), self.game.image_loader.image_RU)

    def test_tie(self):
        self.game.winner_check('rock', 'rock')
        self.assertEqual(self.game.final_message.cget('text'), 'It\'s a tie!!')
        self.assertEqual(self.game.label_celebrate_tie.winfo_ismapped(), True)

    def test_player_win(self):
        self.game.winner_check('rock', 'scissors')
        self.assertEqual(self.game.final_message.cget('text'), 'Player Wins')
        self.assertEqual(self.game.player_score_label.cget('text'), '1')
       