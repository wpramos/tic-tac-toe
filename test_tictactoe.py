import unittest
from tictactoe import Box, Board

class TestTicTacToe(unittest.TestCase):
    def test_diagonal_X(self):
        sample_board_1 = Board()
        sample_board_1.top_left.mark = 'X'
        sample_board_1.middle_center.mark = 'X'
        sample_board_1.bottom_right.mark = 'X'
        
        sample_board_1.print_board()

        self.assertEqual(sample_board_1.find_winner(), 'X', "Should be 'X'.")

    def test_diagonal_O(self):
        sample_board_2 = Board()
        sample_board_2.top_right.mark = 'O'
        sample_board_2.middle_center.mark = 'O'
        sample_board_2.bottom_left.mark = 'O'
        
        sample_board_2.print_board()

        self.assertEqual(sample_board_2.find_winner(), 'O', "Should be 'O'.")

if __name__ == "__main__":
    unittest.main()