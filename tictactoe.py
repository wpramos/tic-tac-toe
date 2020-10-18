import random

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
        print('\n{} | {} | {}'.format(self.top_left, self.top_center, self.top_right))
        print(' ------- ')
        print('{} | {} | {}'.format(self.middle_left, self.middle_center, self.middle_right))
        print(' ------- ')
        print('{} | {} | {}\n'.format(self.bottom_left, self.bottom_center, self.bottom_right))

def play_game():
    print("\nLet's play...")
    game_board = Board()
    game_board.print_board()
    print('Please make your move...\n\n[Respond with a combination' + 
    'of Top/Middle/Bottom\n and Left/Center/Right separated' + 
    'with a hyphen.\n For instance, Top-Right/Bottom-Center]')

game_count = 0

while True:
    question = ['Do you wanna play Tic Tac Toe..?', 'Do you wanna play again..?', 'Another game..?', 'Shall we give that another try..?', 'Are you up for one more..?']
    if game_count == 0:
        play_or_not = input('{} [Respond with Y or N]\n'.format(question[0])).upper()
    else:
        play_or_not = input('{} [Respond with Y or N]\n'.format(question[random.randint(1,4)])).upper()

    if play_or_not == 'Y':
        play_game()
        game_count += 1
    elif play_or_not == 'N':
        print('Fine! See ya later...')
        break
    else:
        print('Either a Y or an N, please.')


