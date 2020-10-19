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
        '''This method displays a visual representation of the board in the console.'''
        print('\n{} | {} | {}'.format(self.top_left, self.top_center, self.top_right))
        print(' ------- ')
        print('{} | {} | {}'.format(self.middle_left, self.middle_center, self.middle_right))
        print(' ------- ')
        print('{} | {} | {}\n'.format(self.bottom_left, self.bottom_center, self.bottom_right))

def play_game():
    '''This function launches the game.'''
    print("\nLet's play...")
    game_board = Board()
    game_board.print_board()
    print('Please make your move...\n\nRespond with a combination of Top/Middle/Bottom\nand Left/Center/Right, separated with a hyphen.\n\nFor instance, "Top-Right"/"Bottom-Center"\n')
    
    while True:
        player_move = input('Your Move: ').lower().replace('-', '_')
        if hasattr(game_board, player_move):
            setattr(game_board, player_move, 'X')
            game_board.print_board()
        else:
            print('\nRespond with a combination of Top/Middle/Bottom\nand Left/Center/Right, separated with a hyphen.\n\nFor instance, "Top-Right"/"Bottom-Center"\n')

game_count = 0
rebound = False

while True:
    question = ['Do you wanna play Tic Tac Toe..?', 'Do you wanna play again..?', 'Another game..?', 'Shall we give that another try..?', 'Are you up for one more..?']
    if rebound:
        # TO CHECK IF THIS IS A REBOUNDED INPUT REQUEST
        yes_or_no = input().upper()
    elif game_count == 0:
        # TO CHECK IF THIS IS THE FIRST GAME OF SESSION
        yes_or_no = input('{} [Respond with Y or N]\n'.format(question[0])).upper()
    else:
        # NEITHER A REBOUNDED INPUT REQUEST NOR THE FIRST GAME OF SESSION
        yes_or_no = input('{} [Respond with Y or N]\n'.format(question[random.randint(1,4)])).upper()

    if yes_or_no == 'Y':
        # IF THE USER WISHES TO PLAY
        play_game()
        game_count += 1
        rebound = False
    elif yes_or_no == 'N':
        # IF THE USER WISHES NOT TO PLAY
        print('Fine! See ya later...')
        break
    else:
        # THIS IS THE CASE OF A REBOUNDED INPUT REQUEST, WHERE THE USER HAS 
        # NEITHER PASSED A 'Y' OR AN 'N' AS THE INPUT
        print('Either a Y or an N, please.')
        rebound = True