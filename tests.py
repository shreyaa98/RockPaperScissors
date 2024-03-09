import unittest
from unittest.mock import patch
from io import StringIO
from celebration import RPSGame

class TestRPSGame(unittest.TestCase):
    def setUp(self):
        self.window = StringIO()

    def tearDown(self):
        self.window.close()

    @patch('sys.stdout', new_callable=StringIO)
    def test_setup_ui(self, mock_stdout):
        game = RPSGame(self.window)
        game.setup_ui()
        expected_output = "UI setup completed successfully"
        self.assertIn(expected_output, mock_stdout.getvalue())

    def test_winner_check(self):
        game = RPSGame(self.window)
        game.player_score = 2
        game.bot_score = 1
        game.winner_check("rock", "paper")
        self.assertEqual(game.player_score, 2)
        self.assertEqual(game.bot_score, 2)

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()