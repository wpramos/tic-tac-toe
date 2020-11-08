import unittest

from tictactoe import Box, Board


class TestFindWinner(unittest.TestCase):
    def setUp(self):
        self.sample_board = Board()

    def tearDown(self):
        pass

    def test_find_winner_diagonal_X(self):
        self.sample_board.top_left.mark = 'X'
        self.sample_board.middle_center.mark = 'X'
        self.sample_board.bottom_right.mark = 'X'

        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(),
                         'X', "Should be 'X'.")

    def test_find_winner_diagonal_O(self):
        self.sample_board.top_right.mark = 'O'
        self.sample_board.middle_center.mark = 'O'
        self.sample_board.bottom_left.mark = 'O'

        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(),
                         'O', "Should be 'O'.")

    def test_find_winner_row_X(self):
        self.sample_board.top_left.mark = 'X'
        self.sample_board.top_center.mark = 'X'
        self.sample_board.top_right.mark = 'X'

        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(),
                         'X', "Should be 'X'.")

    def test_find_winner_row_O(self):
        self.sample_board.bottom_left.mark = 'O'
        self.sample_board.bottom_center.mark = 'O'
        self.sample_board.bottom_right.mark = 'O'

        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(),
                         'O', "Should be 'O'.")

    def test_find_winner_column_X(self):
        self.sample_board.top_left.mark = 'X'
        self.sample_board.middle_left.mark = 'X'
        self.sample_board.bottom_left.mark = 'X'

        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(),
                         'X', "Should be 'X'.")

    def test_find_winner_column_O(self):
        self.sample_board.top_right.mark = 'O'
        self.sample_board.middle_right.mark = 'O'
        self.sample_board.bottom_right.mark = 'O'

        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(),
                         'O', "Should be 'O'.")

    def test_find_winner_blank(self):
        self.sample_board.print_board()

        self.assertEqual(self.sample_board.find_winner(),
                         None, 'Should return None.')


if __name__ == "__main__":
    unittest.main()
