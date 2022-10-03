from unittest import TestCase, main
from home_work_1.tic_tac_toe import TicTacGame


class TicTacGameTest(TestCase):
    def setUp(self):
        self.tic_tac_game = TicTacGame()

    def test_validate_input(self):
        self.assertEqual(self.tic_tac_game.validate_input("5"), 0)

    def test_wrong_type(self):
        self.assertRaises(TypeError, self.tic_tac_game.validate_input, "abc")

    def test_wrong_index(self):
        self.assertRaises(IndexError, self.tic_tac_game.validate_input, "10")


if __name__ == '__main__':
    main()
