class Board:
    def __init__(self):
        self.top_left = ' '
        self.top_center = ' '
        self.top_right = ' '
        self.middle_left = ' '
        self.middle_center = ' '
        self.middle_right = ' '
        self.bottom_left = ' '
        self.bottom_center = ' '
        self.bottom_right = ' '

    def print_board(self):
        print('{} | {} | {}'.format(self.top_left, self.top_center, self.top_right))
        print(' -------- ')
        print('{} | {} | {}'.format(self.middle_left, self.middle_center, self.middle_right))
        print(' -------- ')
        print('{} | {} | {}'.format(self.bottom_left, self.bottom_center, self.bottom_right))

game_board = Board()

game_board.print_board()