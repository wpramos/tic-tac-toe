import random, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.disable(logging.DEBUG)

class Box():
    all_boxes = []

    def __init__(self, on_left=None, on_right=None, on_top=None, on_bottom=None, mark=' '):
        self.on_left = on_left
        self.on_right = on_right
        self.on_top = on_top
        self.on_bottom = on_bottom
        self.mark = mark

        self.all_boxes.append(self)
        logging.debug(self.all_boxes)

    def set_attributes(self, **kwargs):
        '''This method is used to set the attributes of a Box class object, by passing them as keyword arguments.'''
        for k, v in kwargs.items():
            setattr(self, k, v)

    def is_row_complete(self):
        '''This method returns True if the row containing the box is completed by one player.'''
        current_box = self

        ordered_row = [current_box.mark]

        while True:
            if current_box.on_left:
                ordered_row.insert(0, current_box.on_left.mark)
                current_box = current_box.on_left
            else:
                current_box = self
                break

        while True:
            if current_box.on_right:
                ordered_row.append(current_box.on_right.mark)
                current_box = current_box.on_right
            else:
                break
        
        if ordered_row.count('X') == 3 or ordered_row.count('O') == 3:
            return True

    def is_column_complete(self):
        '''This method returns True if the column containing the box is completed by one player.'''
        current_box = self

        ordered_column = [current_box.mark]

        while True:
            if current_box.on_top:
                ordered_column.insert(0, current_box.on_top.mark)
                current_box = current_box.on_top
            else:
                current_box = self
                break

        while True:
            if current_box.on_bottom:
                ordered_column.append(current_box.on_bottom.mark)
                current_box = current_box.on_bottom
            else:
                break
        
        if ordered_column.count('X') == 3 or ordered_column.count('O') == 3:
            return True

    def is_diagonal_complete(self):
        '''This method returns True if either one of the diagonals is completed by one player.'''
        if self.on_left and self.on_right and self.on_top and self.on_bottom:
            ordered_diagonal_1 = [self.on_left.on_top.mark, self.mark, self.on_right.on_bottom.mark]
            ordered_diagonal_2 = [self.on_left.on_bottom.mark, self.mark, self.on_right.on_top.mark]

            if ordered_diagonal_1.count('X') == 3 or ordered_diagonal_1.count('O') == 3:
                return True
            elif ordered_diagonal_2.count('X') == 3 or ordered_diagonal_2.count('O') == 3:
                return True

    def __repr__(self):
        return 'Box(on_left={}, on_right={}, on_top={}, on_bottom={}, mark={})'.format(
            str(self.on_left),
            str(self.on_right),
            str(self.on_top),
            str(self.on_bottom),
            repr(self.mark)
        )

class Board:
    def __init__(self):
        self.top_left = Box()
        self.top_center = Box()
        self.top_right = Box()
        self.middle_left = Box()
        self.middle_center = Box()
        self.middle_right = Box()
        self.bottom_left = Box()
        self.bottom_center = Box()
        self.bottom_right = Box()

        self.top_left.set_attributes(on_right = self.top_center, on_bottom = self.middle_left)
        self.top_center.set_attributes(on_left = self.top_left, on_right = self.top_right, on_bottom = self.middle_center)
        self.top_right.set_attributes(on_left = self.top_center, on_bottom = self.middle_right)
        self.middle_left.set_attributes(on_right = self.middle_center, on_top = self.top_left, on_bottom = self.bottom_left)
        self.middle_center.set_attributes(on_left = self.middle_left, on_right = self.middle_right, on_top = self.top_center, on_bottom = self.bottom_center)
        self.middle_right.set_attributes(on_left = self.middle_center, on_top = self.top_right, on_bottom = self.bottom_right)
        self.bottom_left.set_attributes(on_right = self.bottom_center, on_top = self.middle_left)
        self.bottom_center.set_attributes(on_left = self.bottom_left, on_right = self.bottom_right, on_top = self.middle_center)
        self.bottom_right.set_attributes(on_left = self.bottom_center, on_top = self.middle_right)
        
        self.available_boxes = ['top_left', 'top_center', 'top_right', 'middle_left', 'middle_center', 'middle_right', 'bottom_left', 'bottom_center', 'bottom_right']

    def user_move(self, move_count):
        '''This method requests user input and executes the user's move.'''
        logging.debug("Scope: Board class' user_move() method")
        if move_count < 2:
            print('Please make your move...\n\nRespond with a combination of Top/Middle/Bottom\nand Left/Center/Right, separated with a hyphen.\n\nFor instance, "Top-Right"/"Bottom-Center"\n')
        while True:
            player_move = input('Your Move: ').lower().replace('-', '_')
            if hasattr(self, player_move):
                selected_box = getattr(self, player_move)
                selected_box.mark = 'X'
                self.available_boxes.remove(player_move)
                self.print_board()
                return
            else:
                print('\nTry "Top-Left", for instance.\n')
                continue

    def computer_move(self):
        '''This method executes the computer's move.'''
        logging.debug("Scope: Board class' computer_move() method")
        print("Machine's Move: ")
        machine_move = self.available_boxes[random.randint(0, len(self.available_boxes) - 1)]
        selected_box = getattr(self, machine_move)
        selected_box.mark = 'O'
        self.available_boxes.remove(machine_move)
        self.print_board()

    def are_spaces_filled(self):
        '''This method checks to see if every space in the board is filled.'''
        if len(self.available_boxes) == 0:
            return True
        else:
            return False

    def find_winner(self):
        '''This method runs through each box, to see if either the row, column or diagonal containing it is complete 
        and returns the mark of the winner.'''
        for box in Box.all_boxes:
            if box.is_row_complete():
                return box.mark
            elif box.is_column_complete():
                return box.mark
            elif box.is_diagonal_complete():
                return box.mark

    def print_board(self):
        '''This method displays a visual representation of the board in the console.'''
        print('\n{} | {} | {}'.format(self.top_left.mark, self.top_center.mark, self.top_right.mark))
        print(' ------- ')
        print('{} | {} | {}'.format(self.middle_left.mark, self.middle_center.mark, self.middle_right.mark))
        print(' ------- ')
        print('{} | {} | {}\n'.format(self.bottom_left.mark, self.bottom_center.mark, self.bottom_right.mark))

def main():
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

if __name__ == '__main__':
    main()