import unittest
from tictactoe import Box, Board

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.sample_board = Board()

    def test_diagonal_X(self):
        self.sample_board.top_left.mark = 'X'
        self.sample_board.middle_center.mark = 'X'
        self.sample_board.bottom_right.mark = 'X'
        
        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(), 'X', "Should be 'X'.")

    def test_diagonal_O(self):
        self.sample_board.top_right.mark = 'O'
        self.sample_board.middle_center.mark = 'O'
        self.sample_board.bottom_left.mark = 'O'
        
        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(), 'O', "Should be 'O'.")

if __name__ == "__main__":
    unittest.main()