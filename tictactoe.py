import random, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.disable(logging.DEBUG)

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

        self.available_spaces = ['top_left', 'top_center', 'top_right', 'middle_left', 'middle_center', 'middle_right', 'bottom_left', 'bottom_center', 'bottom_right']

    def user_move(self, move_count):
        '''This method requests user input and executes the user's move.'''
        logging.debug("Scope: Board class' user_move() method")
        if move_count < 2:
            print('Please make your move...\n\nRespond with a combination of Top/Middle/Bottom\nand Left/Center/Right, separated with a hyphen.\n\nFor instance, "Top-Right"/"Bottom-Center"\n')
        while True:
            player_move = input('Your Move: ').lower().replace('-', '_')
            if hasattr(self, player_move):
                setattr(self, player_move, 'X')
                self.available_spaces.remove(player_move)
                self.print_board()
                return
            else:
                print('\nTry "Top-Left", for instance.\n')
                continue

    def computer_move(self):
        '''This method executes the computer's move.'''
        logging.debug("Scope: Board class' computer_move() method")
        print("Machine's Move: ")
        machine_move = self.available_spaces[random.randint(0, len(self.available_spaces) - 1)]
        setattr(self, machine_move, 'O')
        self.available_spaces.remove(machine_move)
        self.print_board()

    def are_spaces_filled(self):
        '''This method checks to see if every space in the board is filled.'''
        if len(self.available_spaces) == 0:
            return True
        else:
            return False

    def find_winner(self):
        def is_this_complete(first, second, third):
            if first == second == third and first == 'X':
                return [True, 'X']
            elif first == second == third and first == 'O':
                return [True, 'O']
            else:
                return[False]

        if is_this_complete(self.top_left, self.top_center, self.top_right)[0]:
            return is_this_complete(self.top_left, self.top_center, self.top_right)[1]    
        elif is_this_complete(self.middle_left, self.middle_center, self.middle_right)[0]:
            return is_this_complete(self.middle_left, self.middle_center, self.middle_right)[1]
        elif is_this_complete(self.bottom_left, self.bottom_center, self.bottom_right)[0]:
            return is_this_complete(self.bottom_left, self.bottom_center, self.bottom_right)[1]

        elif is_this_complete(self.top_left, self.middle_left, self.bottom_left)[0]:
            return is_this_complete(self.top_left, self.middle_left, self.bottom_left)[1]
        elif is_this_complete(self.top_center, self.middle_center, self.bottom_center)[0]:
            return is_this_complete(self.top_center, self.middle_center, self.bottom_center)[1]
        elif is_this_complete(self.top_right, self.middle_right, self.bottom_right)[0]:
            return is_this_complete(self.top_right, self.middle_right, self.bottom_right)[1]

        elif is_this_complete(self.top_left, self.middle_center, self.bottom_right)[0]:
            return is_this_complete(self.top_left, self.middle_center, self.bottom_right)[1]
        elif is_this_complete(self.top_right, self.middle_center, self.bottom_left)[0]:
            return is_this_complete(self.top_right, self.middle_center, self.bottom_left)[1]
        else:
            return None


    def print_board(self):
        '''This method displays a visual representation of the board in the console.'''
        print('\n{} | {} | {}'.format(self.top_left, self.top_center, self.top_right))
        print(' ------- ')
        print('{} | {} | {}'.format(self.middle_left, self.middle_center, self.middle_right))
        print(' ------- ')
        print('{} | {} | {}\n'.format(self.bottom_left, self.bottom_center, self.bottom_right))

def play_game():
    '''This function launches the game.'''
    logging.debug("Scope: play_game() function")
    print("\nLet's play...")
    game_board = Board()
    game_board.print_board()

    m_count = random.randint(0, 1) # THE VARIABLE SPECIFIES THE MOVE_NUMBER
    while True:
        if m_count % 2 == 0:
            game_board.user_move(m_count)
        else:
            game_board.computer_move()
        m_count += 1
        
        winner = game_board.find_winner()
        
        if winner:
            print('The {} is the winner.\n'.format('user' if winner == 'X' else 'machine'))
            break
        if game_board.are_spaces_filled():
            print('Stalemate! Neither the user nor the machine is a winner...')
            break

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